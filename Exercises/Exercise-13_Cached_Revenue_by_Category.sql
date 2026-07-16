DROP MATERIALIZED VIEW IF EXISTS category_revenue;

CREATE MATERIALIZED VIEW category_revenue AS
SELECT
    c.name AS category,
    SUM(p.amount) AS revenue
FROM payment p
INNER JOIN rental r
    ON p.rental_id = r.rental_id
INNER JOIN inventory i
    ON r.inventory_id = i.inventory_id
INNER JOIN film_category fc
    ON i.film_id = fc.film_id
INNER JOIN category c
    ON fc.category_id = c.category_id
GROUP BY c.name;

SELECT
    category,
    revenue
FROM category_revenue
ORDER BY revenue DESC
LIMIT 5;

REFRESH MATERIALIZED VIEW category_revenue;