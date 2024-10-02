document.getElementById('send-btn').addEventListener('click', function() {
  let userInput = document.getElementById('user-input').value;

  fetch(`/chatbot/get-response/?user_input=${userInput}`)
      .then(response => response.json())
      .then(data => {
          let chatOutput = document.getElementById('chat-output');
          chatOutput.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
          chatOutput.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
          document.getElementById('user-input').value = '';  // Clear input field
      })
      .catch(error => console.error('Error:', error));
});
