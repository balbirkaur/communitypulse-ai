"""Agent router for managing agent interactions."""

from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class AgentRouter:
    """Route requests to appropriate agents."""

    def __init__(self):
        """Initialize the agent router."""
        self.agents: Dict[str, Any] = {}

    def register_agent(self, agent_type: str, agent_instance: Any) -> None:
        """Register an agent with the router."""
        self.agents[agent_type] = agent_instance
        logger.info(f"Registered agent: {agent_type}")

    async def route_request(self, agent_type: str, query: str, context: Optional[Dict] = None) -> Dict:
        """Route a request to the appropriate agent."""
        if agent_type not in self.agents:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        agent = self.agents[agent_type]
        logger.info(f"Routing request to {agent_type} agent")
        
        return await agent.process(query, context or {})

    def get_available_agents(self) -> list:
        """Get list of available agents."""
        return list(self.agents.keys())


# Global router instance
agent_router = AgentRouter()
