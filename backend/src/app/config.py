from starlette.config import Config

config = Config(".env")

# database
DATABASE_HOSTNAME = config("DATABASE_HOSTNAME")
# this will support special chars for credentials
DATABASE_USER = config("DATABASE_USER")
DATABASE_PASSWORD = config("DATABASE_PASSWORD")
DATABASE_NAME = config("DATABASE_NAME", default="scanapp_db")
DATABASE_PORT = config("DATABASE_PORT", default="5432")

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}"

PAGINATION_PAGE_SIZE = config("PAGINATION_PAGE_SIZE", default=5)

CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_BACKEND_URL = config("CELERY_BACKEND_URL")
