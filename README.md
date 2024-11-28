# RAG Using Azure Cognitive Vector Search

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) solution using Azure Cognitive Vector Search for efficient information retrieval and context-aware generation. The system is designed to process audio transcriptions, generate embeddings, and perform semantic search.

## 🚀 Features

- Azure Cognitive Vector Search integration (Index config & creation)
- Semantic search capabilities
- Text preprocessing
- Embedding generation
- Audio transcription analysis

## 🛠 Prerequisites

- Python 3.8+
- Azure Account
- Azure Cognitive Search Service
- OpenAI API Key (optional, for advanced generation)

## 📦 Project Structure

```
azure_vector_search/
│
├── config/
│   ├── __init__.py
│   └── settings.py         # Configuration management
│
├── utils/
│   ├── __init__.py
│   ├── text_processor.py   # Text cleaning and preprocessing
│   ├── embedding_generator.py  # Generate vector embeddings
│   └── vector_search.py    # Azure Vector Search utilities
│
├── data/
│   └── raw_data/
│       └── meeting_transcriptions.csv  # Source data
│
├── vectors/
│   └── .gitkeep            # Placeholder for generated vector files
│
├── main.py                 # Primary application entry point
├── requirements.txt        # Project dependencies
└── .env                    # Environment variables
```

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Elprinz1/RAG-Using-Azure-Cognitive-Vector-Search.git
   cd RAG-Using-Azure-Cognitive-Vector-Search
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables in `.env`:
   ```
   AZURE_SEARCH_ENDPOINT=your_azure_search_endpoint
   AZURE_SEARCH_KEY=your_azure_search_key
   OPENAI_API_KEY=your_openai_api_key  # Optional
   ```

## 🚀 Usage

Run the main application:

```bash
python main.py
```

## 🔍 Key Components

- **Text Processor**: Clean and prepare text for embedding
- **Embedding Generator**: Convert text to vector representations
- **Vector Search**: Perform semantic search using Azure Cognitive Search

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature-directory`)
3. Commit your changes (`git commit -m 'Add some new update'`)
4. Push to the branch (`git push origin feature-directory`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🌟 Acknowledgments

- Azure Cognitive Services
- OpenAI
- Python Community

## 🔗 Contact

Your Name - coinhub.info@gmail.com

Project Link: [https://github.com/Elprinz1/RAG-Using-Azure-Cognitive-Vector-Search](https://github.com/Elprinz1/RAG-Using-Azure-Cognitive-Vector-Search)
