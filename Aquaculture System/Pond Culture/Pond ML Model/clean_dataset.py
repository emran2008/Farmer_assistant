import pandas as pd
from pathlib import Path


# -----------------------------------------
# Paths
# -----------------------------------------

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "Dataset" / "pond_water_fish.csv"
OUTPUT_FILE = BASE_DIR / "Dataset" / "cleaned_pond_dataset.csv"


# -----------------------------------------
# Load dataset
# -----------------------------------------

df = pd.read_csv(INPUT_FILE)

print("Original dataset shape:")
print(df.shape)


# -----------------------------------------
# Standardize column names
# -----------------------------------------

df.columns = [column.strip().lower() for column in df.columns]

print("\nColumns:")
print(df.columns.tolist())


# -----------------------------------------
# Remove unnecessary spaces from text
# -----------------------------------------

if "fish" in df.columns:
    df["fish"] = df["fish"].astype(str).str.strip()




# -----------------------------------------
# Remove rows with missing values
# -----------------------------------------

before_missing = len(df)

df = df.dropna()

after_missing = len(df)

print("\nRows removed because of missing values:")
print(before_missing - after_missing)


# -----------------------------------------
# Keep only required columns
# -----------------------------------------

required_columns = [
    "ph",
    "temperature",
    "turbidity",
    "fish"
]

df = df[required_columns]


# -----------------------------------------
# Save cleaned dataset
# -----------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# -----------------------------------------
# Final information
# -----------------------------------------

print("\n========== CLEANING COMPLETE ==========")

print("Final rows:", len(df))
print("Final columns:", len(df.columns))

print("\nFish classes:")
print(df["fish"].value_counts())

print("\nSaved to:")
print(OUTPUT_FILE)