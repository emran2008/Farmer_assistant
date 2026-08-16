import sqlite3
import joblib
import pandas as pd
from database import get_fish_information

from pathlib import Path


# =====================================================
# PATHS
# =====================================================

MODEL_DIR = Path(__file__).resolve().parent

MODEL_PATH = MODEL_DIR / "pond_fish_model.pkl"

DATABASE_PATH = (
    MODEL_DIR.parent
    / "Pond Database"
    / "pond.db"
)


# =====================================================
# LOAD ML MODEL
# =====================================================

model = joblib.load(MODEL_PATH)

FISH_NAME_MAPPING = {
    "katla": "Catla",
    "rui": "Rohu",
    "silverCup": "Silver Carp",
    "karpio": "Common Carp",
}
# =====================================================
# DATABASE FUNCTION
# =====================================================

def get_fish_information(fish_name):

    database_fish_name = FISH_NAME_MAPPING.get(
        fish_name,
        fish_name
    )

    connection = sqlite3.connect(DATABASE_PATH)

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
        (database_fish_name,)
    )

    result = cursor.fetchone()

    connection.close()

    return result


# =====================================================
# USER INPUT
# =====================================================

print("\n========================================")
print("        POND FISH PREDICTION")
print("========================================")

pond_size = float(
    input("Pond Size (decimal): ")
)

pond_depth = float(
    input("Pond Depth (meter): ")
)

temperature = float(
    input("Temperature (°C): ")
)

ph = float(
    input("pH: ")
)

do = float(
    input("Dissolved Oxygen - DO (mg/L): ")
)

turbidity = float(
    input("Turbidity: ")
)


# =====================================================
# ML INPUT
# =====================================================

input_data = pd.DataFrame(
    [
        {
            "ph": ph,
            "temperature": temperature,
            "turbidity": turbidity
        }
    ]
)


# =====================================================
# FISH PREDICTION
# =====================================================

predicted_fish = model.predict(input_data)[0]

probabilities = model.predict_proba(input_data)[0]

confidence = probabilities.max() * 100


# =====================================================
# DATABASE LOOKUP
# =====================================================

fish_info = get_fish_information(predicted_fish)


if fish_info is None:

    print("\nFish was predicted by ML,")
    print("but this fish is not available in database.")

    print("\nPredicted Fish:", predicted_fish)
    print(f"Confidence: {confidence:.2f}%")

    exit()


(
    fish_name,
    density_min,
    density_max,
    density_unit,
    feeding_rate,
    expected_growth,
    culture_period_days
) = fish_info


# =====================================================
# STOCKING DENSITY
# =====================================================

stocking_density = (
    density_min + density_max
) / 2


# =====================================================
# TOTAL FISH
# =====================================================

if density_unit.lower() == "fish/decimal":

    total_fish = round(
        pond_size * stocking_density
    )

elif density_unit.lower() == "fingerlings/bigha":

    # 1 bigha = 33 decimal
    pond_bigha = pond_size / 33

    total_fish = round(
        pond_bigha * stocking_density
    )

else:

    total_fish = 0


# =====================================================
# ESTIMATED BIOMASS
# =====================================================

if expected_growth is not None:

    biomass_kg = (
        total_fish * expected_growth
    ) / 1000

else:

    biomass_kg = 0


# =====================================================
# DAILY FEED
# =====================================================

if feeding_rate is not None:

    daily_feed_kg = (
        biomass_kg * feeding_rate
    ) / 100

else:

    daily_feed_kg = 0


# =====================================================
# ESTIMATED PRODUCTION
# =====================================================

estimated_production = biomass_kg


# =====================================================
# RESULT
# =====================================================

print("\n")
print("========================================")
print("        PREDICTION RESULT")
print("========================================")

print(f"Fish Name: {fish_name}")

print(
    f"Confidence: {confidence:.2f}%"
)

print(
    f"Recommended Stocking Density: "
    f"{stocking_density:.0f} {density_unit}"
)

print(
    f"Recommended Total Fish: "
    f"{total_fish}"
)

print(
    f"Expected Growth: "
    f"{expected_growth if expected_growth else 'N/A'} kg/fish"
)

print(
    f"Recommended Daily Feed: "
    f"{daily_feed_kg:.2f} kg/day"
)

print(
    f"Estimated Culture Period: "
    f"{culture_period_days} days"
)

print(
    f"Estimated Production: "
    f"{estimated_production:.2f} kg"
)

print("========================================")

def save_prediction(
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
    estimated_production
):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO pond_predictions
        (
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
            estimated_production
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
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
            estimated_production
        )
    )

    connection.commit()

    connection.close()

    print("\nPrediction saved to database successfully.")
    print("========================================")
    # =====================================================
# =====================================================
# SAVE PREDICTION HISTORY
# =====================================================

save_prediction(
    pond_size=pond_size,
    pond_depth=pond_depth,
    temperature=temperature,
    ph=ph,
    do=do,
    predicted_fish=fish_name,
    stocking_density=stocking_density,
    total_fish=total_fish,
    daily_feed=daily_feed_kg,
    expected_growth=None,
    culture_period_days=culture_period_days,
    estimated_production=estimated_production
)