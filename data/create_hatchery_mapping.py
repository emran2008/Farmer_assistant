import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HATCHERY_CSV = r"D:\crop recommendation\data\bangladesh_fish_hatcheries_current.csv"

OUTPUT_CSV = r"D:\crop recommendation\data\fish_hatchery_species_mapping.csv"


# Current hatchery/farm data load
df = pd.read_csv(HATCHERY_CSV)


# Mapping table তৈরি
mapping = pd.DataFrame({
    "mapping_id": range(1, len(df) + 1),
    "farm_id": df["farm_id"],
    "farm_name": df["farm_name"],
    "division": df["division"],
    "district": df["district"],
    "upazila": df["upazila"],

    # এখনো source থেকে species নিশ্চিত না
    "fish_species": "",

    # এখনো source থেকে service নিশ্চিত না
    "service_type": "",

    "source": "Department of Fisheries Bangladesh - Farm List",
    "source_year": 2026,
    "verification_status": "Species not yet verified"
})


mapping.to_csv(
    OUTPUT_CSV,
    index=False,
    encoding="utf-8-sig"
)

print("Mapping CSV created successfully!")
print("Total hatchery/farm records:", len(mapping))
print("File:", OUTPUT_CSV)