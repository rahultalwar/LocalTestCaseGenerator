# Task Plan

## Phases
1. **Initialization**: [COMPLETED] Setup and Discovery.
2. **Blueprint**: [IN PROGRESS] Vision, Logic, and Schema.
3. **Link**: Connectivity verification (Ollama).
4. **Architect**: Build Backend (FastAPI) and Frontend (HTML/JS).
5. **Stylize**: Refine UI (CSS) and Response Formatting (Markdown).
6. **Trigger**: Deployment (Local Run Script).

## Goals
- **North Star**: Local LLM Test Case Generator (Chat UI) using Ollama (`llama3.2`).
- **Core Feature**: User inputs query -> System applies Template -> Ollama generates Test Cases -> Displayed in Chat.

## Checklists

### Phase 1: Blueprint
- [x] Discovery Questions
- [x] Define Schema (`gemini.md`)
- [ ] **Action Item**: Get the "proper Template" from user.

### Phase 2: Link
- [ ] Verify `ollama` is installed and running.
- [ ] Verify `llama3.2` model is pulled.
- [ ] Create `tools/verify_ollama.py`.

### Phase 3: Architect
- [ ] **Backend**:
    - [ ] `tools/server.py` (FastAPI setup)
    - [ ] `tools/ollama_client.py` (Wrapper for API)
- [ ] **Frontend**:
    - [ ] `ui/index.html` (Chat layout)
    - [ ] `ui/script.js` (Fetch logic)

### Phase 4: Stylize
- [ ] `ui/style.css` (Premium dark mode look)
- [ ] Render Markdown in Chat (e.g., using `marked.js`).

### Phase 5: Trigger
- [ ] Create `run.sh` to start everything suitable for local use.
