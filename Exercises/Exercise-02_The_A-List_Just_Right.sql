SELECT
    title,
    length
FROM film
WHERE length BETWEEN 60 AND 120
  AND title LIKE 'A%'
ORDER BY length ASC;