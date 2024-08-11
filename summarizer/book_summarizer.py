from langchain_ollama.embeddings import OllamaEmbeddings

ollama_embedding = OllamaEmbeddings(
    model_name="llama3.1",
    base_url="https://8a1a-35-186-153-205.ngrok-free.app:11434",
    ollama_additional_kwargs={
        "mirostat": 0,
        "num_ctx": 4096,
        "num_gpu": 1,
        "temperature": 0.6
    },
)

embeddings = ollama_embedding.aembed_documents()


