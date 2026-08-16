import sqlite3
import joblib
import pandas as pd

from pathlib import Path


# =====================================================
# PATHS
# =====================================================

MODEL_DIR = Path(__file__).resolve().parent

MODEL_PATH = MODEL_DIR / "pond_fish_model.pkl"

DATABASE_PATH = MODEL_DIR / "pond.db"

# =====================================================
# FISH NAME MAPPING
# =====================================================

FISH_NAME_MAPPING = {
    "katla": "Catla",
    "rui": "Rohu",
    "silverCup": "Silver Carp",
    "karpio": "Common Carp",
    "tilapia": "Tilapia",
    "pangas": "Pangas",
    "koi": "Koi",
    "magur": "Magur",
    "sing": "Sing",
    "prawn": "Prawn",
    "shrimp": "Shrimp",
}


# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load(MODEL_PATH)


# =====================================================
# DATABASE
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
        survival_rate,
        target_weight,
        culture_period_days,
        data_source
    FROM fish_species
    WHERE LOWER(fish_name) = LOWER(?)
    """,
    (database_fish_name,)
)

    result = cursor.fetchone()

    connection.close()

    return result


# =====================================================
# STOCKING CALCULATION
# =====================================================

def calculate_stocking(
    pond_size,
    density_min,
    density_max,
    density_unit
):

    if density_min is None or density_max is None:
        return None, None

    density_average = (
        density_min + density_max
    ) / 2

    unit = density_unit.lower()

    # ---------------------------------------------
    # Fish per decimal
    # ---------------------------------------------

    if unit == "fish/decimal":

        total_fish = round(
            pond_size * density_average
        )

        return density_average, total_fish

    # ---------------------------------------------
    # Fingerlings per bigha
    # ---------------------------------------------

    elif unit == "fingerlings/bigha":

        pond_bigha = pond_size / 33

        total_fish = round(
            pond_bigha * density_average
        )

        return density_average, total_fish

    # ---------------------------------------------
    # Fish per hectare
    # ---------------------------------------------

    elif unit == "fish/ha" or unit == "fish/ha/year":

        pond_hectare = pond_size / 247.1

        total_fish = round(
            pond_hectare * density_average
        )

        return density_average, total_fish

    return density_average, None


# =====================================================
# USER INPUT
# =====================================================

print()
print("========================================")
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
# ML PREDICTION
# =====================================================

predicted_fish = model.predict(input_data)[0]

probabilities = model.predict_proba(input_data)[0]

confidence = probabilities.max() * 100


# =====================================================
# DATABASE LOOKUP
# =====================================================

fish_info = get_fish_information(
    predicted_fish
)


if fish_info is None:

    print()
    print("Fish prediction found,")
    print("but management data is unavailable.")

    print()
    print("Predicted Fish:", predicted_fish)
    print(
        f"Confidence: {confidence:.2f}%"
    )

    exit()


(
    fish_name,
    density_min,
    density_max,
    density_unit,
    feeding_rate,
    survival_rate,
    target_weight,
    culture_period_days,
    data_source
) = fish_info


# =====================================================
# STOCKING
# =====================================================

stocking_density, total_fish = calculate_stocking(
    pond_size,
    density_min,
    density_max,
    density_unit
)


# =====================================================
# PRODUCTION
# =====================================================

estimated_production = None

if (
    total_fish is not None
    and target_weight is not None
):

    if survival_rate is not None:

        survival_fraction = (
            survival_rate / 100
        )

    else:

        survival_fraction = 1.0

    estimated_production = (
        total_fish
        * target_weight
        * survival_fraction
    )


# =====================================================
# DAILY FEED
# =====================================================

daily_feed = None

if (
    estimated_production is not None
    and feeding_rate is not None
):

    daily_feed = (
        estimated_production
        * feeding_rate
        / 100
    )


# =====================================================
# RESULT
# =====================================================

print()
print("========================================")
print("        PREDICTION RESULT")
print("========================================")

print(
    f"Fish Name: {fish_name}"
)

print(
    f"Confidence: {confidence:.2f}%"
)

print(
    f"Pond Size: {pond_size:.2f} decimal"
)

print(
    f"Pond Depth: {pond_depth:.2f} meter"
)

print(
    f"Temperature: {temperature:.2f} °C"
)

print(
    f"pH: {ph:.2f}"
)

print(
    f"DO: {do:.2f} mg/L"
)

print(
    f"Turbidity: {turbidity:.2f}"
)

print("----------------------------------------")


if stocking_density is not None:

    print(
        "Recommended Stocking Density: "
        f"{stocking_density:.0f} "
        f"{density_unit}"
    )

else:

    print(
        "Recommended Stocking Density: "
        "Data unavailable"
    )


if total_fish is not None:

    print(
        f"Recommended Total Fish: {total_fish}"
    )

else:

    print(
        "Recommended Total Fish: "
        "Data unavailable"
    )


if target_weight is not None:

    print(
        "Expected Harvest Weight: "
        f"{target_weight:.3f} kg/fish"
    )

else:

    print(
        "Expected Harvest Weight: "
        "Data unavailable"
    )


if daily_feed is not None:

    print(
        "Recommended Daily Feed: "
        f"{daily_feed:.2f} kg/day"
    )

else:

    print(
        "Recommended Daily Feed: "
        "Data unavailable"
    )


if culture_period_days is not None:

    print(
        "Estimated Culture Period: "
        f"{culture_period_days} days"
    )

else:

    print(
        "Estimated Culture Period: "
        "Data unavailable"
    )


if estimated_production is not None:

    print(
        "Estimated Production: "
        f"{estimated_production:.2f} kg"
    )

else:

    print(
        "Estimated Production: "
        "Data unavailable"
    )


print("----------------------------------------")

if confidence < 50:

    print(
        "Warning: Low-confidence prediction."
    )

elif confidence < 75:

    print(
        "Notice: Moderate-confidence prediction."
    )

else:

    print(
        "Prediction confidence is high."
    )

print("----------------------------------------")

print("Data Source:")
print(data_source)

print("========================================")