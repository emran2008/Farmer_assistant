import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DATABASE_PATH = BASE_DIR / "pond.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)
def get_fish_information(fish_name):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            fish_name,
            stocking_density_min,
            stocking_density_max,
            stocking_density_unit,
            feeding_rate,
            expected_growth,
            culture_period_days
        FROM fish_species
        WHERE LOWER(fish_name) = LOWER(?)
        """,
        (fish_name,)
    )

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return None

    fish_name = result[0]
    density_min = result[1]
    density_max = result[2]
    density_unit = result[3]
    feeding_rate = result[4]
    expected_growth = result[5]
    culture_period_days = result[6]

    return (
        fish_name,
        density_min,
        density_max,
        density_unit,
        feeding_rate,
        expected_growth,
        culture_period_days
    )
    fish_name = result[0]
    density_min = result[1]
    density_max = result[2]
    density_unit = result[3]

    # এগুলো পরের ধাপে database থেকে নেব
    feeding_rate = None
    expected_growth = None
    culture_period_days = None

    return (
        fish_name,
        density_min,
        density_max,
        density_unit,
        feeding_rate,
        expected_growth,
        culture_period_days
    )

def create_database():

    connection = get_connection()

    cursor = connection.cursor()

    schema_file = BASE_DIR / "schema.sql"

    with open(schema_file, "r", encoding="utf-8") as file:
        schema = file.read()

    cursor.executescript(schema)

    connection.commit()
    connection.close()

    print("Pond database created successfully.")


if __name__ == "__main__":
    create_database()