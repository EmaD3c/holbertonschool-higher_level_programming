-- Counts records for each score in 'second_table'.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
