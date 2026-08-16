from pathlib import Path
import sys


# ============================================================
# DATABASE PATH
# ============================================================

CURRENT_DIR = Path(__file__).resolve().parent

DATABASE_DIR = CURRENT_DIR.parent / "Biofloc Database"

sys.path.insert(0, str(DATABASE_DIR))

from database import get_fish_by_name


# ============================================================
# HISTORY PATH
# ============================================================

HISTORY_DIR = CURRENT_DIR.parent / "Biofloc Prediction History"

sys.path.insert(0, str(HISTORY_DIR))

from history import save_prediction

# ============================================================
# ML MODEL PATH
# ============================================================

ML_DIR = CURRENT_DIR.parent / "Biofloc ML Model"

sys.path.insert(0, str(ML_DIR))

from predict import predict_biofloc

# ============================================================
# BIOMASS CALCULATION
# ============================================================

def calculate_biomass(fish_count, average_weight_g):
    """
    Biomass = number of fish × average weight

    Returns:
        biomass_kg
    """

    biomass_kg = (fish_count * average_weight_g) / 1000

    return round(biomass_kg, 2)


# ============================================================
# STOCKING DENSITY
# ============================================================

def calculate_stocking_density(fish_count, tank_volume_liter):
    """
    Convert tank volume from liter to cubic meter.

    1 m³ = 1000 L
    """

    if tank_volume_liter <= 0:
        return 0

    tank_volume_m3 = tank_volume_liter / 1000

    density = fish_count / tank_volume_m3

    return round(density, 2)


# ============================================================
# FEED REQUIREMENT
# ============================================================

def calculate_daily_feed(biomass_kg, feeding_rate_percent):
    """
    Daily feed = biomass × feeding rate %
    """

    daily_feed_kg = biomass_kg * (feeding_rate_percent / 100)

    return round(daily_feed_kg, 3)


# ============================================================
# WATER QUALITY CHECK
# ============================================================

def check_range(value, minimum, maximum):

    if value < minimum:
        return "LOW"

    elif value > maximum:
        return "HIGH"

    else:
        return "GOOD"


def check_water_quality(
    fish,
    temperature,
    ph,
    dissolved_oxygen,
    alkalinity
):

    result = {}

    result["temperature"] = check_range(
        temperature,
        fish["min_temperature"],
        fish["max_temperature"]
    )

    result["ph"] = check_range(
        ph,
        fish["min_ph"],
        fish["max_ph"]
    )

    result["dissolved_oxygen"] = check_range(
        dissolved_oxygen,
        fish["min_do"],
        fish["max_do"]
    )

    result["alkalinity"] = check_range(
        alkalinity,
        fish["min_alkalinity"],
        fish["max_alkalinity"]
    )

    return result


# ============================================================
# AMMONIA CHECK
# ============================================================

def check_ammonia(ammonia):

    if ammonia <= 0.5:
        return "GOOD"

    elif ammonia <= 1.0:
        return "WARNING"

    else:
        return "CRITICAL"


# ============================================================
# NITRITE CHECK
# ============================================================

def check_nitrite(nitrite):

    if nitrite <= 0.5:
        return "GOOD"

    elif nitrite <= 1.0:
        return "WARNING"

    else:
        return "CRITICAL"


# ============================================================
# BIOFLOC SUITABILITY
# ============================================================

def calculate_suitability(
    water_quality,
    ammonia_status,
    nitrite_status
):

    problems = 0
    warnings = 0

    for status in water_quality.values():

        if status == "LOW" or status == "HIGH":
            problems += 1

    if ammonia_status == "CRITICAL":
        problems += 1

    elif ammonia_status == "WARNING":
        warnings += 1

    if nitrite_status == "CRITICAL":
        problems += 1

    elif nitrite_status == "WARNING":
        warnings += 1

    if problems > 0:
        return "NOT SUITABLE"

    elif warnings > 0:
        return "MODERATELY SUITABLE"

    else:
        return "HIGHLY SUITABLE"
