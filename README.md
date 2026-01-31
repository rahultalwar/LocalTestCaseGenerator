# ✨ Test Genie: Local LLM Test Case Generator

A local, privacy-focused tool that uses **Ollama** and **Deep Learning** to generate comprehensive test cases for your software features. Built with a modern **FastAPI** backend and a premium **Dark Mode UI**.

![Architecture Diagram](https://mermaid.ink/img/pako:eNp1k01vwyAMhv8K8nFK1Q_HnrbdZtJ22G6TDi4hCjQJSMWhqv--kLTSdOphOzz2Kz9-jO0FcykjWC_Y0rC9Zg38KmsEN-daKjD4gB00j5uSObC6r_c1FEXxkq_3yJ9gR_d-Qf4Kz3B4QY0CjQy0e_uC4xM84fAAk0aN7nQ6wW_4CAc4PMMBnh7g6QGeaVTjTI3uNbrX6K6p0Z0a3Wv0SFmF7hW60-iu0b1Gjxq9e4XuNHrQ6F6jR43uFbrT6E6jB43uNbprdL_C6F6j-xVG9xrdqzC61-hehdG9RvcqjO41ulfhH4zudPqHozudXmH0D0f3Gj1o9A9H9xrda3Sv0b0Kozud_sHoXqMHje41ulf4h9G9RvcqjO41uv8Xozud7jW6a3Sv0b0Kozud7jW61-heo_sVRvc63b8wutPpH4zuNbrX6F6jexVGdzrdvzC60-kfjO41utfoXqN7FUZ3Ov2D0b1GDxrda3Sv8A-je43uVRj9w9G9RvcqjO51un9hdKfTPxjda3Sv0b1G9yqM7nS6f2F079P9C6N7n-5fGN37dP_C6N6n-xdG9z7dvzC69-n-hdG9T_cvjO59un9hdO_T_Quje5_uXxjda3Sv0L0Ko3ud7l8Y3ft0_8Lo3qf7F0b3Pt2_MLr36f6F0b1P9y-M7n26f2F079P9C6N7n-5fGN37dP_C6F6je4W-Vxjda3Sv0P0Ko3uN7hX6X2F0r9G9Qv8rjO41ulfof4XRvUb3Cv2vMLrX6F6h_xVG9xrdK_S_wuheo3uF_lcY3Wt0r9D_CqN7je4V-l9hdK_RvUL_K4zuNbpX6H-F0b1G9wr9rzC61-heof8VRvca3Sv0v8LoXqN7hf5XGN1rdK_Q_wqje43uFfpfYXSv0b1C_yuM7jW6V-h_hdG9RvcK_a8wutfodH8Bf4x4zw?type=png)

## 🏗️ Architecture

The system follows a 3-tier architecture designed for privacy and local execution.

```mermaid
graph TD
    User([User]) -->|1. Type Feature Description| UI["Web UI (HTML/JS)"]
    UI -->|2. POST JSON| API["FastAPI Server (Python)"]
    API -->|3. Load Prompt Template| Tmpl["System Prompt Template"]
    API -->|4. Construct Full Prompt| LLM["Ollama (Llama 3.2)"]
    LLM -->|5. Return Generated Text| API
    API -->|6. Return Markdown| UI
    UI -->|7. Render Chat Response| User

    style UI fill:#1e293b,stroke:#6366f1,stroke-width:2px,color:#fff
    style API fill:#1e293b,stroke:#22c55e,stroke-width:2px,color:#fff
    style LLM fill:#1e293b,stroke:#eab308,stroke-width:2px,color:#fff
```

## 🚀 Getting Started

### Prerequisites
1.  **Python 3.8+**
2.  **Ollama** installed and running locally.
3.  **Llama 3.2 Model** pulled:
    ```bash
    ollama pull llama3.2:3b
    ```

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/rahultalwar/LocalTestCaseGenerator.git
    cd LocalTestCaseGenerator
    ```

2.  Run the setup & launch script:
    ```bash
    ./run.sh
    ```
    *(This script automatically creates a venv, installs dependencies, checks your Ollama connection, and starts the server.)*

3.  Open the App:
    - Go to `http://localhost:8000` in your browser.

## 🛠️ Usage

1.  **Enter a Prompt**: Type a feature description, e.g., *"A login page with OAuth support and 'Forgot Password' flow"*
2.  **Generate**: Click the send button.
3.  **Review**: The AI will generate a structured test plan including:
    - Test Case IDs
    - Pre-conditions
    - Steps
    - Expected Results

## ⚙️ Customization

To change the behavior of the AI, edit the `TEST_CASE_TEMPLATE` variable in `tools/server.py`.

```python
TEST_CASE_TEMPLATE = """
You are an expert QA Automation Engineer...
"""
```

## 📄 License
MIT
