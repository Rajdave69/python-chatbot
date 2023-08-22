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

  addMessage(message, "sent", false)

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

      addMessage(data.response, "received")

    })
    .catch(error => {
      messageInput.value = ""

      console.error('Error:', error);
      addMessage("There was an error.", "received", true, true)

    });

});

function addMessage(message, type, delay = true, error = false) {

  // Get the messagebox element
  const messageBox = document.getElementsByClassName('chat-panel')[0]

  // Create the actual bubble and assign the message
  const messageBubble = document.createElement("div")
  messageBubble.className = "message-bubble " + type
  messageBubble.innerText = message

  // If it's an error, change the style and make it red
  if (error) {
    messageBubble.style = "color: red; border: 2px solid rgba(255, 0, 0, 0.5);"
  }

  // Add a delay of .5 seconds if specified
  setTimeout(() => {
    messageBox.appendChild(messageBubble)
    messageBubble.scrollIntoView()
  }, delay ? 500 : 0);

}



document.addEventListener("DOMContentLoaded", function () {
  const formBox = document.querySelector(".form-box");
  const screenHeight = window.innerHeight;
  const formBoxHeight = formBox.clientHeight;
  const middlePosition = (screenHeight - formBoxHeight) / 2;

  formBox.style.bottom = `-${formBoxHeight}px`; /* Start from below the screen */
  formBox.style.opacity = "1"; /* Fade in the form-box */

  // Trigger the animation after a short delay for smoother transition
  setTimeout(function () {
    formBox.style.bottom = `${middlePosition}px`; /* Move up to middle position */
  }, 100); // Adjust the delay as needed
});


// add event listener to on window resize
window.addEventListener("resize", () => {
    const formBox = document.querySelector(".form-box");
    const screenHeight = window.innerHeight;
    const formBoxHeight = formBox.clientHeight;
    const middlePosition = (screenHeight - formBoxHeight) / 2;

    formBox.style.bottom = `${middlePosition}px`; /* Move up to middle position */
});