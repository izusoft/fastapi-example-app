from fastapi import FastAPI
from loguru import logger

async def connect_to_db(app: FastAPI) -> None:
    None
    #logger.info("Connecting to bd")
    # code ...
    #logger.info("Connection established")

async def close_db_connection(app: FastAPI) -> None:
    None
    #logger.info("Closing connection to db")
    #code ...
    #logger.info("Connection closed")