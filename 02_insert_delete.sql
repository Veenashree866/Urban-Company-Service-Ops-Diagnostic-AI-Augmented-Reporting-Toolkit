-- 02_insert_delete.sql

-- (a) Remove the 3 dummy/test bookings.
DELETE FROM bookings
WHERE is_test = 1;

-- (b) Insert exactly these 3 new bookings.
INSERT INTO bookings VALUES
('B9001','P009','Mumbai','Deep Home Cleaning','2026-03-31',3200,'Paid',5,0,0,0),
('B9002','P041','Chennai','Plumbing','2026-03-31',640,'Paid',4,0,0,0),
('B9003','P035','Hyderabad','Electrical Repair','2026-03-31',980,'Pending',NULL,0,0,0);

-- Expected result immediately after DELETE + INSERT:
-- COUNT(*) = 600, SUM(amount_inr) = 1047973 (₹10,47,973)

SELECT COUNT(*), SUM(amount_inr)
FROM bookings;

-- LIKE query: partners whose primary_category starts with "Salon".
SELECT *
FROM partners
WHERE primary_category LIKE 'Salon%';

-- Exact Part B/C export query.
SELECT
    city,
    category,
    COUNT(*) AS bookings_count,
    SUM(amount_inr) AS revenue_inr,
    SUM(sla_breach_flag) AS sla_breaches
FROM bookings
GROUP BY city, category
ORDER BY city, category;
