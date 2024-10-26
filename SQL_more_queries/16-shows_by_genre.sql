-- Sélectionne les colonnes title (titre de l’émission) et name (nom du genre)
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
-- Lier toutes les émissions avec tv_show_genres, même celles qui n’ont pas de genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Lier tv_show_genres et tv_genres, pour obtenir les noms des genres (ou NULL si aucun genre associé)
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Trie les résultats par titre d’émission et, si un titre a plusieurs genres, par nom du genre en ordre alphabétique
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