# ============================================================
# WATER QUALITY RECOMMENDATION ENGINE
# ============================================================

def get_water_quality_recommendations(
    fish,
    temperature,
    ph,
    dissolved_oxygen,
    ammonia,
    nitrite,
    alkalinity
):
    recommendations = []

    # --------------------------------------------------------
    # Temperature
    # --------------------------------------------------------

    if temperature < fish["min_temperature"]:
        recommendations.append({
            "parameter": "Temperature",
            "status": "LOW",
            "message": (
                f"Temperature is below the recommended range "
                f"({fish['min_temperature']}–"
                f"{fish['max_temperature']} °C)."
            ),
            "action": (
                "Monitor water temperature and take appropriate "
                "temperature-management measures."
            )
        })

    elif temperature > fish["max_temperature"]:
        recommendations.append({
            "parameter": "Temperature",
            "status": "HIGH",
            "message": (
                f"Temperature is above the recommended range "
                f"({fish['min_temperature']}–"
                f"{fish['max_temperature']} °C)."
            ),
            "action": (
                "Reduce heat stress and closely monitor the fish."
            )
        })

    else:
        recommendations.append({
            "parameter": "Temperature",
            "status": "GOOD",
            "message": "Temperature is within the recommended range.",
            "action": "Continue regular monitoring."
        })

    # --------------------------------------------------------
    # pH
    # --------------------------------------------------------

    if ph < fish["min_ph"]:
        recommendations.append({
            "parameter": "pH",
            "status": "LOW",
            "message": "pH is below the recommended range.",
            "action": (
                "Check alkalinity and manage the water system "
                "gradually. Avoid sudden pH changes."
            )
        })

    elif ph > fish["max_ph"]:
        recommendations.append({
            "parameter": "pH",
            "status": "HIGH",
            "message": "pH is above the recommended range.",
            "action": (
                "Monitor pH closely and investigate the cause "
                "before making gradual corrections."
            )
        })

    else:
        recommendations.append({
            "parameter": "pH",
            "status": "GOOD",
            "message": "pH is within the recommended range.",
            "action": "Continue regular monitoring."
        })

    # --------------------------------------------------------
    # Dissolved Oxygen
    # --------------------------------------------------------

    if dissolved_oxygen < fish["min_do"]:
        recommendations.append({
            "parameter": "Dissolved Oxygen",
            "status": "CRITICAL",
            "message": "Dissolved oxygen is below the recommended level.",
            "action": (
                "Immediately check aeration and maintain strong "
                "water circulation. Closely monitor fish behavior."
            )
        })

    else:
        recommendations.append({
            "parameter": "Dissolved Oxygen",
            "status": "GOOD",
            "message": "Dissolved oxygen is within the recommended range.",
            "action": "Continue aeration and regular monitoring."
        })

    # --------------------------------------------------------
    # Ammonia
    # --------------------------------------------------------

    if ammonia <= 0.5:

        recommendations.append({
            "parameter": "Ammonia",
            "status": "GOOD",
            "message": "Ammonia is at an acceptable monitoring level.",
            "action": "Continue regular ammonia monitoring."
        })

    elif ammonia <= 1.0:

        recommendations.append({
            "parameter": "Ammonia",
            "status": "WARNING",
            "message": "Ammonia is elevated.",
            "action": (
                "Review feeding, aeration and biofloc condition. "
                "Increase monitoring frequency."
            )
        })

    else:

        recommendations.append({
            "parameter": "Ammonia",
            "status": "CRITICAL",
            "message": "Ammonia is high.",
            "action": (
                "Take immediate corrective action and closely "
                "monitor water quality and fish condition."
            )
        })

    # --------------------------------------------------------
    # Nitrite
    # --------------------------------------------------------

    if nitrite <= 0.5:

        recommendations.append({
            "parameter": "Nitrite",
            "status": "GOOD",
            "message": "Nitrite is at an acceptable monitoring level.",
            "action": "Continue regular monitoring."
        })

    elif nitrite <= 1.0:

        recommendations.append({
            "parameter": "Nitrite",
            "status": "WARNING",
            "message": "Nitrite is elevated.",
            "action": (
                "Monitor nitrite closely and review the "
                "biofloc/water-management condition."
            )
        })

    else:

        recommendations.append({
            "parameter": "Nitrite",
            "status": "CRITICAL",
            "message": "Nitrite is high.",
            "action": (
                "Take immediate corrective action and closely "
                "monitor the fish and water quality."
            )
        })

    # --------------------------------------------------------
    # Alkalinity
    # --------------------------------------------------------

    if alkalinity < fish["min_alkalinity"]:

        recommendations.append({
            "parameter": "Alkalinity",
            "status": "LOW",
            "message": "Alkalinity is below the reference range.",
            "action": (
                "Monitor alkalinity and manage buffering capacity "
                "gradually according to the farm's water-management plan."
            )
        })

    elif alkalinity > fish["max_alkalinity"]:

        recommendations.append({
            "parameter": "Alkalinity",
            "status": "HIGH",
            "message": "Alkalinity is above the reference range.",
            "action": (
                "Continue monitoring and investigate the reason "
                "for elevated alkalinity."
            )
        })

    else:

        recommendations.append({
            "parameter": "Alkalinity",
            "status": "GOOD",
            "message": "Alkalinity is within the reference range.",
            "action": "Continue regular monitoring."
        })

    return recommendations


