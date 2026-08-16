import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "pond.db"


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


columns = [
    ("feeding_rate", "REAL"),
    ("expected_growth", "REAL"),
    ("culture_period_days", "INTEGER")
]


for column_name, column_type in columns:

    try:

        cursor.execute(
            f"""
            ALTER TABLE fish_species
            ADD COLUMN {column_name} {column_type}
            """
        )

        print(f"Added column: {column_name}")

    except sqlite3.OperationalError as error:

        if "duplicate column name" in str(error).lower():

            print(f"Column already exists: {column_name}")

        else:

            raise


connection.commit()
connection.close()


print()
print("========================================")
print("Database update completed successfully.")
print("========================================")