SELECT
    CASE
        WHEN length < 60 THEN 'Short'
        WHEN length BETWEEN 60 AND 120 THEN 'Medium'
        ELSE 'Long'
    END AS length_bucket,
    COUNT(*) AS films
FROM film
GROUP BY length_bucket
ORDER BY films DESC;