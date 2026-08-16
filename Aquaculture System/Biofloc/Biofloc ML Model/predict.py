from pathlib import Path

import joblib
import pandas as pd


# ============================================================
# PATH
# ============================================================

CURRENT_DIR = Path(__file__).resolve().parent

MODEL_DIR = CURRENT_DIR / "models"


# ============================================================
# MODEL FILES
# ============================================================

MODEL_FILES = {

    "final_weight":
        MODEL_DIR / "final_weight_model.pkl",

    "final_biomass":
        MODEL_DIR / "final_biomass_model.pkl",

    "survival":
        MODEL_DIR / "survival_model.pkl",

    "fcr":
        MODEL_DIR / "fcr_model.pkl"
}


# ============================================================
# LOAD MODELS
# ============================================================

def load_models():

    models = {}

    for name, path in MODEL_FILES.items():

        if not path.exists():

            raise FileNotFoundError(
                f"Model file not found: {path}"
            )

        models[name] = joblib.load(path)

    return models


# ============================================================
# ML PREDICTION
# ============================================================

def predict_biofloc(input_data):

    models = load_models()

    # --------------------------------------------------------
    # Convert input to DataFrame
    # --------------------------------------------------------

    data = pd.DataFrame(
        [input_data]
    )

    # --------------------------------------------------------
    # Predictions
    # --------------------------------------------------------

    final_weight = models[
        "final_weight"
    ].predict(data)[0]

    final_biomass = models[
        "final_biomass"
    ].predict(data)[0]

    survival = models[
        "survival"
    ].predict(data)[0]

    fcr = models[
        "fcr"
    ].predict(data)[0]

    # --------------------------------------------------------
    # Keep values within reasonable ranges
    # --------------------------------------------------------

    survival = max(
        0,
        min(100, survival)
    )

    fcr = max(
        0,
        fcr
    )

    final_weight = max(
        0,
        final_weight
    )

    final_biomass = max(
        0,
        final_biomass
    )

    # --------------------------------------------------------
    # Result
    # --------------------------------------------------------

    return {

        "predicted_final_weight_g":
            round(final_weight, 2),

        "predicted_final_biomass_kg":
            round(final_biomass, 2),

        "predicted_survival_rate_percent":
            round(survival, 2),

        "predicted_fcr":
            round(fcr, 2)
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    test_input = {

        "fish_name": "Tilapia",

        "tank_volume_m3": 10,

        "fish_count": 2000,

        "initial_weight_g": 20,

        "stocking_density_fish_m3": 200,

        "temperature": 28,

        "ph": 7.5,

        "dissolved_oxygen": 5.5,

        "ammonia": 0.3,

        "nitrite": 0.2,

        "alkalinity": 120,

        "feed_protein_percent": 30,

        "daily_feed_kg": 0.8,

        "culture_period_days": 120
    }

    print("\n========================================")
    print("BIOFLOC ML PREDICTION")
    print("========================================")

    result = predict_biofloc(
        test_input
    )

    for key, value in result.items():

        print(
            f"{key}: {value}"
        )

    print("========================================")