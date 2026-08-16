import sqlite3
import joblib
import pandas as pd

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
# GET FISH INFORMATION
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

    # Fish per decimal
    if unit == "fish/decimal":

        total_fish = round(
            pond_size * density_average
        )

        return density_average, total_fish

    # Fingerlings per bigha
    elif unit == "fingerlings/bigha":

        pond_bigha = pond_size / 33

        total_fish = round(
            pond_bigha * density_average
        )

        return density_average, total_fish

    # Fish per hectare
    elif (
        unit == "fish/ha"
        or unit == "fish/ha/year"
    ):

        pond_hectare = pond_size / 247.1

        total_fish = round(
            pond_hectare * density_average
        )

        return density_average, total_fish

    return density_average, None


# =====================================================
# MAIN PREDICTION FUNCTION
# =====================================================

def predict_fish(
    pond_size,
    pond_depth,
    temperature,
    ph,
    do,
    turbidity
):

    # -------------------------------------------------
    # ML INPUT
    # -------------------------------------------------

    input_data = pd.DataFrame(
        [
            {
                "ph": ph,
                "temperature": temperature,
                "turbidity": turbidity
            }
        ]
    )

    # -------------------------------------------------
    # ML PREDICTION
    # -------------------------------------------------

    predicted_fish = model.predict(
        input_data
    )[0]

    probabilities = model.predict_proba(
        input_data
    )[0]

    confidence = (
        probabilities.max() * 100
    )

    # -------------------------------------------------
    # DATABASE LOOKUP
    # -------------------------------------------------

    fish_info = get_fish_information(
        predicted_fish
    )

    if fish_info is None:

        return {
            "success": False,
            "message": (
                "Fish prediction found, "
                "but management data is unavailable."
            ),
            "predicted_fish": predicted_fish,
            "confidence": confidence
        }

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

    # -------------------------------------------------
    # STOCKING
    # -------------------------------------------------

    stocking_density, total_fish = calculate_stocking(
        pond_size,
        density_min,
        density_max,
        density_unit
    )

    # -------------------------------------------------
    # PRODUCTION
    # -------------------------------------------------

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

    # -------------------------------------------------
    # DAILY FEED
    # -------------------------------------------------

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

    # -------------------------------------------------
    # SAVE HISTORY
    # -------------------------------------------------

    save_prediction(
        pond_size=pond_size,
        pond_depth=pond_depth,
        temperature=temperature,
        ph=ph,
        do=do,
        predicted_fish=fish_name,
        stocking_density=stocking_density,
        total_fish=total_fish,
        daily_feed=daily_feed,
        expected_growth=target_weight,
        culture_period_days=culture_period_days,
        estimated_production=estimated_production
    )

    # -------------------------------------------------
    # RETURN RESULT
    # -------------------------------------------------

    return {
        "success": True,

        "fish_name": fish_name,

        "predicted_fish": predicted_fish,

        "confidence": confidence,

        "pond_size": pond_size,

        "pond_depth": pond_depth,

        "temperature": temperature,

        "ph": ph,

        "do": do,

        "turbidity": turbidity,

        "stocking_density": stocking_density,

        "density_unit": density_unit,

        "total_fish": total_fish,

        "feeding_rate": feeding_rate,

        "daily_feed": daily_feed,

        "expected_growth": target_weight,

        "culture_period_days": culture_period_days,

        "estimated_production":
            estimated_production,

        "data_source": data_source
    }


# =====================================================
# SAVE PREDICTION
# =====================================================

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

    connection = sqlite3.connect(
        DATABASE_PATH
    )

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