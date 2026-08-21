import sqlite3
from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "crop_disease.db"

DATA_FILE = BASE_DIR / "data" / "diseases.json"


def create_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS diseases (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            crop_bn TEXT NOT NULL,

            crop_en TEXT NOT NULL,

            disease_bn TEXT NOT NULL,

            disease_name_en TEXT NOT NULL,

            scientific_cause TEXT,

            symptoms TEXT,

            favorable_condition TEXT,

            prevention TEXT,

            management TEXT,

            medicine TEXT,

            application TEXT,

            safety TEXT,

            source TEXT,

            source_url TEXT

        )
        """
    )


    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        diseases = json.load(file)


    for disease in diseases:

        cursor.execute(
            """
            INSERT INTO diseases (

                crop_bn,
                crop_en,
                disease_bn,
                disease_name_en,
                scientific_cause,
                symptoms,
                favorable_condition,
                prevention,
                management,
                medicine,
                application,
                safety,
                source,
                source_url

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,

            (

                disease.get("crop_bn", ""),

                disease.get("crop_en", ""),

                disease.get("disease_bn", ""),

                disease.get("disease_en", ""),

                disease.get(
                    "scientific_cause",
                    ""
                ),

                disease.get(
                    "symptoms",
                    ""
                ),

                disease.get(
                    "favorable_condition",
                    ""
                ),

                disease.get(
                    "prevention",
                    ""
                ),

                disease.get(
                    "management",
                    ""
                ),

                disease.get(
                    "medicine",
                    ""
                ),

                disease.get(
                    "application",
                    ""
                ),

                disease.get(
                    "safety",
                    ""
                ),

                disease.get(
                    "source",
                    ""
                ),

                disease.get(
                    "source_url",
                    ""
                )

            )
        )


    conn.commit()

    conn.close()


    print(
        "✅ Disease database তৈরি হয়েছে।"
    )


if __name__ == "__main__":

    create_database()