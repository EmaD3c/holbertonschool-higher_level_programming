-- lists all shows contained in hbtn_0d_tvshows without a genre linked

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
-- récupérer les titres des émissions en fonction des genres associés
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- return null if its not a genre linked
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
