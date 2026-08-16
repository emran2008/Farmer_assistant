from pathlib import Path
import sys


# ============================================================
# DATABASE PATH
# ============================================================

CURRENT_DIR = Path(__file__).resolve().parent
DATABASE_DIR = CURRENT_DIR.parent / "Biofloc Database"

sys.path.insert(0, str(DATABASE_DIR))

from database import get_connection


# ============================================================
# SAVE PREDICTION
# ============================================================

def save_prediction(result):

    conn = get_connection()

    query = """
    INSERT INTO biofloc_predictions (

        fish_name,
        tank_volume,
        fish_count,
        average_weight,

        temperature,
        ph,
        dissolved_oxygen,

        ammonia,
        nitrite,
        alkalinity,

        feed_protein,
        daily_feed,

        carbon_source,
        carbon_amount,

        predicted_final_weight,
        predicted_final_biomass,
        predicted_survival_rate,
        predicted_fcr,

        recommendation

    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    conn.execute(
        query,
        (
            result["fish_name"],

            result["tank_volume_liter"],

            result["fish_count"],

            result["average_weight_g"],

            result.get("temperature"),

            result.get("ph"),

            result.get("dissolved_oxygen"),

            result.get("ammonia"),

            result.get("nitrite"),

            result.get("alkalinity"),

            result["feed_protein_percent"],

            result["estimated_daily_feed_kg"],

            result["carbon_source"],

            result["estimated_carbon_amount_kg"],

            result.get("predicted_final_weight"),

            result.get("predicted_final_biomass"),

            result.get("predicted_survival_rate"),

            result.get("predicted_fcr"),

            result["biofloc_suitability"]
        )
    )

    conn.commit()

    prediction_id = conn.execute(
        "SELECT last_insert_rowid()"
    ).fetchone()[0]

    conn.close()

    return prediction_id


# ============================================================
# GET PREDICTION HISTORY
# ============================================================

def get_prediction_history(limit=50):

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT *
        FROM biofloc_predictions
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (limit,)
    ).fetchall()

    conn.close()

    return rows


# ============================================================
# GET SINGLE PREDICTION
# ============================================================

def get_prediction_by_id(prediction_id):

    conn = get_connection()

    row = conn.execute(
        """
        SELECT *
        FROM biofloc_predictions
        WHERE id = ?
        """,
        (prediction_id,)
    ).fetchone()

    conn.close()

    return row


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    history = get_prediction_history()

    print("\n========================================")
    print("BIOFLOC PREDICTION HISTORY")
    print("========================================")

    if not history:

        print("No prediction history found.")

    else:

        for item in history:

            print(
                f"ID: {item['id']} | "
                f"Fish: {item['fish_name']} | "
                f"Tank: {item['tank_volume']} L | "
                f"Fish Count: {item['fish_count']} | "
                f"Result: {item['recommendation']} | "
                f"Date: {item['created_at']}"
            )

    print("========================================")