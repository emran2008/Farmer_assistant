import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "pond.db"


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""
    SELECT
        fish_name,
        stocking_density_min,
        stocking_density_max,
        stocking_density_unit,
        feeding_rate,
        culture_period_days
    FROM fish_species
""")

rows = cursor.fetchall()

print("\nFish Management Data")
print("-" * 80)

for row in rows:
    print(
        f"Fish: {row[0]} | "
        f"Density: {row[1]} - {row[2]} {row[3]} | "
        f"Feed: {row[4]}% | "
        f"Culture: {row[5]} days"
    )

connection.close()