## ABOUT THE PROJECT

This project is an initial exploration of LangChain for building an interactive question-answering system.

- The system allows users to ask questions.
- It searches a vector database to find relevant information.
- The database is populated with chunks extracted from multiple PDF documents.
- When a user asks a question, the system finds and returns the most relevant PDF chunk(s) as the answer.

The goal is to efficiently retrieve information from large collections of PDFs using natural language queries.

## ROADMAP

### Phase 1: Core Infrastructure Setup
- [ ] Set up PostgreSQL with pgvector extension
- [ ] Configure Ollama with embedding model (nomic-embed-text)
- [ ] Configure Ollama with LLM (llama3.1)
- [ ] Test basic database connectivity and vector operations

### Phase 2: Document Processing Pipeline
- [ ] Load PDF documents and extract text using LangChain and pypdf
- [ ] Split text into chunks with LangChain's text splitter
- [ ] Generate vector embeddings for each chunk using pre-trained models (sentence-transformers or Ollama)
- [ ] Store embeddings and metadata in pgvector (PostgreSQL)

### Phase 3: Retrieval System
- [ ] Use pgvector's built-in similarity search (e.g., cosine) to find relevant chunks
- [ ] Integrate LangChain retriever for querying pgvector
- [ ] Test retrieval accuracy and performance

### Phase 4: Question-Answering Chain
- [ ] Build RAG chain with LangChain
- [ ] Integrate Ollama LLM for response generation
- [ ] Create prompt templates for context injection
- [ ] Implement response formatting and citation tracking

### Phase 5: User Interface & Experience
- [ ] Create simple CLI interface for testing
- [ ] Add conversation memory for follow-up questions
- [ ] Implement basic error handling and validation
- [ ] Optional: Build web interface with Streamlit/Gradio

### Phase 6: Optimization & Production
- [ ] Add logging and monitoring
- [ ] Implement backup and data persistence strategies
- [ ] Documentation and deployment guides

## TECH STACK

- **LangChain**: Orchestration and RAG implementation
- **PostgreSQL + pgvector**: Vector database for embeddings storage
- **Ollama**: Local LLM and embedding models
- **sentence-transformers**: Embedding generation
- **pypdf**: PDF document processing
- **Python 3.12+**: Core development environment