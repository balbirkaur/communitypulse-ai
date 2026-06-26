"""Health check endpoints."""

from fastapi import APIRouter, Depends
from app.core.settings import get_settings

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check(settings=Depends(get_settings)):
    """Health check endpoint."""
    return {
        "status": "healthy",
        "project": "may2026-cohort2",
        "region": settings.gcp_location,
        "bigquery": "connected",
        "vertex_ai": "ready",
        "version": settings.app_version
    }


@router.get("/ready")
async def readiness_check(settings=Depends(get_settings)):
    """Readiness check endpoint."""
    return {
        "status": "ready",
        "app": settings.app_name,
        "version": settings.app_version,
    }
