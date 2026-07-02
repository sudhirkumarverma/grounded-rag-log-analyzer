def chunk_logs(log_text, chunk_size=3):
    """
    Simple log chunker for RAG MVP
    Groups consecutive log lines into chunks
    """
    lines = log_text.strip().split("\n")

    chunks = []
    for i in range(0, len(lines), chunk_size):
        chunk = "\n".join(lines[i:i + chunk_size])
        chunks.append(chunk)

    return chunks
