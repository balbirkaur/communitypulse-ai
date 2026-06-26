# CommunityPulse AI Architecture

## System Overview

CommunityPulse AI is built on a multi-agent decision intelligence platform powered by Google Cloud technologies.

## Architecture Flow

```
API Requests
   │
   ▼
FastAPI Application (main.py)
   │
   ├─── /api/v1/health (Health Check)
   ├─── /api/v1/analytics (Analytics Endpoint)
   ├─── /api/v1/prediction (Prediction Endpoint)
   └─── /api/v1/chat (Chat Endpoint)
   │
   ▼
Decision Engine (Orchestrator)
   │
   ├── Step 1: Analytics Agent
   │   └─ Analyzes community data using BigQuery
   │
   ├── Step 2: Prediction Agent
   │   └─ Generates forecasts using BigQuery ML
   │
   ├── Step 3: Policy Agent
   │   └─ Analyzes policy implications
   │
   └── Step 4: Decision Agent (Gemini)
       └─ Synthesizes all inputs for final decision
   │
   ▼
Backend Services
   │
   ├── BigQuery Service (Data queries & analysis)
   ├── Vertex AI Service (ML models & embeddings)
   └── Vector Search Service (Semantic search)
   │
   ▼
Google Cloud Infrastructure
   │
   ├── BigQuery (Data warehouse)
   ├── Vertex AI (Model training & serving)
   ├── Cloud Run (Deployment)
   └── Cloud Storage (Data storage)
```

## Component Details

### 1. API Layer (`app/api/`)

- **health.py**: Health check and readiness endpoints
- **analytics.py**: Analytics query endpoints
- **chat.py**: Conversational AI endpoints
- **prediction.py**: ML prediction endpoints

### 2. Decision Engine (`app/agents/decision_engine.py`)

Central orchestrator that:

1. Routes queries to appropriate agents
2. Manages agent execution pipeline
3. Combines results for final decision
4. Handles error scenarios

### 3. Agent Layer (`app/agents/`)

- **AnalyticsAgent**: Data analysis using BigQuery
- **PredictionAgent**: Forecasting using BigQuery ML
- **PolicyAgent**: Policy impact analysis
- **DecisionAgent**: Final decision synthesis using Gemini

### 4. Service Layer (`app/services/`)

- **BigQueryService**: Query execution, data operations
- **VertexService**: Model predictions, embeddings
- **VectorSearchService**: Semantic search operations

### 5. Core Layer (`app/core/`)

- **config.py**: Configuration management
- **settings.py**: Settings and environment handling

## Data Flow Example

```
User Query: "What is the impact of implementing new community policy X?"
│
├─→ Analytics Agent: "Current community metrics are..."
├─→ Prediction Agent: "If implemented, we predict..."
├─→ Policy Agent: "Policy implications include..."
└─→ Decision Agent: "Recommendation: ... because..."
│
└─→ Final Response: Comprehensive decision with all perspectives
```

## Deployment Architecture

### Local Development

```
Local Machine
└── FastAPI Server (uvicorn)
    └── Agents (in-process)
```

### Cloud Deployment (Google Cloud Run)

```
Cloud Run Service
└── FastAPI Container
    └── Decision Engine + Agents
        └── Google Cloud Services
            ├── BigQuery
            ├── Vertex AI
            └── Cloud Storage
```

## Configuration

### Environment Variables

- `PORT`: Server port (default: 8000)
- `GCP_PROJECT_ID`: Google Cloud project ID
- `GCP_LOCATION`: GCP region (default: us-central1)
- `BIGQUERY_DATASET`: BigQuery dataset name
- `VERTEX_MODEL_NAME`: Vertex AI model name
- `OPENAI_API_KEY`: OpenAI API key (if using external LLM)

### Settings File

Configuration is managed through `app/core/config.py` using Pydantic.

## Key Features

1. **Multi-Agent Orchestration**: Coordinated analysis from multiple specialized agents
2. **Cloud-Native**: Built on Google Cloud infrastructure
3. **Scalable**: Containerized for Cloud Run deployment
4. **Observable**: Comprehensive logging and request tracking
5. **Error Handling**: Global exception handling with consistent error responses
6. **API Documentation**: Interactive Swagger UI at `/docs`

## API Endpoints

### Health Check

- `GET /api/v1/health` - Application health status

### Analytics

- `GET /api/v1/analytics/summary` - Analytics summary
- `GET /api/v1/analytics/trends` - Trend analysis

### Chat

- `POST /api/v1/chat/message` - Send message to AI agent
- `GET /api/v1/chat/history` - Get chat history

### Prediction

- `POST /api/v1/prediction/predict` - Make predictions
- `GET /api/v1/prediction/models` - List available models

## Development Workflow

1. **Setup**: `py -m venv .venv && .\.venv\Scripts\Activate.ps1`
2. **Install**: `pip install -r requirements.txt`
3. **Run**: `py -m uvicorn app.main:app --reload`
4. **Test**: Visit `http://localhost:8000/docs`

## Future Enhancements

- [ ] Authentication & Authorization
- [ ] Rate limiting
- [ ] Caching layer (Redis)
- [ ] Advanced monitoring (Cloud Trace, Cloud Profiler)
- [ ] Streaming responses for long-running operations
- [ ] WebSocket support for real-time updates
