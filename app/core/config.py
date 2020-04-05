import logging
import os.path as path
import sys
from typing import List
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from core.logging import InterceptHandler

dotenv_path = path.abspath(path.join(__file__ ,"../../../.env"))
config = Config(dotenv_path)

API_PREFIX = "/api"
VERSION = "0.0.0"
JWT_TOKEN_PREFIX = "Token"  # noqa: S105
DEBUG: bool = config("DEBUG", cast=bool, default=False)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)
PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)
# Redis
REDIS_HOST: str = config("REDIS_HOST", default="127.0.0.1")
REDIS_PORT: int = config("REDIS_PORT", cast=int, default=6379)
REDIS_DB: int = config("REDIS_DB", cast=int, default=0)
# uvicorn configuration
UVICORN_HOST: str = config("UVICORN_HOST", default="0.0.0.0")
UVICORN_PORT: int = config("UVICORN_PORT", cast=int, default=5000)
UVICORN_RELOAD: bool = config("UVICORN_RELOAD", cast=bool, default=False)
UVICORN_ACCESS_LOG: bool = config("UVICORN_ACCESS_LOG", cast=bool, default=False)
UVICORN_LOG_LEVEL: str = "debug" if DEBUG else "info"
#Options: 'critical', 'error', 'warning', 'info', 'debug', 'trace'
# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])