
document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');
    const chatContainer = document.getElementById('chatContainer');
    const API_URL = '/api/chat';

    // Auto-resize textarea
    userInput.addEventListener('input', function () {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
        if (this.value === '') this.style.height = 'auto';
    });

    // Send Message Logic
    async function sendMessage() {
        const text = userInput.value.trim();
        if (!text) return;

        // 1. Add User Message to UI
        appendMessage('user', text);
        userInput.value = '';
        userInput.style.height = 'auto';
        sendBtn.disabled = true;

        // 2. Add Loading Indicator
        const loadingId = appendLoading();

        try {
            // 3. Call API
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_query: text })
            });

            const data = await response.json();

            // 4. Remove Loading & Add AI Response
            removeLoading(loadingId);

            if (response.ok && data.status === 'success') {
                appendMessage('ai', data.response);
            } else {
                appendMessage('system', 'Error: ' + (data.detail || 'Something went wrong.'));
            }

        } catch (error) {
            removeLoading(loadingId);
            appendMessage('system', 'Network Error: Could not connect to server.');
            console.error(error);
        } finally {
            sendBtn.disabled = false;
        }
    }

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Helper: Append Message
    function appendMessage(sender, text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender}-message`;

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';

        if (sender === 'ai') {
            // Parse Markdown
            contentDiv.innerHTML = marked.parse(text);
        } else {
            contentDiv.textContent = text;
        }

        msgDiv.appendChild(contentDiv);
        chatContainer.appendChild(msgDiv);
        scrollToBottom();
    }

    // Helper: Loading
    function appendLoading() {
        const id = 'loading-' + Date.now();
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ai-message`;
        msgDiv.id = id;

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.innerHTML = '<em>Generating test cases... <span class="spinner">⏳</span></em>';

        msgDiv.appendChild(contentDiv);
        chatContainer.appendChild(msgDiv);
        scrollToBottom();
        return id;
    }

    function removeLoading(id) {
        const el = document.getElementById(id);
        if (el) el.remove();
    }

    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
});
