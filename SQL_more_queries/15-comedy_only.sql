-- Sélectionne uniquement la colonne title de la table tv_shows
SELECT tv_shows.title
FROM tv_shows
-- Relie tv_shows avec tv_show_genres en associant les id des émissions
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Relie tv_show_genres avec tv_genres en associant genre_id et id des genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Filtre pour n’inclure que les genres dont le nom est "Comedy"
WHERE tv_genres.name = 'Comedy'
-- Trie les résultats par ordre alphabétique du titre de l’émission
ORDER BY tv_shows.title ASC;
