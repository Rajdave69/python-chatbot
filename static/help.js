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
