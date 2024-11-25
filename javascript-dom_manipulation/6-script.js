// Sélectionner l'élément pour afficher le nom
const characterDiv = document.getElementById("character");

// Envoyer une requête Fetch pour récupérer les données du personnage
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
.then((response) => response.json())  // Convertir la réponse en JSON
.then(data => { //acceder aux donnes json et les utiliser
  const characterName = data.name; // Extrait le nom du perso 
  characterDiv.textContent = characterName; // l'afficher dans le dom
})
.catch(error => console.error("Erreur de récupération :", error));
