from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.requests import Request
import logging
import time
import os

from app.core.settings import get_settings
from app.api import health, analytics, chat, prediction

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get settings
settings = get_settings()

# Define API tags metadata
tags_metadata = [
    {
        "name": "Health",
        "description": "Application health and status checks"
    },
    {
        "name": "Analytics",
        "description": "BigQuery analytics"
    },
    {
        "name": "Prediction",
        "description": "BigQuery ML forecasting"
    },
    {
        "name": "Chat",
        "description": "Gemini conversational analytics"
    }
]

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="""
CommunityPulse AI

AI-powered Decision Intelligence Platform

Google Cloud Gen AI Academy APAC 2026
""",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Handle all unhandled exceptions globally."""
    logger.exception(exc)
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": str(exc)
        }
    )


# HTTP request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all HTTP requests with processing time."""
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    logger.info(
        f"{request.method} {request.url.path} {process_time:.3f}s"
    )
    return response


# Include routers
app.include_router(
    health.router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    analytics.router,
    prefix="/api/v1",
    tags=["Analytics"]
)

app.include_router(
    chat.router,
    prefix="/api/v1",
    tags=["Chat"]
)

app.include_router(
    prediction.router,
    prefix="/api/v1",
    tags=["Prediction"]
)


@app.get("/")
async def root():
    """Root endpoint with application information."""
    return {
        "project": "CommunityPulse AI",
        "version": "0.1.0",
        "hackathon": "Google Cloud Gen AI Academy APAC Cohort 2",
        "cloud": "Google Cloud",
        "status": "Running",
        "docs": "/docs"
    }


@app.on_event("startup")
async def startup_event():
    """Handle startup events."""
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    logger.info("Initializing Vertex AI...")
    logger.info("Initializing BigQuery...")
    logger.info("Loading LangGraph...")
    logger.info("CommunityPulse AI Ready")


@app.on_event("shutdown")
async def shutdown_event():
    """Handle shutdown events."""
    logger.info(f"Shutting down {settings.app_name}")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", settings.port))
    uvicorn.run(app, host=settings.host, port=port)