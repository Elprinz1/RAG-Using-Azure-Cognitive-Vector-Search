import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Azure Configuration
    AZURE_API_KEY = os.getenv("AZURE_API_KEY")
    AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")

    # Index Configuration
    INDEX_NAME = "meeting-transcripts"

    # Embedding Model
    EMBEDDING_MODEL = "text-embedding-ada-002"
