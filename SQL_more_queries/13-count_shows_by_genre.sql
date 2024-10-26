-- Affiche le nom du genre et le nombre d'émissions associées
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows
-- On commence par la table des genres.
FROM tv_genres
-- Lier les genres aux émissions via l’identifiant genre_id
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Grouper les résultats pour chaque genre
GROUP BY tv_genres.name
-- Trier par nombre d'émissions, en commençant par les genres ayant le plus de séries
ORDER BY number_of_shows DESC;
