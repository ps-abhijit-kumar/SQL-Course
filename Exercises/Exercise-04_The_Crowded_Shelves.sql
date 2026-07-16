SELECT
    c.name AS category,
    COUNT(*) AS film_count
FROM film_category fc
JOIN category c
    ON fc.category_id = c.category_id
GROUP BY c.name
HAVING COUNT(*) > 65
ORDER BY film_count DESC;