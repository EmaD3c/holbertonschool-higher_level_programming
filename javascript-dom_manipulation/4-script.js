const add_item = document.querySelector("#add_item");
const myList = document.querySelector(".my_list");

add_item.addEventListener("click", () => {
  // inside the click so u can create infinite item and not only one
  const li = document.createElement("li");
  li.textContent = "Item";
  myList.appendChild(li);
});
