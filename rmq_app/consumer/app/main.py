from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.consumer import consume


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start up event for FastAPI application.
    await consume()

    yield
    
    # Shutdown event for FastAPI application.


app = FastAPI(lifespan=lifespan)

