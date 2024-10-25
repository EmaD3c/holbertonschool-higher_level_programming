-- Use the database 'hbtn_0d_usa'

SELECT cities.id, cities.name, states.name  FROM cities
-- effectue une jointure interne entre les tables cities et states
	INNER JOIN states ON cities.state_id = states.id
ORDER BY id ASC;