# ============================================================
# OVERALL WATER QUALITY STATUS
# ============================================================

def get_overall_water_status(recommendations):

    critical_count = 0
    warning_count = 0

    for item in recommendations:

        if item["status"] == "CRITICAL":
            critical_count += 1

        elif item["status"] in ("WARNING", "LOW", "HIGH"):
            warning_count += 1

    if critical_count > 0:

        return {
            "status": "CRITICAL",
            "label": "NEEDS IMMEDIATE ATTENTION"
        }

    elif warning_count > 0:

        return {
            "status": "WARNING",
            "label": "NEEDS ATTENTION"
        }

    else:

        return {
            "status": "GOOD",
            "label": "WATER QUALITY IS GOOD"
        }

# ============================================================
# MAIN BIOFLOC CALCULATION
# ============================================================

def calculate_biofloc(
    fish_name,
    tank_volume_liter,
    fish_count,
    average_weight_g,
    temperature,
    ph,
    dissolved_oxygen,
    ammonia,
    nitrite,
    alkalinity,
    feed_protein
):

    # --------------------------------------------------------
    # Get fish data
    # --------------------------------------------------------

    fish = get_fish_by_name(fish_name)

    if fish is None:
        raise ValueError(
            f"Fish '{fish_name}' was not found in database."
        )

    # --------------------------------------------------------
    # Biomass
    # --------------------------------------------------------

    biomass_kg = calculate_biomass(
        fish_count,
        average_weight_g
    )

    # --------------------------------------------------------
    # Stocking density
    # --------------------------------------------------------

    stocking_density = calculate_stocking_density(
        fish_count,
        tank_volume_liter
    )

    # --------------------------------------------------------
    # Recommended stocking density
    # --------------------------------------------------------

    recommended_density = fish[
        "recommended_stocking_density"
    ]

    if stocking_density <= recommended_density:
        stocking_status = "GOOD"

    elif stocking_density <= recommended_density * 1.20:
        stocking_status = "WARNING"

    else:
        stocking_status = "HIGH"

    # --------------------------------------------------------
    # Daily feed
    # --------------------------------------------------------

    feeding_rate = fish["feeding_rate"]

    daily_feed_kg = calculate_daily_feed(
        biomass_kg,
        feeding_rate
    )
        # --------------------------------------------------------
    # Carbon source
    # --------------------------------------------------------

    carbon_source = "Molasses"

    carbon_result = calculate_carbon_recommendation(
        daily_feed_kg=daily_feed_kg,
        feed_protein_percent=feed_protein,
        carbon_source=carbon_source,
        target_cn_ratio=15
    )

    # --------------------------------------------------------
    # Water quality
    # --------------------------------------------------------

    water_quality = check_water_quality(
        fish,
        temperature,
        ph,
        dissolved_oxygen,
        alkalinity
    )

    # --------------------------------------------------------
    # Ammonia
    # --------------------------------------------------------

    ammonia_status = check_ammonia(ammonia)

    # --------------------------------------------------------
    # Nitrite
    # --------------------------------------------------------

    nitrite_status = check_nitrite(nitrite)
        # --------------------------------------------------------
    # Detailed water quality recommendations
    # --------------------------------------------------------

    water_recommendations = get_water_quality_recommendations(
        fish=fish,
        temperature=temperature,
        ph=ph,
        dissolved_oxygen=dissolved_oxygen,
        ammonia=ammonia,
        nitrite=nitrite,
        alkalinity=alkalinity
    )

    overall_water_status = get_overall_water_status(
        water_recommendations
    )
    # --------------------------------------------------------
    # Overall suitability
    # --------------------------------------------------------

    suitability = calculate_suitability(
        water_quality,
        ammonia_status,
        nitrite_status
    )

    # --------------------------------------------------------
    # Return all results
    # --------------------------------------------------------
        # ========================================================
    # ML PREDICTION
    # ========================================================

    ml_input = {

        "fish_name":
            fish["fish_name"],

        "tank_volume_m3":
            tank_volume_liter / 1000,

        "fish_count":
            fish_count,

        "initial_weight_g":
            average_weight_g,

        "stocking_density_fish_m3":
            stocking_density,

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
            daily_feed_kg,

        "culture_period_days":
            fish["culture_period_days"]
    }

    ml_prediction = predict_biofloc(
        ml_input
    )

    return {

        "fish_name": fish["fish_name"],

        "tank_volume_liter": tank_volume_liter,

        "tank_volume_m3": round(
            tank_volume_liter / 1000,
            2
        ),

        "fish_count": fish_count,

        "average_weight_g": average_weight_g,

        "current_biomass_kg": biomass_kg,

        "stocking_density_fish_m3": stocking_density,

        "recommended_stocking_density_fish_m3":
            recommended_density,

        "stocking_status": stocking_status,

        "feeding_rate_percent": feeding_rate,

        "estimated_daily_feed_kg": daily_feed_kg,

        "feed_protein_percent": feed_protein,

        "carbon_source":
            carbon_result["carbon_source"],

        "target_cn_ratio":
            carbon_result["target_cn_ratio"],

        "estimated_carbon_amount_kg":
            carbon_result["estimated_carbon_amount_kg"],
            
        "temperature": temperature,

    "ph": ph,

    "dissolved_oxygen": dissolved_oxygen,

    "ammonia": ammonia,

    "nitrite": nitrite,

    "alkalinity": alkalinity,

        "temperature_status":
            water_quality["temperature"],

        "ph_status":
            water_quality["ph"],

        "do_status":
            water_quality["dissolved_oxygen"],

        "alkalinity_status":
            water_quality["alkalinity"],

        "ammonia_status":
            ammonia_status,

        "nitrite_status":
            nitrite_status,
                "water_quality_status":
            overall_water_status["status"],

        "water_quality_label":
            overall_water_status["label"],

        "water_recommendations":
            water_recommendations,
        "predicted_final_weight":
        ml_prediction[
        "predicted_final_weight_g"
        ],

        "predicted_final_biomass":
        ml_prediction[
        "predicted_final_biomass_kg"
        ],

        "predicted_survival_rate":
        ml_prediction[
        "predicted_survival_rate_percent"
        ],

        "predicted_fcr":
        ml_prediction[
        "predicted_fcr"
        ],

        "biofloc_suitability":
            suitability
            

    }
    # ============================================================
