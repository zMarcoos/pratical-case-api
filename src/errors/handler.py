from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging
import uuid

logger = logging.getLogger("application")
logging.basicConfig(level=logging.INFO)


def problem(status: int, title: str, detail: str | None, instance: str, type_: str = "about:blank"):
    return {
        "type": type_,
        "title": title,
        "status": status,
        "detail": detail,
        "instance": instance,
    }


async def http_exception_handler(request: Request, exc: HTTPException):
    trace_id = str(uuid.uuid4())
    logger.info("HTTPException %s %s -> %s (%s)",
                request.method, request.url.path, exc.detail, trace_id)
    return JSONResponse(
        status_code=exc.status_code,
        content=problem(
            status=exc.status_code,
            title="Erro de aplicação",
            detail=str(exc.detail),
            instance=str(request.url),
            type_="urn:autou:http-error"
        ),
        headers={"X-Trace-Id": trace_id},
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    trace_id = str(uuid.uuid4())
    logger.info("ValidationError %s %s -> %s (%s)",
                request.method, request.url.path, exc.errors(), trace_id)
    return JSONResponse(
        status_code=422,
        content={
            **problem(
                status=422,
                title="Erro de validação",
                detail="Dados inválidos. Veja 'errors' para detalhes.",
                instance=str(request.url),
                type_="urn:autou:validation-error"
            ),
            "errors": exc.errors(),
        },
        headers={"X-Trace-Id": trace_id},
    )


async def generic_exception_handler(request: Request, exc: Exception):
    trace_id = str(uuid.uuid4())
    logger.exception("Unhandled %s %s (%s)", request.method,
                     request.url.path, trace_id)
    return JSONResponse(
        status_code=500,
        content=problem(
            status=500,
            title="Erro interno do servidor",
            detail="Ocorreu um erro inesperado. Tente novamente mais tarde.",
            instance=str(request.url),
            type_="urn:autou:internal-error"
        ),
        headers={"X-Trace-Id": trace_id},
    )
