"""Decision engine that orchestrates all agents."""

import logging
from typing import Dict, Any, Optional
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.prediction_agent import PredictionAgent
from app.agents.policy_agent import PolicyAgent
from app.agents.decision_agent import DecisionAgent

logger = logging.getLogger(__name__)


class DecisionEngine:
    """Central orchestration engine for all decision-making agents."""

    def __init__(self):
        """Initialize the decision engine with all agents."""
        self.analytics_agent = AnalyticsAgent()
        self.prediction_agent = PredictionAgent()
        self.policy_agent = PolicyAgent()
        self.decision_agent = DecisionAgent()
        logger.info("Decision Engine initialized with all agents")

    async def process_query(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process a query through the decision engine pipeline.

        Flow:
        1. Analyze the data using Analytics Agent
        2. Generate predictions using Prediction Agent
        3. Analyze policy implications using Policy Agent
        4. Make final decision using Decision Agent

        Args:
            query: The user query or decision request
            context: Additional context for the query

        Returns:
            Comprehensive decision with analysis, predictions, and recommendations
        """
        context = context or {}
        logger.info(f"Processing query through Decision Engine: {query}")

        try:
            # Step 1: Analytics
            logger.info("Step 1: Running Analytics Agent")
            analytics_result = await self.analytics_agent.process(query, context)

            # Step 2: Prediction
            logger.info("Step 2: Running Prediction Agent")
            prediction_result = await self.prediction_agent.process(query, context)

            # Step 3: Policy Analysis
            logger.info("Step 3: Running Policy Agent")
            policy_result = await self.policy_agent.process(query, context)

            # Step 4: Decision Making
            logger.info("Step 4: Running Decision Agent")
            decision_context = {
                "analytics": analytics_result,
                "predictions": prediction_result,
                "policy": policy_result,
                "original_query": query
            }
            decision_result = await self.decision_agent.process(query, decision_context)

            # Combine all results
            final_result = {
                "status": "success",
                "query": query,
                "pipeline": {
                    "analytics": analytics_result,
                    "prediction": prediction_result,
                    "policy": policy_result,
                    "decision": decision_result
                }
            }

            logger.info("Decision Engine pipeline completed successfully")
            return final_result

        except Exception as e:
            logger.error(f"Error in Decision Engine pipeline: {str(e)}")
            return {
                "status": "error",
                "query": query,
                "error": str(e)
            }

    async def get_agent_status(self) -> Dict[str, str]:
        """Get status of all agents."""
        return {
            "analytics_agent": "ready",
            "prediction_agent": "ready",
            "policy_agent": "ready",
            "decision_agent": "ready"
        }


# Global decision engine instance
decision_engine = DecisionEngine()
