console.log("Hello World")


const form = document.getElementById("form")
const sendButton = document.getElementById("sendButton")
const messageInput = document.getElementById("inputbox")



// Add an event listener to the form's submit event
form.addEventListener('submit', function (event) {
  // Prevent the default form submission behavior
  event.preventDefault();

});


sendButton.addEventListener("click", () => {
  const message = messageInput.value
  console.log(message)
  if (message === "") return

  const messagebox = document.getElementsByClassName('chatbox-panel')[0]

  // create div
  const sentMessage = document.createElement("div")
  sentMessage.className = "message-bubble sent"
  sentMessage.innerText = message

  messagebox.appendChild(sentMessage)

  /// Define the URL
  const url = 'http://127.0.0.1:5000/chatbot';

  // Define the JSON payload
  const payload = {
    user_input: message
  };

  // Set up the fetch request
  fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
      console.log('Response:', data);

      // Clear the input box
    messageInput.value = ""

      // Create receiving messagebox

      const messageBubble = document.createElement("div")
      messageBubble.className = "message-bubble received"
      messageBubble.innerText = data.response

      messagebox.appendChild(messageBubble)

      messageBubble.scrollIntoView()

    })
    .catch(error => {
      console.error('Error:', error);
    });







});


// });
