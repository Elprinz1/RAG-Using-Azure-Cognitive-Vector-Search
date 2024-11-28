import pandas as pd
from langchain_community.document_loaders import TextLoader
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from config import Config
from utils import TextProcessor
from utils import AzureVectorSearch


def main():
    # Load and preprocess data
    transcript_df = pd.read_csv("data/raw_data/meeting_transcriptions.csv")

    # Clean the first transcript
    transcript = transcript_df["conversation"].values[0]
    transcript = TextProcessor.clean_text(transcript)

    # Create vector search index
    vector_search = AzureVectorSearch()
    vector_search.create_index()

    # Prepare documents
    text_splitter = CharacterTextSplitter(
        chunk_size=3500, chunk_overlap=100, separator=" ")
    documents = text_splitter.split_documents(
        [Document(page_content=transcript)])

    # Upload documents
    vector_search.upload_documents(documents)

    # Example search
    query = "What is the purpose of the meeting?"
    results = vector_search.search(query)

    # Print search results
    for result in results:
        print(f"Score: {result['@search.score']}")
        print(f"Content: {result['content']}\n")


if __name__ == "__main__":
    main()
