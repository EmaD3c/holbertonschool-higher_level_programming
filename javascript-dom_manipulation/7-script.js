const listMovies = document.getElementById("list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
// promesse ( resolue / rejeter)
  .then((response) => response.json())
  .then((data) => {
    data.results.forEach((movie) => {
      const listItem = document.createElement("li");
      listItem.textContent = movie.title;
      listMovies.appendChild(listItem);
    });
  })
  // catch si il y une erreur dans les promesses 
  .catch((error) => console.error("Error fetching movies:", error));
