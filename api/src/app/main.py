import logging
from contextvars import ContextVar
from typing import Final, Optional
from uuid import uuid1

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import scoped_session
from starlette.requests import Request
from starlette.routing import compile_path

from .api import api_router
from .database.core import engine, sessionmaker

log = logging.getLogger(__name__)


async def not_found(request, exc):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": [{"msg": "Not Found."}]}
    )


exception_handlers = {404: not_found}


app = FastAPI(exception_handlers=exception_handlers, openapi_url="")


api = FastAPI(
    title="X web app",
    description="Welcome to X's API documentation!",
    root_path="/api/v1",
    docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
)
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_path_params_from_request(request: Request) -> str:
    path_params = {}
    for r in api_router.routes:
        path_regex, path_format, param_converters = compile_path(r.path)
        path = request["path"].removeprefix("/api/v1")  # remove the /api/v1 for matching
        match = path_regex.match(path)
        if match:
            path_params = match.groupdict()
    return path_params


def get_request_id() -> Optional[str]:
    return _request_id_ctx_var.get()


REQUEST_ID_CTX_KEY: Final[str] = "request_id"
_request_id_ctx_var: ContextVar[Optional[str]] = ContextVar(REQUEST_ID_CTX_KEY, default=None)


@api.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request_id = str(uuid1())

    # we create a per-request id such that we can ensure that our session is scoped for a particular request.
    # see: https://github.com/tiangolo/fastapi/issues/726
    ctx_token = _request_id_ctx_var.set(request_id)
    # path_params = get_path_params_from_request(request)

    # # if this call is organization specific set the correct search path
    # organization_slug = path_params.get("organization", "default")
    # request.state.organization = organization_slug
    # schema = f"dispatch_organization_{organization_slug}"
    # # validate slug exists
    # schema_names = inspect(engine).get_schema_names()
    # if schema in schema_names:
    #     # add correct schema mapping depending on the request
    #     schema_engine = engine.execution_options(
    #         schema_translate_map={
    #             None: schema,
    #         }
    #     )
    # else:
    #     return JSONResponse(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         content={"detail": [{"msg": f"Unknown database schema name: {schema}"}]},
    #     )

    try:
        session = scoped_session(sessionmaker(engine), scopefunc=get_request_id)
        request.state.db = session()
        response = await call_next(request)
    except Exception as e:
        raise e from None
    finally:
        request.state.db.close()

    _request_id_ctx_var.reset(ctx_token)
    return response


api.include_router(api_router)


app.mount("/api/v1", app=api)
