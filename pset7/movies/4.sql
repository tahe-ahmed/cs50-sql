-- n 4.sql, write a SQL query to determine the number of movies with an IMDb rating of 10.0.
-- Your query should output a table with a single column and a single row (plus optional header) containing the number of movies with a 10.0 rating.

SELECT  count(*) AS 'the number of movies with rating 10' FROM movies WHERE id IN (SELECT movie_id FROM ratings WHERE rating='10.0');

-- or

SELECT count(*) FROM 
movies JOIN ratings ON movies.id = ratings.movie_id 
WHERE rating=10;
