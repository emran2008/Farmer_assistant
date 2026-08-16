import sqlite3
from pathlib import Path


# =====================================================
# DATABASE PATH
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATABASE_PATH = BASE_DIR / "pond.db"


# =====================================================
# CONNECT DATABASE
# =====================================================

connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


# =====================================================
# GET PREDICTION HISTORY
# =====================================================

cursor.execute(
    """
    SELECT
        id,
        pond_size,
        pond_depth,
        temperature,
        ph,
        do,
        predicted_fish,
        stocking_density,
        total_fish,
        daily_feed,
        expected_growth,
        culture_period_days,
        estimated_production,
        created_at
    FROM pond_predictions
    ORDER BY id DESC
    """
)

rows = cursor.fetchall()


# =====================================================
# CLOSE DATABASE
# =====================================================

connection.close()


# =====================================================
# DISPLAY HISTORY
# =====================================================

print()
print("========================================")
print("        PREDICTION HISTORY")
print("========================================")


if not rows:

    print()
    print("No prediction history found.")

else:

    for row in rows:

        (
            prediction_id,
            pond_size,
            pond_depth,
            temperature,
            ph,
            do,
            fish,
            density,
            total_fish,
            daily_feed,
            growth,
            culture_days,
            production,
            created_at
        ) = row

        print()
        print("----------------------------------------")

        print(
            f"Prediction ID: {prediction_id}"
        )

        print(
            f"Date: {created_at}"
        )

        print(
            f"Pond Size: {pond_size} decimal"
        )

        print(
            f"Pond Depth: {pond_depth} meter"
        )

        print(
            f"Temperature: {temperature} °C"
        )

        print(
            f"pH: {ph}"
        )

        print(
            f"DO: {do} mg/L"
        )

        print(
            f"Predicted Fish: {fish}"
        )

        print(
            f"Stocking Density: {density}"
        )

        print(
            f"Total Fish: {total_fish}"
        )

        print(
            f"Daily Feed: {daily_feed}"
        )

        print(
            f"Expected Growth: {growth}"
        )

        print(
            f"Culture Period: {culture_days} days"
        )

        print(
            f"Estimated Production: {production} kg"
        )

        print("----------------------------------------")


print()
print("========================================")
print("        END OF HISTORY")
print("========================================")