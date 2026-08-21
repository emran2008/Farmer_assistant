import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "crop_disease.db"


def get_connection():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn


def get_disease(disease_name):

    conn = get_connection()

    disease = conn.execute(
        """
        SELECT *
        FROM diseases
        WHERE disease_name_en = ?
        LIMIT 1
        """,
        (disease_name,)
    ).fetchone()

    conn.close()

    return disease