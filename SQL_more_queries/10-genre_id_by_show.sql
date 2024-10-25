-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
-- récupérer les titres des émissions tv_shows.title en fonction des genres associés via l’identifiant de l’émission tv_show_genres.show_id
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
