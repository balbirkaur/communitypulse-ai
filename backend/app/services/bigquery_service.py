"""BigQuery service for database operations."""

import logging
from typing import Dict, Any, List, Optional
from google.cloud import bigquery

logger = logging.getLogger(__name__)


class BigQueryService:
    """Service for interacting with Google BigQuery."""

    def __init__(self, project_id: Optional[str] = None):
        """
        Initialize BigQuery service.
        
        Args:
            project_id: GCP project ID
        """
        self.project_id = project_id
        self.client = bigquery.Client(project=project_id)
        logger.info(f"BigQueryService initialized for project: {project_id}")

    async def query(self, sql: str) -> List[Dict]:
        """
        Execute a BigQuery query.
        
        Args:
            sql: SQL query string
            
        Returns:
            Query results as list of dictionaries
        """
        try:
            logger.info(f"Executing query: {sql[:100]}...")
            results = self.client.query(sql).result()
            return [dict(row) for row in results]
        except Exception as e:
            logger.error(f"Query failed: {str(e)}")
            raise

    async def insert(self, table_id: str, rows: List[Dict]) -> None:
        """
        Insert rows into a BigQuery table.
        
        Args:
            table_id: Full table ID (project.dataset.table)
            rows: List of row dictionaries
        """
        try:
            logger.info(f"Inserting {len(rows)} rows into {table_id}")
            errors = self.client.insert_rows_json(table_id, rows)
            if errors:
                logger.error(f"Insert errors: {errors}")
            else:
                logger.info("Rows inserted successfully")
        except Exception as e:
            logger.error(f"Insert failed: {str(e)}")
            raise

    async def get_table_schema(self, table_id: str) -> Dict:
        """Get the schema of a BigQuery table."""
        try:
            table = self.client.get_table(table_id)
            return {field.name: field.field_type for field in table.schema}
        except Exception as e:
            logger.error(f"Failed to get schema: {str(e)}")
            raise
