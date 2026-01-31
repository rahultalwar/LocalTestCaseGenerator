# SOP: Backend Architecture

## Goal
Reliable communication between the Web UI and the Ollama model.

## Principles
1.  **Stateless**: The server does not maintain conversation history (unless explicitly requested, but for now it's single-turn generation).
2.  **Error Handling**: If Ollama fails, return a graceful 500 error with a descriptive message to the UI.
3.  **Template Management**: The backend applies the System Template to the User Query.

## API Endpoints

### `POST /api/chat`
- **Input**: `{"user_query": "string"}`
- **Process**:
    1.  Load `TEST_CASE_TEMPLATE`.
    2.  Construct prompt: `f"{TEST_CASE_TEMPLATE}\n\nUser Query: {user_query}"`.
    3.  Call Ollama API: `POST /api/generate` (model=`llama3.2`).
- **Output**: `{"response": "markdown string", "status": "success"}`

## Recovery
- If Ollama Connection refused: Suggest ensuring `ollama serve` is running.
