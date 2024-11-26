// sassurer que mon code sexecute une fois le dom completement charger 
document.addEventListener("DOMContentLoaded", () => {
const hello = document.getElementById("hello");

fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
// promesse ( resolue / rejeter)
  .then((response) => response.json())
  .then((data) => {
    hello.textContent = data.hello;
  })  
  // catch si il y une erreur dans les promesses 
  .catch((error) => console.error("Error fetching movies:", error));
});
