from pathlib import Path

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
# PATHS
# ============================================================

CURRENT_DIR = Path(__file__).resolve().parent

DATASET_FILE = (
    CURRENT_DIR
    / "dataset"
    / "biofloc_training_data.csv"
)

MODEL_DIR = CURRENT_DIR / "models"

MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# LOAD DATASET
# ============================================================

print("\n========================================")
print("LOADING BIOFLOC DATASET")
print("========================================")

df = pd.read_csv(DATASET_FILE)

print(f"Dataset rows: {len(df)}")
print(f"Dataset columns: {len(df.columns)}")


# ============================================================
# FEATURES
# ============================================================

FEATURES = [

    "fish_name",

    "tank_volume_m3",

    "fish_count",

    "initial_weight_g",

    "stocking_density_fish_m3",

    "temperature",

    "ph",

    "dissolved_oxygen",

    "ammonia",

    "nitrite",

    "alkalinity",

    "feed_protein_percent",

    "daily_feed_kg",

    "culture_period_days"
]


# ============================================================
# TARGETS
# ============================================================

TARGETS = {

    "final_weight": "final_weight_g",

    "final_biomass": "final_biomass_kg",

    "survival": "survival_rate_percent",

    "fcr": "fcr"
}


# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

required_columns = FEATURES + list(
    TARGETS.values()
)

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:

    raise ValueError(
        "Missing columns in dataset: "
        + ", ".join(missing_columns)
    )


# ============================================================
# REMOVE INVALID ROWS
# ============================================================

df = df.dropna(
    subset=required_columns
).copy()

print(f"Usable rows: {len(df)}")


# ============================================================
# INPUT DATA
# ============================================================

X = df[FEATURES]


# ============================================================
# FEATURE TYPES
# ============================================================

CATEGORICAL_FEATURES = [
    "fish_name"
]

NUMERICAL_FEATURES = [
    column
    for column in FEATURES
    if column not in CATEGORICAL_FEATURES
]


# ============================================================
# PREPROCESSOR
# ============================================================

preprocessor = ColumnTransformer(

    transformers=[

        (
            "categorical",

            OneHotEncoder(
                handle_unknown="ignore"
            ),

            CATEGORICAL_FEATURES
        ),

        (
            "numerical",

            "passthrough",

            NUMERICAL_FEATURES
        )
    ]
)


# ============================================================
# TRAIN ONE MODEL
# ============================================================

def train_model(
    target_name,
    target_column
):

    print("\n----------------------------------------")
    print(f"Training: {target_name}")
    print("----------------------------------------")

    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.20,

        random_state=42
    )

    model = Pipeline(

        steps=[

            (
                "preprocessor",
                preprocessor
            ),

            (
                "model",

                RandomForestRegressor(

                    n_estimators=300,

                    max_depth=None,

                    min_samples_split=2,

                    min_samples_leaf=1,

                    random_state=42,

                    n_jobs=-1
                )
            )
        ]
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = mse ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )

    print(
        f"MAE  : {mae:.4f}"
    )

    print(
        f"RMSE : {rmse:.4f}"
    )

    print(
        f"R²   : {r2:.4f}"
    )

    model_file = (
        MODEL_DIR
        / f"{target_name}_model.pkl"
    )

    joblib.dump(
        model,
        model_file
    )

    print(
        f"Saved: {model_file}"
    )

    return {
        "target": target_name,
        "mae": mae,
        "rmse": rmse,
        "r2": r2
    }


# ============================================================
# TRAIN ALL MODELS
# ============================================================

results = []

for target_name, target_column in TARGETS.items():

    result = train_model(
        target_name,
        target_column
    )

    results.append(
        result
    )


# ============================================================
# SUMMARY
# ============================================================

print("\n========================================")
print("MODEL TRAINING COMPLETE")
print("========================================")

for result in results:

    print(
        f"{result['target']:15} "
        f"MAE={result['mae']:.4f}  "
        f"RMSE={result['rmse']:.4f}  "
        f"R²={result['r2']:.4f}"
    )

print("\nModels saved in:")

print(
    MODEL_DIR
)

print("========================================")