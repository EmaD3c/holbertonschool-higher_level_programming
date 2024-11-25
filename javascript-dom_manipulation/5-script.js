const update_header = document.querySelector("#update_header");
const header = document.querySelector("header");

update_header.addEventListener("click", () => {
  header.textContent = "New Header!!!";
});
