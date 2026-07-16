SELECT
    c.name AS category,
    f.title,
    COUNT(r.rental_id) AS rentals,
    RANK() OVER (
        PARTITION BY c.name
        ORDER BY COUNT(r.rental_id) DESC
    ) AS rnk
FROM film f
INNER JOIN film_category fc
    ON f.film_id = fc.film_id
INNER JOIN category c
    ON fc.category_id = c.category_id
INNER JOIN inventory i
    ON f.film_id = i.film_id
INNER JOIN rental r
    ON i.inventory_id = r.inventory_id
GROUP BY
    c.name,
    f.title
ORDER BY
    c.name,
    rnk;