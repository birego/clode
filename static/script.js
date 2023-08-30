function sendQuestion() {
    var userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== '') {
        addToChat('Vous', userInput);
        document.getElementById('user-input').value = '';

        fetch('/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: userInput,
            }),
        })
        .then(response => response.json())
        .then(data => {
            var response = data.response;
            animateAssistantTyping(response);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}

function addToChat(sender, message) {
    var chatOutput = document.getElementById('chat-output');
    var messageElement = document.createElement('div');

    var senderIcon = document.createElement('span');
    if (sender === 'Vous') {
        senderIcon.setAttribute('id', 'user-icon');
        senderIcon.innerText = '👤';
    } else if (sender === 'Christian Birego') {
        senderIcon.setAttribute('id', 'assistant-icon');
        senderIcon.innerText = '💼';
    }

    messageElement.appendChild(senderIcon);
    messageElement.innerText = message;

    chatOutput.appendChild(messageElement);
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

function animateAssistantTyping(response) {
    var chatOutput = document.getElementById('chat-output');
    var assistantTypingElement = document.createElement('div');
    assistantTypingElement.setAttribute('class', 'assistant-typing');
    chatOutput.appendChild(assistantTypingElement);

    setTimeout(function () {
        chatOutput.removeChild(assistantTypingElement);
        addToChat('Christian Birego', response);
    }, 1000 + Math.random() * 1000); // Random delay for a more natural typing effect
}

function toggleDarkMode() {
    var body = document.body;
    body.classList.toggle('dark-mode');
}
