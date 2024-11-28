import re
import openai
from config import Config


class EmbeddingGenerator:
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)

    def generate_embeddings(self, content):
        """
        Generate embeddings for given content

        Args:
            content (str): Text to generate embeddings for

        Returns:
            list: Embedding vector or None if generation fails
        """
        try:
            content = ' '.join(content.split())
            content = re.sub(r'[^\w\s]', '', content.lower()).strip()

            # Truncate extremely long content if needed
            # OpenAI models have token limits
            max_tokens = 8192
            content = content[:max_tokens]
            if not content:
                print("Empty content after preprocessing")
                return None

            response = self.client.embeddings.create(
                input=[content],
                model=Config.EMBEDDING_MODEL
            )

            embedding = response.data[0].embedding
            if not embedding or len(embedding) == 0:
                print("Generated embedding is empty")
                return None

            return embedding

        except Exception as e:
            print(f"Embedding generation error: {e}")
            return None
