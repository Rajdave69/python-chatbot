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

  const messagebox = document.getElementsByClassName('chat-panel')[0]

  // create div
  const sentMessage = document.createElement("div")
  sentMessage.className = "message-bubble sent"
  sentMessage.innerText = message

  messagebox.appendChild(sentMessage)
  sentMessage.scrollIntoView()

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

      setTimeout(() => {
        messagebox.appendChild(messageBubble)
        messageBubble.scrollIntoView()
      }, 500);

    })
    .catch(error => {
      messageInput.value = ""


      console.error('Error:', error);
      const messageBubble = document.createElement("div")
      messageBubble.className = "message-bubble received"
      messageBubble.style = "color: red; border: 2px solid rgba(255, 0, 0, 0.5);"
      messageBubble.innerText = "There was an error. Please try again later."

      // sleep for 0.5 seconds
      setTimeout(() => {
        messagebox.appendChild(messageBubble)
        messageBubble.scrollIntoView()
      }, 500);



    });




});


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