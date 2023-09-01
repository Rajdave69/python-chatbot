/*

█▀█ ▄▀█   █  █▀      █▀▀ █ █ ▄▀█ ▀█▀ █▄▄ █▀█ ▀█▀
█▀▄ █▀█ █▄█  ▄█      █▄▄ █▀█ █▀█  █  █▄█ █▄█  █


Welcome to the source code of my chatbot! This is a simple chatbot that uses
a Flask backend to communicate with a Python chatbot. The chatbot is created
with the NLTK library.

 */



const form = document.getElementById("form");
const sendButton = document.getElementById("sendButton");
const messageInput = document.getElementById("inputbox");



// Add an event listener to the send message form
form.addEventListener('submit', function (event) {
  // Stop the form from reloading the page
  event.preventDefault();
});

// Add an event listener to the send button
sendButton.addEventListener("click", () => {
  // Get the message and check if it's empty
  const message = messageInput.value
  if (message === "") return

  // Create the message bubble
  addMessage(message, "sent", false)

  // Define the JSON payload
  const payload = {
    user_input: message
  };

  // Set up the fetch request
  fetch(`${document.location.origin}/chatbot`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
      console.debug('Response:', data);

      // Clear the input box and create the response bubble
      messageInput.value = ""
      addMessage(data.response, "received")
    })
    .catch(error => {
      messageInput.value = ""

      console.error('Error:', error);
      addMessage("There was an error while trying to reach the API.", "received", true, true)
    });

});

// Function to add a message to the chat box
function addMessage(message, type, delay = true, error = false) {

  // Get the messagebox element
  const messageBox = document.getElementsByClassName('chat-panel')[0]

  // Create the actual bubble and assign the message
  const messageBubble = document.createElement("div");
  messageBubble.className = "message-bubble " + type
  messageBubble.innerText = message

  // If it's an error, change the style and make it red
  if (error) {
    messageBubble.setAttribute("style", "color: red; border: 2px solid rgba(255, 0, 0, 0.5);")
  }

  // Add a delay of .5 seconds if specified
  setTimeout(() => {
    messageBox.appendChild(messageBubble)
    messageBubble.scrollIntoView()
  }, delay ? 500 : 0);

}


// Add an event listener for when the page is loaded
document.addEventListener("DOMContentLoaded", function () {
  // Get the form-box element and calculate the middle position
  const formBox = document.querySelector(".form-box");
  const screenHeight = window.innerHeight;
  const formBoxHeight = formBox.clientHeight;
  const middlePosition = (screenHeight - formBoxHeight) / 2;

  // Set the initial position and opacity
  formBox.style.bottom = `-${formBoxHeight}px`; /* Start from below the screen */
  formBox.style.opacity = "1"; /* Fade in the form-box */

  // Trigger the animation after a short delay for smoother transition
  setTimeout(function () {
    formBox.style.bottom = `${middlePosition}px`; /* Move up to middle position */
  }, 100); // Adjust the delay as needed

  // Sleep for 1.5 seconds and then send a welcome message
    setTimeout(function () {
        addMessage("Hello! I am the Qatar Expo 2023 chatbot. Try asking me about the venue, schedule, " +
            "or participating countries", "received", true)
    }, 1500); // Adjust the delay as needed
});


// add event listener to on window resize
window.addEventListener("resize", () => {
  // recalculate the middle position
  const formBox = document.querySelector(".form-box");
  const screenHeight = window.innerHeight;
  const formBoxHeight = formBox.clientHeight;
  const middlePosition = (screenHeight - formBoxHeight) / 2;

  // Center the form box
  formBox.style.bottom = `${middlePosition}px`; /* Move up to middle position */
});
