import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "pond.db"


fish_data = [
        {
        "fish_name": "Catla",

        "min_temperature": 25,
        "max_temperature": 30,

        "min_ph": 6.5,
        "max_ph": 8.5,

        "min_do": 4,

        "stocking_density_min": 5000,
        "stocking_density_max": 10000,
        "stocking_density_unit": "fish/ha",

        "feeding_rate": 3.0,
        "expected_growth": 1.0,
        "culture_period_days": 180,

        "data_source": "FAO Rohu culture and feeding guidance"
    },

    {
        "fish_name": "Mrigal",

        "min_temperature": 25,
        "max_temperature": 30,

        "min_ph": 6.5,
        "max_ph": 8.5,

        "min_do": 4,

        "stocking_density_min": 5000,
        "stocking_density_max": 10000,
        "stocking_density_unit": "fish/ha",

        "feeding_rate": 3.0,
        "expected_growth": 1.0,
        "culture_period_days": 180,

        "data_source": "FAO carp culture guidance"
    },

    {
        "fish_name": "Silver Carp",

        "min_temperature": 24,
        "max_temperature": 30,

        "min_ph": 6.5,
        "max_ph": 8.5,

        "min_do": 4,

        "stocking_density_min": 700,
        "stocking_density_max": 900,
        "stocking_density_unit": "fingerlings/bigha",

        "feeding_rate": 2.0,
        "expected_growth": 1.0,
        "culture_period_days": 180,

        "data_source": "FAO Bangladesh polyculture guideline"
    },

    {
        "fish_name": "Grass Carp",

        "min_temperature": 24,
        "max_temperature": 30,

        "min_ph": 6.5,
        "max_ph": 8.5,

        "min_do": 4,

        "stocking_density_min": 700,
        "stocking_density_max": 900,
        "stocking_density_unit": "fingerlings/bigha",

        "feeding_rate": 3.0,
        "expected_growth": 1.0,
        "culture_period_days": 180,

        "data_source": "FAO Bangladesh polyculture guideline"
    },

    {
        "fish_name": "Common Carp",

        "min_temperature": 20,
        "max_temperature": 30,

        "min_ph": 6.5,
        "max_ph": 8.5,

        "min_do": 4,

        "stocking_density_min": 5000,
        "stocking_density_max": 10000,
        "stocking_density_unit": "fish/ha",

        "feeding_rate": 3.0,
        "expected_growth": 1.0,
        "culture_period_days": 180,

        "data_source": "FAO carp culture guidance"
    },

    {
        "fish_name": "Tilapia",

        "min_temperature": 24,
        "max_temperature": 30,

        "min_ph": 6.5,
        "max_ph": 8.5,

        "min_do": 4,

        "stocking_density_min": 200,
        "stocking_density_max": 230,
        "stocking_density_unit": "fish/decimal",

        "feeding_rate": 3.0,
        "expected_growth": 0.60,
        "culture_period_days": 240,
        "target_weight": 0.60057,

        "data_source": "2026 Bangladesh semi-intensive non-aerated pond study"
    },

    {
        "fish_name": "Pangas",

        "min_temperature": 25,
        "max_temperature": 30,

        "min_ph": 6.5,
        "max_ph": 8.5,

        "min_do": 4,

        "stocking_density_min": 8000,
        "stocking_density_max": 12000,
        "stocking_density_unit": "fish/ha",

        "feeding_rate": 3.0,
        "expected_growth": 1.0,
        "culture_period_days": 365,

        "data_source": "FAO Bangladesh Pangus pond culture guidance"
    },
    {
        "fish_name": "koi",

        "min_temperature": 20,
        "max_temperature": 30,

        "min_ph": 6.5,
        "max_ph": 8.5,

        "min_do": 4,

        "stocking_density_min": 500,
        "stocking_density_max": 1000,
        "stocking_density_unit": "fish/decimal",

        "feeding_rate": 3.0,
        "expected_growth": 0.8,
        "culture_period_days": 180,
        "data_source": "FAO Bangladesh Pangus pond culture guidance"
    },
    {
        "fish_name": "Prawn",

        "min_temperature": 25,
        "max_temperature": 30,

        "min_ph": 6.5,
        "max_ph": 8.5,

        "min_do": 4,

        "stocking_density_min": 500,
        "stocking_density_max": 1000,
        "stocking_density_unit": "fish/decimal",

        "feeding_rate": 3.0,
        "expected_growth": 0.08,
        "culture_period_days": 180,

        "target_weight": 0.08,

        "data_source": "Pond culture reference data"
    },
]


def insert_fish_data():

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    for fish in fish_data:
        cursor.execute(
            """
            INSERT OR REPLACE INTO fish_species
            (
                fish_name,
                stocking_density_min,
                stocking_density_max,
                stocking_density_unit,
                feeding_rate,
                expected_growth,
                culture_period_days,
                target_weight,
                data_source
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                fish["fish_name"],
                fish["stocking_density_min"],
                fish["stocking_density_max"],
                fish["stocking_density_unit"],
                fish["feeding_rate"],
                fish.get("expected_growth"),
                fish["culture_period_days"],
                fish.get("target_weight"),
                fish.get("data_source"),
            ),
        )

    connection.commit()
    connection.close()

    print("Fish management data inserted successfully.")


if __name__ == "__main__":
    insert_fish_data()