# BIOFLOC CARBON / C:N CALCULATION
# ============================================================

def calculate_feed_nitrogen(
    daily_feed_kg,
    feed_protein_percent,
    protein_nitrogen_fraction=0.16
):
    """
    Estimate nitrogen contained in feed.

    Protein is approximately 16% nitrogen.
    """

    protein_kg = (
        daily_feed_kg *
        feed_protein_percent /
        100
    )

    nitrogen_kg = (
        protein_kg *
        protein_nitrogen_fraction
    )

    return round(nitrogen_kg, 4)


def calculate_carbon_requirement(
    daily_feed_kg,
    feed_protein_percent,
    target_cn_ratio=15,
    carbon_source_carbon_fraction=0.40,
    nitrogen_retention_fraction=0.25
):
    """
    Estimate carbon-source requirement.

    This is an estimation model, not a fixed universal dose.

    target_cn_ratio:
        Desired carbon:nitrogen ratio.

    carbon_source_carbon_fraction:
        Fraction of carbon in the selected carbon source.

    nitrogen_retention_fraction:
        Estimated fraction of feed nitrogen entering
        the microbial/biofloc system.
    """

    if daily_feed_kg <= 0:
        return 0

    if feed_protein_percent <= 0:
        return 0

    if carbon_source_carbon_fraction <= 0:
        return 0

    nitrogen_kg = calculate_feed_nitrogen(
        daily_feed_kg,
        feed_protein_percent
    )

    microbial_nitrogen_kg = (
        nitrogen_kg *
        nitrogen_retention_fraction
    )

    required_carbon_kg = (
        microbial_nitrogen_kg *
        target_cn_ratio
    )

    carbon_source_kg = (
        required_carbon_kg /
        carbon_source_carbon_fraction
    )

    return round(carbon_source_kg, 3)


