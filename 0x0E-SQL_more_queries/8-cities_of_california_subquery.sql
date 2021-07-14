-- script that lists all the cities of California that can be
SELECT id, name 
FROM cities
WHERE states_id =
	(SELECT id
	FROM states
	WHERE name = "California")
ORDER BY id ASC;
