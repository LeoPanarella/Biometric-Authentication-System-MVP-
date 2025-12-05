from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.core.logging_middleware import LoggingMiddleware
from app.core.exceptions import (
    BiometricNotFoundError,
    BiometricProcessingError,
)


def create_app() -> FastAPI:
    app = FastAPI(title="Biometric Authentication API")

    # 1. HTTPException padrão
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "type": "HTTPException",
                    "message": exc.detail,
                    "status_code": exc.status_code,
                    "path": str(request.url),
                }
            },
        )

    # 2. Erros de validação do FastAPI (body inválido, campos faltando, etc)
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        return JSONResponse(
            status_code=422,
            content={
                "error": {
                    "type": "ValidationError",
                    "message": "Erro de validação dos dados enviados.",
                    "details": exc.errors(),
                    "path": str(request.url),
                }
            },
        )

    # 3. Exceções personalizadas de biometria
    @app.exception_handler(BiometricNotFoundError)
    async def biometric_not_found_handler(
        request: Request, exc: BiometricNotFoundError
    ):
        return JSONResponse(
            status_code=404,
            content={
                "error": {
                    "type": "BiometricNotFoundError",
                    "message": str(exc),
                    "path": str(request.url),
                }
            },
        )

    @app.exception_handler(BiometricProcessingError)
    async def biometric_processing_error_handler(
        request: Request, exc: BiometricProcessingError
    ):
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "type": "BiometricProcessingError",
                    "message": str(exc),
                    "path": str(request.url),
                }
            },
        )

    # --------------------------------
    # REGISTRO DAS ROTAS
    # --------------------------------
    from app.api.v1.router import router as biometric_router
    app.include_router(biometric_router, prefix="/biometric", tags=["Biometric"])

    return app


app = create_app()
