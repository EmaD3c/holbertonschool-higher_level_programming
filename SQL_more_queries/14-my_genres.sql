-- Sélectionne le nom des genres de la table tv_genres
SELECT tv_genres.name
FROM tv_shows
-- Lie la table tv_shows à la table tv_show_genres sur l'identifiant de l'émission
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Lie la table tv_show_genres à la table tv_genres sur l'identifiant du genre
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Filtre pour ne récupérer que les genres de l'émission intitulée "Dexter"
WHERE tv_shows.title = 'Dexter'
-- Trie les résultats par ordre croissant selon le nom du genre
ORDER BY tv_genres.name ASC;
