const chatMessages = document.getElementById('chat-messages');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const newChatButton = document.getElementById('new-chat');
const conversationList = document.getElementById('conversation-list');

let conversations = [];
let currentConversationId = null;

// add a message to the chat
function addMessage(text, isUser) {
    const messageWrapper = document.createElement('div');
    messageWrapper.style.width = '100%';
    messageWrapper.style.clear = 'both';

    const messageElement = document.createElement('div');
    messageElement.classList.add('message', isUser ? 'user-message' : 'bot-message');
    messageElement.textContent = text;

    messageWrapper.appendChild(messageElement);
    chatMessages.appendChild(messageWrapper);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// start a new conversation
function startNewConversation() {
    currentConversationId = Date.now();
    conversations.unshift({
        id: currentConversationId,
        messages: []
    });
    updateConversationList();
    chatMessages.innerHTML = '';
}

// update the conversation list in the sidebar
function updateConversationList() {
    conversationList.innerHTML = '';
    conversations.forEach(conv => {
        const item = document.createElement('div');
        item.classList.add('conversation-item');
        item.textContent = conv.messages.length > 0 ? conv.messages[0].text.substring(0, 30) + '...' : 'New Conversation';
        item.onclick = () => loadConversation(conv.id);
        conversationList.appendChild(item);
    });
}

// load a convo
function loadConversation(id) {
    currentConversationId = id;
    chatMessages.innerHTML = '';
    const conversation = conversations.find(conv => conv.id === id);
    conversation.messages.forEach(msg => addMessage(msg.text, msg.isUser));
}

// Event listener for form submission
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = userInput.value.trim();
    if (!query) return;

    addMessage(query, true);
    userInput.value = '';

    try {
        const response = await fetch('/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });

        if (!response.ok) throw new Error('Network response was not ok');

        const data = await response.json();
        
        // Add a small delay before adding the bot message
        setTimeout(() => {
            addMessage(data.response, false);
            
            const conversation = conversations.find(conv => conv.id === currentConversationId);
            conversation.messages.push({ text: query, isUser: true }, { text: data.response, isUser: false });
            updateConversationList();
        }, 100);
    } catch (error) {
        console.error('Error:', error);
        addMessage('Sorry, an error occurred. Please try again later.', false);
    }
});

// Event listener for new chat button
newChatButton.addEventListener('click', startNewConversation);

// Initialize the app
startNewConversation();