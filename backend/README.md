# Community Pulse AI Backend

This directory contains the FastAPI backend application for Community Pulse AI.

## Structure

- `app/` - Main application code
  - `api/` - API route handlers
  - `core/` - Core configuration and settings
  - `agents/` - AI agents for various tasks
  - `services/` - Business logic services
  - `models/` - Pydantic data models
  - `prompts/` - LLM prompt templates
  - `utils/` - Utility functions
  - `main.py` - FastAPI application entry point

- `tests/` - Unit and integration tests
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration

## Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the development server:

   ```bash
   python -m uvicorn app.main:app --reload
   ```

3. Access the API at `http://localhost:8000`
4. View API documentation at `http://localhost:8000/docs`
