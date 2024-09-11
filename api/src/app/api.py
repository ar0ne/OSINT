from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.scans.views import router as scans_router


class ErrorMessage(BaseModel):
    msg: str


class ErrorResponse(BaseModel):
    detail: Optional[List[ErrorMessage]]


api_router = APIRouter(
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)


api_router.include_router(
    scans_router, prefix="/scans", tags=["scans"]
)
