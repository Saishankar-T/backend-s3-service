from starlette.middleware.base import BaseHTTPMiddleware
import logging
import time

logging.basicConfig(level=logging.INFO)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger = logging.getLogger("logging_middleware")
        logger.info(f"Request: {request.method} {request.url}")
        
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time

        logger.info(f"Response status: {response.status_code} Duration: {duration:.4f}s")
        
        response.headers["X-Process-Time"] = f"{duration:.4f}"
        
        return response
