import logging
import os
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    log_level: int = int(os.getenv("LOG_LEVEL", 10))
    aws_region: str = os.getenv("AWS_REGION")
    sqs_trigger: str = os.getenv("SQS_TRIGGER")
    prompt_select_table = os.getenv("PROMPT_TABLE")
    prompt_create_query = os.getenv("PROMPT_QUERY")


app_config = AppConfig()
