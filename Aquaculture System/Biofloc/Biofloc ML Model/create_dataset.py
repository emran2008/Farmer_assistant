from pathlib import Path
import csv
import random


# ============================================================
# PATH
# ============================================================

CURRENT_DIR = Path(__file__).resolve().parent

DATASET_DIR = CURRENT_DIR / "dataset"

DATASET_DIR.mkdir(
    parents=True,
    exist_ok=True
)

DATASET_FILE = DATASET_DIR / "biofloc_training_data.csv"


# ============================================================
# FISH BASE PROFILES
# ============================================================

FISH_PROFILES = {

    "Tilapia": {
        "growth_rate": 0.85,
        "survival_base": 94,
        "fcr_base": 1.35
    },

    "Pangasius": {
        "growth_rate": 0.80,
        "survival_base": 93,
        "fcr_base": 1.45
    },

    "Koi": {
        "growth_rate": 0.70,
        "survival_base": 92,
        "fcr_base": 1.50
    },

    "Magur": {
        "growth_rate": 0.65,
        "survival_base": 91,
        "fcr_base": 1.55
    },

    "Shing": {
        "growth_rate": 0.65,
        "survival_base": 91,
        "fcr_base": 1.55
    },

    "Pabda": {
        "growth_rate": 0.60,
        "survival_base": 90,
        "fcr_base": 1.60
    },

    "Rohu": {
        "growth_rate": 0.55,
        "survival_base": 92,
        "fcr_base": 1.65
    },

    "Mrigal": {
        "growth_rate": 0.55,
        "survival_base": 91,
        "fcr_base": 1.65
    },

    "Catla": {
        "growth_rate": 0.55,
        "survival_base": 90,
        "fcr_base": 1.70
    },

    "Silver Carp": {
        "growth_rate": 0.55,
        "survival_base": 90,
        "fcr_base": 1.70
    },

    "Common Carp": {
        "growth_rate": 0.60,
        "survival_base": 91,
        "fcr_base": 1.60
    },

    "Gulsha": {
        "growth_rate": 0.60,
        "survival_base": 90,
        "fcr_base": 1.60
    },

    "Thai Koi": {
        "growth_rate": 0.70,
        "survival_base": 92,
        "fcr_base": 1.50
    }
}


# ============================================================
# RANDOM VALUE HELPERS
# ============================================================

def random_float(low, high, digits=2):

    return round(
        random.uniform(low, high),
        digits
    )


# ============================================================
# GENERATE ONE RECORD
# ============================================================

def generate_record():

    fish_name = random.choice(
        list(FISH_PROFILES.keys())
    )

    profile = FISH_PROFILES[fish_name]

    # --------------------------------------------------------
    # Farm inputs
    # --------------------------------------------------------

    tank_volume = random_float(
        5,
        100,
        1
    )

    fish_count = random.randint(
        300,
        10000
    )

    initial_weight = random_float(
        5,
        80,
        1
    )

    culture_days = random.randint(
        90,
        240
    )

    temperature = random_float(
        24,
        32,
        1
    )

    ph = random_float(
        6.5,
        8.5,
        2
    )

    dissolved_oxygen = random_float(
        3.5,
        7.5,
        2
    )

    ammonia = random_float(
        0.05,
        1.2,
        2
    )

    nitrite = random_float(
        0.02,
        1.0,
        2
    )

    alkalinity = random_float(
        70,
        180,
        1
    )

    feed_protein = random_float(
        25,
        35,
        1
    )

    feeding_rate = random_float(
        1.5,
        3.0,
        2
    )

    # --------------------------------------------------------
    # Initial biomass
    # --------------------------------------------------------

    initial_biomass = (
        fish_count *
        initial_weight
    ) / 1000

    # --------------------------------------------------------
    # Density
    # --------------------------------------------------------

    stocking_density = (
        fish_count /
        tank_volume
    )

    # --------------------------------------------------------
    # Daily feed
    # --------------------------------------------------------

    daily_feed = (
        initial_biomass *
        feeding_rate /
        100
    )

    # --------------------------------------------------------
    # Environmental score
    # --------------------------------------------------------

    water_score = 1.0

    if dissolved_oxygen < 4:
        water_score -= 0.08

    if ammonia > 0.5:
        water_score -= 0.08

    if ammonia > 1.0:
        water_score -= 0.10

    if nitrite > 0.5:
        water_score -= 0.08

    if ph < 6.8 or ph > 8.2:
        water_score -= 0.05

    if temperature < 24 or temperature > 32:
        water_score -= 0.05

    if stocking_density > 150:
        water_score -= 0.08

    water_score = max(
        0.60,
        water_score
    )

    # --------------------------------------------------------
    # Growth estimation
    # --------------------------------------------------------

    growth_factor = (
        profile["growth_rate"] *
        (culture_days / 120)
    )

    growth_factor *= water_score

    final_weight = (
        initial_weight *
        (1 + growth_factor)
    )

    # Add small natural variation
    final_weight *= random_float(
        0.95,
        1.05,
        3
    )

    final_weight = max(
        initial_weight,
        final_weight
    )

    # --------------------------------------------------------
    # Survival
    # --------------------------------------------------------

    survival_rate = (
        profile["survival_base"] *
        water_score
    )

    survival_rate += random_float(
        -2,
        2,
        2
    )

    survival_rate = max(
        60,
        min(99, survival_rate)
    )

    # --------------------------------------------------------
    # Final biomass
    # --------------------------------------------------------

    surviving_fish = (
        fish_count *
        survival_rate /
        100
    )

    final_biomass = (
        surviving_fish *
        final_weight
    ) / 1000

    # --------------------------------------------------------
    # FCR
    # --------------------------------------------------------

    fcr = (
        profile["fcr_base"] +
        random_float(-0.15, 0.15, 3)
    )

    if water_score < 0.85:
        fcr += 0.15

    fcr = max(
        1.0,
        fcr
    )

    # --------------------------------------------------------
    # Return record
    # --------------------------------------------------------

    return {

        "fish_name": fish_name,

        "tank_volume_m3":
            tank_volume,

        "fish_count":
            fish_count,

        "initial_weight_g":
            initial_weight,

        "stocking_density_fish_m3":
            round(stocking_density, 2),

        "temperature":
            temperature,

        "ph":
            ph,

        "dissolved_oxygen":
            dissolved_oxygen,

        "ammonia":
            ammonia,

        "nitrite":
            nitrite,

        "alkalinity":
            alkalinity,

        "feed_protein_percent":
            feed_protein,

        "daily_feed_kg":
            round(daily_feed, 3),

        "culture_period_days":
            culture_days,

        "final_weight_g":
            round(final_weight, 2),

        "final_biomass_kg":
            round(final_biomass, 2),

        "survival_rate_percent":
            round(survival_rate, 2),

        "fcr":
            round(fcr, 2)
    }


# ============================================================
# CREATE DATASET
# ============================================================

def create_dataset(number_of_records=5000):

    fieldnames = [

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

        "culture_period_days",

        "final_weight_g",

        "final_biomass_kg",

        "survival_rate_percent",

        "fcr"
    ]

    with open(
        DATASET_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for _ in range(number_of_records):

            record = generate_record()

            writer.writerow(record)

    print("\n========================================")
    print("BIOFLOC DATASET CREATED")
    print("========================================")
    print(f"File: {DATASET_FILE}")
    print(f"Records: {number_of_records}")
    print("========================================")


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    create_dataset(5000)