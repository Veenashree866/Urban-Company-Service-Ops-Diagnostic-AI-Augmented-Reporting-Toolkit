import random
import sqlite3
import csv
import os

# ============================================================
# 1. Project folder location
# ============================================================

random.seed(2604)

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# 2. Cities and Categories
# ============================================================

CITIES = [
    "Bengaluru",
    "Mumbai",
    "Delhi NCR",
    "Pune",
    "Hyderabad",
    "Chennai"
]

ACTIVE_CATEGORIES = [
    "AC Repair & Service",
    "Salon for Women",
    "Salon for Men",
    "Deep Home Cleaning",
    "Plumbing",
    "Electrical Repair"
]

HELD_OUT_CATEGORY = "Pest Control"

ALL_CATEGORIES = ACTIVE_CATEGORIES + [HELD_OUT_CATEGORY]


# ============================================================
# 3. Category price ranges
# ============================================================

CATEGORY_PRICE_RANGE = {
    "AC Repair & Service": (499, 2499),
    "Salon for Women": (699, 3499),
    "Salon for Men": (349, 1499),
    "Deep Home Cleaning": (999, 4999),
    "Plumbing": (199, 1499),
    "Electrical Repair": (199, 1999),
}

CATEGORY_WEIGHTS = [
    0.22,
    0.20,
    0.14,
    0.18,
    0.14,
    0.12
]


# ============================================================
# 4. Partners
# ============================================================

PARTNERS = []

partner_seq = 1

for city in CITIES:

    for _ in range(8):

        pid = f"P{partner_seq:03d}"

        cat = random.choices(
            ACTIVE_CATEGORIES,
            weights=CATEGORY_WEIGHTS,
            k=1
        )[0]

        rating = round(
            random.uniform(3.4, 5.0),
            1
        )

        PARTNERS.append({
            "partner_id": pid,
            "city": city,
            "primary_category": cat,
            "rating": rating,
            "active": True,
            "days_since_onboarding": random.randint(30, 500)
        })

        partner_seq += 1


# ============================================================
# 5. Idle partner
# ============================================================

IDLE_PARTNER_ID = f"P{partner_seq:03d}"

PARTNERS.append({
    "partner_id": IDLE_PARTNER_ID,
    "city": "Pune",
    "primary_category": "Plumbing",
    "rating": 0.0,
    "active": True,
    "days_since_onboarding": 4
})

partner_seq += 1


# ============================================================
# 6. Partner lookup dictionaries
# ============================================================

PARTNER_BY_ID = {
    p["partner_id"]: p
    for p in PARTNERS
}

PARTNERS_BY_CITY = {}

for p in PARTNERS:

    if p["partner_id"] == IDLE_PARTNER_ID:
        continue

    PARTNERS_BY_CITY.setdefault(
        p["city"],
        []
    ).append(
        p["partner_id"]
    )


# ============================================================
# 7. Generate Bookings
# ============================================================

N_BOOKINGS = 600

BOOKINGS = []

STATUS_CHOICES = [
    "Paid",
    "Refunded",
    "Pending"
]

STATUS_WEIGHTS = [
    0.82,
    0.10,
    0.08
]


for booking_seq in range(1, N_BOOKINGS + 1):

    city = random.choice(CITIES)

    partner_id = random.choice(
        PARTNERS_BY_CITY[city]
    )

    partner = PARTNER_BY_ID[partner_id]

    category = partner["primary_category"]

    lo, hi = CATEGORY_PRICE_RANGE[category]

    amount = random.randint(lo, hi)

    day = random.randint(1, 90)

    if day <= 30:
        month = 1
    elif day <= 60:
        month = 2
    else:
        month = 3

    day_in_month = day - (month - 1) * 30

    booking_date = (
        f"2026-{month:02d}-{day_in_month:02d}"
    )

    status = random.choices(
        STATUS_CHOICES,
        weights=STATUS_WEIGHTS,
        k=1
    )[0]

    complaint_flag = (
        1 if random.random() < 0.12 else 0
    )

    sla_breach_flag = (
        1 if random.random() < 0.15 else 0
    )

    # Customer rating is calculated
    # but not stored in the database.

    if status == "Pending":

        customer_rating = None

    else:

        base = (
            4.3
            - (1.4 if complaint_flag else 0)
            - (0.6 if sla_breach_flag else 0)
        )

        customer_rating = max(
            1,
            min(
                5,
                round(
                    base + random.uniform(-0.6, 0.6)
                )
            )
        )

    # Three test bookings
    is_test = (
        1
        if booking_seq in (37, 214, 501)
        else 0
    )

    BOOKINGS.append({
        "booking_id": f"B{booking_seq:04d}",
        "partner_id": partner_id,
        "city": city,
        "category": category,
        "booking_date": booking_date,
        "amount_inr": amount,
        "complaint_flag": complaint_flag,
        "sla_breach_flag": sla_breach_flag,
        "is_test": is_test
    })


