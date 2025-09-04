from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from routes import classify
from errors import handler
from processing import classifier


@asynccontextmanager
async def lifespan(app: FastAPI):
    classifier.load_model()
    yield

application = FastAPI(
    title="AutoU email classifier",
    lifespan=lifespan
)

application.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

application.include_router(
    classify.router, prefix="/classify", tags=["classification"])

application.add_exception_handler(
    HTTPException, handler.http_exception_handler)
application.add_exception_handler(
    RequestValidationError, handler.validation_exception_handler)
application.add_exception_handler(Exception, handler.generic_exception_handler)
