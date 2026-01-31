# Project Constitution (gemini.md)

## 1. Data Schemas
### Input Payload (Frontend -> Backend)
```json
{
  "user_query": "String: The feature description or input from user"
}
```

### Internal Logic
- **Template Variable**: `TEST_CASE_TEMPLATE` (Stored in code/env)
- **Model**: `llama3.2`

### Output Payload (Backend -> Frontend)
```json
{
  "response": "String: Markdown formatted test cases",
  "status": "success | error"
}
```

## 2. Behavioral Rules
- **Reliability**: If Ollama is offline, return a clear error message to the UI, don't crash.
- **Formatting**: Output must be Markdown to render nicely in the Chat UI.
- **Model enforcement**: Always use `model='llama3.2'` in API calls.

## 3. Architectural Invariants
- **Layer 1**: SOPs in `architecture/`
- **Layer 2**: FastAPI Backend (Router)
- **Layer 3**: Tools (Ollama Client)
- **UI**: Client-side rendering (HTML/JS)
- **Data-First**: strict JSON contracts between Frontend and Backend.

## 4. Maintenance Log
- **2026-01-31**: Initial Deployment.
- **Issue**: Ollama returned 404 for `llama3.2`.
- **Fix**: Updated model tag to `llama3.2:3b`.
- **Note**: Ensure `ollama serve` is running before starting the app.