# ============================================================
# 8. Create partners_import.csv
#    with deliberate duplicate rows
# ============================================================

DUPLICATED_IDS = [
    "P003",
    "P017",
    "P031"
]

import_rows = list(PARTNERS)

for pid in DUPLICATED_IDS:

    import_rows.append(
        dict(PARTNER_BY_ID[pid])
    )

random.shuffle(import_rows)


# ============================================================
# 9. CSV writing function
# ============================================================

def write_csv(filename, rows, fieldnames):

    file_path = os.path.join(
        OUTDIR,
        filename
    )

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for row in rows:
            writer.writerow(row)


# ============================================================
# 10. Create CSV files
# ============================================================

write_csv(
    "cities.csv",
    [{"city": c} for c in CITIES],
    ["city"]
)

write_csv(
    "categories.csv",
    [{"category": c} for c in ALL_CATEGORIES],
    ["category"]
)

write_csv(
    "partners_import.csv",
    import_rows,
    [
        "partner_id",
        "city",
        "primary_category",
        "rating",
        "active",
        "days_since_onboarding"
    ]
)

write_csv(
    "bookings.csv",
    BOOKINGS,
    [
        "booking_id",
        "partner_id",
        "city",
        "category",
        "booking_date",
        "amount_inr",
        "complaint_flag",
        "sla_breach_flag",
        "is_test"
    ]
)


# ============================================================
# 11. Create SQLite database
# ============================================================

db_path = os.path.join(
    OUTDIR,
    "urban_service.db"
)

# Delete old database if it exists
if os.path.exists(db_path):

    os.remove(db_path)


conn = sqlite3.connect(db_path)

cur = conn.cursor()


# ============================================================
# 12. Categories table
# ============================================================

cur.execute("""
CREATE TABLE categories (
    category TEXT PRIMARY KEY
)
""")

cur.executemany(
    "INSERT INTO categories VALUES (?)",
    [
        (c,)
        for c in ALL_CATEGORIES
    ]
)


# ============================================================
# 13. Partners import table
# ============================================================

cur.execute("""
CREATE TABLE partners_import (
    partner_id TEXT,
    city TEXT,
    primary_category TEXT,
    rating REAL,
    active INTEGER,
    days_since_onboarding INTEGER
)
""")

cur.executemany(
    """
    INSERT INTO partners_import
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    [
        (
            r["partner_id"],
            r["city"],
            r["primary_category"],
            r["rating"],
            1 if r["active"] else 0,
            r["days_since_onboarding"]
        )
        for r in import_rows
    ]
)


# ============================================================
# 14. Bookings table
# ============================================================

cur.execute("""
CREATE TABLE bookings (
    booking_id TEXT PRIMARY KEY,
    partner_id TEXT,
    city TEXT,
    category TEXT,
    booking_date TEXT,
    amount_inr INTEGER,
    complaint_flag INTEGER,
    sla_breach_flag INTEGER,
    is_test INTEGER
)
""")

cur.executemany(
    """
    INSERT INTO bookings
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    [
        (
            r["booking_id"],
            r["partner_id"],
            r["city"],
            r["category"],
            r["booking_date"],
            r["amount_inr"],
            r["complaint_flag"],
            r["sla_breach_flag"],
            r["is_test"]
        )
        for r in BOOKINGS
    ]
)


# ============================================================
# 15. Create clean partners table
#     Remove duplicate partner records
# ============================================================

cur.execute("""
CREATE TABLE partners AS

SELECT DISTINCT
    partner_id,
    city,
    primary_category,
    rating,
    active,
    days_since_onboarding

FROM partners_import
""")


# ============================================================
# 16. Remove test bookings
# ============================================================

cur.execute("""
DELETE FROM bookings
WHERE is_test = 1
""")


# ============================================================
# 17. Add the three required bookings
# ============================================================

extra_bookings = [

    (
        "B9001",
        "P009",
        "Mumbai",
        "Deep Home Cleaning",
        "2026-03-31",
        3200,
        0,
        0,
        0
    ),

    (
        "B9002",
        "P041",
        "Chennai",
        "Plumbing",
        "2026-03-31",
        640,
        0,
        0,
        0
    ),

    (
        "B9003",
        "P035",
        "Hyderabad",
        "Electrical Repair",
        "2026-03-31",
        980,
        0,
        0,
        0
    )
]


cur.executemany(
    """
    INSERT INTO bookings
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    extra_bookings
)


# ============================================================
# 18. Save database
# ============================================================

conn.commit()

conn.close()


# ============================================================
# 19. Final message
# ============================================================

print()
print("==========================================")
print("Urban Service Project Created Successfully")
print("==========================================")
print()
print("Created files:")
print("1. cities.csv")
print("2. categories.csv")
print("3. partners_import.csv")
print("4. bookings.csv")
print("5. urban_service.db")
print()
print("Clean partners table created.")
print("Test bookings removed.")
print("B9001, B9002 and B9003 added.")
print()
print("Done!")