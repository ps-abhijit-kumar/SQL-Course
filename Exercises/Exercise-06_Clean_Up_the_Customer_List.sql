SELECT
    UPPER(first_name || ' ' || last_name) AS customer_name,
    SPLIT_PART(email, '@', 2) AS email_domain
FROM customer;