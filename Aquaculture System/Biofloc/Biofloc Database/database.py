import sqlite3
from pathlib import Path


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "biofloc.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def initialize_database():

    schema_path = BASE_DIR / "schema.sql"

    conn = get_connection()

    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()

    conn.executescript(schema)
    conn.commit()
    conn.close()


# ============================================================
# GET ALL FISH SPECIES
# ============================================================

def get_all_fish():

    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM fish_species
        ORDER BY fish_name
    """).fetchall()

    conn.close()

    return rows


# ============================================================
# GET SINGLE FISH
# ============================================================

def get_fish_by_name(fish_name):

    conn = get_connection()

    row = conn.execute("""
        SELECT *
        FROM fish_species
        WHERE LOWER(fish_name) = LOWER(?)
    """, (fish_name,)).fetchone()

    conn.close()

    return row


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    initialize_database()

    fish_list = get_all_fish()

    print("\n========================================")
    print("BIOFLOC FISH SPECIES")
    print("========================================")

    for fish in fish_list:
        print(
            f"{fish['id']}. "
            f"{fish['fish_name']}"
        )

    print("\n========================================")
    print(f"Total species: {len(fish_list)}")
    print("========================================")