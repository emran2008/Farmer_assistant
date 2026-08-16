import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "Dataset" / "pond_water_fish.csv"


# Load dataset
df = pd.read_csv(DATASET_PATH)


print("\n========== DATASET INFORMATION ==========\n")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())


print("\n========== FIRST 10 ROWS ==========\n")
print(df.head(10))


print("\n========== DATA TYPES ==========\n")
print(df.dtypes)


print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())


print("\n========== DUPLICATE ROWS ==========\n")
print(df.duplicated().sum())


print("\n========== FISH CLASSES ==========\n")

if "Fish" in df.columns:
    print(df["Fish"].value_counts())


print("\n========== NUMERIC SUMMARY ==========\n")
print(df.describe())