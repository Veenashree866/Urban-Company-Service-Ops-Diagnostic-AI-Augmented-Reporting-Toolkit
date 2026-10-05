-- 01_dedup_and_joins.sql

-- (a) List every duplicated partner_id in the raw import.
SELECT partner_id, COUNT(*) AS duplicate_count
FROM partners_import
GROUP BY partner_id
HAVING COUNT(*) > 1;

-- (b) Build the clean partners table.
-- Grouping by every column removes only exact duplicate rows.
DROP TABLE IF EXISTS partners;

CREATE TABLE partners AS
SELECT
    partner_id,
    city,
    primary_category,
    rating,
    active,
    days_since_onboarding
FROM partners_import
GROUP BY
    partner_id,
    city,
    primary_category,
    rating,
    active,
    days_since_onboarding;

-- (a) INNER JOIN diagnostic: every booking should resolve to a clean partner.
SELECT b.booking_id, b.partner_id, p.partner_id AS matched_partner_id
FROM bookings AS b
INNER JOIN partners AS p
    ON b.partner_id = p.partner_id;

-- Explicit orphan check: should return zero rows.
SELECT b.booking_id, b.partner_id
FROM bookings AS b
LEFT JOIN partners AS p
    ON b.partner_id = p.partner_id
WHERE p.partner_id IS NULL;

-- (b) Categories that have never received a booking.
SELECT c.category
FROM categories AS c
LEFT JOIN bookings AS b
    ON c.category = b.category
WHERE b.booking_id IS NULL;

-- (c) Partners that have never received a booking.
SELECT p.partner_id
FROM partners AS p
LEFT JOIN bookings AS b
    ON p.partner_id = b.partner_id
WHERE b.booking_id IS NULL;

-- (d) Compare COUNT(*) with COUNT(b.booking_id) for every category.
SELECT
    c.category,
    COUNT(*) AS joined_rows,
    COUNT(b.booking_id) AS booking_count
FROM categories AS c
LEFT JOIN bookings AS b
    ON c.category = b.category
GROUP BY c.category
ORDER BY c.category;

-- For the zero-booking category, COUNT(*) is 1 because the LEFT JOIN keeps
-- the category row with an all-NULL booking side; COUNT(b.booking_id) is 0
-- because it counts only non-NULL real booking IDs.