# ============================================================
# CARBON SOURCE INFORMATION
# ============================================================

CARBON_SOURCES = {

    "Molasses": {
        "carbon_fraction": 0.40
    },

    "Sugar": {
        "carbon_fraction": 0.40
    },

    "Rice Bran": {
        "carbon_fraction": 0.40
    }
}


def get_carbon_source_info(carbon_source):

    return CARBON_SOURCES.get(
        carbon_source
    )


# ============================================================
# CARBON RECOMMENDATION
# ============================================================

def calculate_carbon_recommendation(
    daily_feed_kg,
    feed_protein_percent,
    carbon_source,
    target_cn_ratio=15
):

    source_info = get_carbon_source_info(
        carbon_source
    )

    if source_info is None:
        raise ValueError(
            f"Unknown carbon source: {carbon_source}"
        )

    carbon_fraction = source_info[
        "carbon_fraction"
    ]

    carbon_amount_kg = calculate_carbon_requirement(
        daily_feed_kg=daily_feed_kg,
        feed_protein_percent=feed_protein_percent,
        target_cn_ratio=target_cn_ratio,
        carbon_source_carbon_fraction=carbon_fraction
    )

    return {
        "carbon_source": carbon_source,
        "target_cn_ratio": target_cn_ratio,
        "estimated_carbon_amount_kg": carbon_amount_kg,
        "carbon_fraction": carbon_fraction
    }

# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    result = calculate_biofloc(

        fish_name="Tilapia",

        tank_volume_liter=10000,

        fish_count=2000,

        average_weight_g=20,

        temperature=28,

        ph=7.5,

        dissolved_oxygen=5.5,

        ammonia=0.3,

        nitrite=0.2,

        alkalinity=120,

        feed_protein=30
    )

    print("\n========================================")
    print("       BIOFLOC CALCULATION RESULT")
    print("========================================")
    
        # ========================================================
    # ML PREDICTION
    # ========================================================

     
    

    for key, value in result.items():

        print(
            f"{key}: {value}"
        )

    print("========================================")

    # ========================================================
    # SAVE PREDICTION HISTORY
    # ========================================================

    try:

        prediction_id = save_prediction(result)

        print(
            f"\nPrediction saved successfully."
        )

        print(
            f"Prediction ID: {prediction_id}"
        )

    except Exception as e:

        print(
            f"\nCould not save prediction history."
        )

        print(
            f"Error: {e}"
        )