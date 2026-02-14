from collections.abc import Callable
from typing import Any
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from backend.utils.logging import logger


class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Any]
    ) -> Response:
        """
        Logs all incoming and outgoing request, response pairs. This method logs the request params,
        datetime of request, duration of execution. Logs should be printed using the custom logging module provided.
        Logs should be printed so that they are easily readable and understandable.

        :param request: Request received to this middleware from client (it is supplied by FastAPI)
        :param call_next: Endpoint or next middleware to be called (if any, this is the next middleware in the chain of middlewares, it is supplied by FastAPI)
        :return: Response from endpoint
        """
        # TODO:(Member) Finish implementing this method
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        starttime = time.perf_counter()

        Method = request.method
        Path = request.url.path
        Query_params = dict(request.query_params)

        logger.info(
            f"""Incoming request:
            Method: {Method},
            Path: {Path},
            Query Params: {Query_params},
            Time: {start_time}"""
        )

        response = await call_next(request)

        if response is not None:
            duration = time.perf_counter() - starttime
            logger.info(
                f"""Outgoing response:,
                Method: {Method},
                Path: {Path},
                Query Params: {Query_params},
                Duration: {duration:.4f} seconds"""
            )
        return response
        
        

