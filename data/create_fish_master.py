import pandas as pd
import os

BASE_DIR = r"D:\crop recommendation"

INPUT_CSV = os.path.join(
    BASE_DIR,
    "data",
    "bangladesh_fishery_final_master.csv"
)

OUTPUT_CSV = os.path.join(
    BASE_DIR,
    "data",
    "fish_master.csv"
)

# Load master fish data
df = pd.read_csv(INPUT_CSV)

print("Original columns:")
print(df.columns.tolist())

print("\nTotal records:", len(df))


# যেসব column আমাদের দরকার
required_columns = [
    "fish_name_bn",
    "fish_name_en"
]

# Column check
missing = [
    col for col in required_columns
    if col not in df.columns
]

if missing:
    print("\nMissing columns:", missing)
    print("CSV-এর actual column names দেখে তারপর mapping করতে হবে.")
    exit()


# Duplicate বাদ
fish_master = df[
    required_columns
].drop_duplicates()


# Empty fish name বাদ
fish_master = fish_master[
    fish_master["fish_name_bn"].notna()
]

# ID তৈরি
fish_master.insert(
    0,
    "fish_id",
    range(1, len(fish_master) + 1)
)


# Save
fish_master.to_csv(
    OUTPUT_CSV,
    index=False,
    encoding="utf-8-sig"
)

print("\nFish master created successfully!")
print("Total unique fish:", len(fish_master))
print("Saved to:", OUTPUT_CSV)