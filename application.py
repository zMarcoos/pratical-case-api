from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from src.routes import classify
from src.errors import handler


application = FastAPI(
    title="AutoU email classifier",
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
