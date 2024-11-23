from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start up event for FastAPI application.
    yield
    # Shutdown event for FastAPI application.


app = FastAPI(lifespan=lifespan)
app.include_router(router)
