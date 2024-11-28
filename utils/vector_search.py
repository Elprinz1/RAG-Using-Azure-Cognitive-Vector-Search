import uuid
import json
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.models import VectorizedQuery
from azure.search.documents.indexes.models import (
    SearchIndex, SearchField, SimpleField, SearchableField,
    SearchFieldDataType, VectorSearch, VectorSearchProfile,
    HnswAlgorithmConfiguration
)
from azure.core.exceptions import ResourceNotFoundError
from config import Config
from utils import EmbeddingGenerator


class AzureVectorSearch:
    def __init__(self):
        self.endpoint = Config.AZURE_ENDPOINT
        self.credential = AzureKeyCredential(Config.AZURE_API_KEY)
        self.embedding_generator = EmbeddingGenerator()

    def create_index(self):
        """
        Create Azure Cognitive Search index
        """
        client = SearchIndexClient(
            endpoint=self.endpoint,
            credential=self.credential
        )

        # Vector search configuration
        vector_search = VectorSearch(
            profiles=[VectorSearchProfile(
                name="my-vector-config",
                algorithm_configuration_name="my_hnsw_algo_config"
            )],
            algorithms=[
                HnswAlgorithmConfiguration(
                    name="my_hnsw_algo_config",
                    kind="hnsw",
                    parameters={
                        "m": 4,
                        "efConstruction": 400,
                        "efSearch": 500,
                        "metric": "cosine"
                    }
                )
            ]
        )

        # Index fields
        fields = [
            SimpleField(name="documentId",
                        type=SearchFieldDataType.String, filterable=True, key=True, sortable=True),
            SearchableField(name="content", type=SearchFieldDataType.String),
            SearchField(name="embedding", type=SearchFieldDataType.Collection(
                SearchFieldDataType.Single), searchable=True, vector_search_dimensions=1536, vector_search_profile_name="my-vector-config")
        ]

        index = SearchIndex(
            name=Config.INDEX_NAME,
            fields=fields,
            vector_search=vector_search
        )


        try:
            existing_index = client.get_index(Config.INDEX_NAME)
            print(f"Index '{Config.INDEX_NAME}' already exists.")
            return
        except ResourceNotFoundError:
            # If the index doesn't exist, create it
            try:
                response = client.create_index(index)
                print(f"Index '{Config.INDEX_NAME}' created successfully.")
            except Exception as e:
                print(f"Error creating index: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def upload_documents(self, documents):
        """
        Upload documents to Azure Cognitive Search

        Args:
            documents (list): List of documents to upload
        """
        processed_docs = []
        for doc in documents:
            embeddings = self.embedding_generator.generate_embeddings(
                doc.page_content)
            if embeddings:
                processed_docs.append({
                    "documentId": str(uuid.uuid4()),
                    "content": doc.page_content,
                    "embedding": embeddings
                })

        try:
            search_client = SearchClient(
                endpoint=self.endpoint,
                index_name=Config.INDEX_NAME,
                credential=self.credential
            )
            result = search_client.upload_documents(documents=processed_docs)
            print("Upload of vector documents completed.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search(self, query, k_nearest_neighbors=3):
        """
        Perform vector search

        Args:
            query (str): Search query
            k_nearest_neighbors (int): Number of nearest neighbors to retrieve

        Returns:
            list: Search results
        """
        search_client = SearchClient(
            endpoint=self.endpoint,
            index_name=Config.INDEX_NAME,
            credential=self.credential
        )

        vectors = VectorizedQuery(
            vector=self.embedding_generator.generate_embeddings(query),
            k_nearest_neighbors=k_nearest_neighbors,
            fields="embedding"
        )

        try:
            responses = search_client.search(
                search_text=None,
                vector_queries=[vectors],
                select=["content"]
            )
            return list(responses)
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
