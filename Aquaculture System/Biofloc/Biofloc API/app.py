from pathlib import Path
import sys

from flask import Flask, request, jsonify
from flask_cors import CORS


# ============================================================
# PATH SETUP
# ============================================================

CURRENT_DIR = Path(__file__).resolve().parent

BIOFLOC_DIR = CURRENT_DIR.parent


# ============================================================
# CALCULATOR IMPORT
# ============================================================

CALCULATOR_DIR = BIOFLOC_DIR / "Biofloc Calculator"

sys.path.insert(0, str(CALCULATOR_DIR))

from biofloc_calculator import calculate_biofloc


# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)

CORS(app)


# ============================================================
# HOME
# ============================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "success": True,

        "message": "Biofloc API is running.",

        "service": "Aquaculture Biofloc System"

    })


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/api/biofloc/health", methods=["GET"])
def health():

    return jsonify({

        "success": True,

        "status": "online"

    })


# ============================================================
# BIOFLOC PREDICTION
# ============================================================

@app.route(
    "/api/biofloc/predict",
    methods=["POST"]
)
def biofloc_predict():

    try:

        data = request.get_json()

        if not data:

            return jsonify({

                "success": False,

                "message": "No JSON data received."

            }), 400


        # ====================================================
        # REQUIRED INPUTS
        # ====================================================

        required_fields = [

            "fish_name",

            "tank_volume_liter",

            "fish_count",

            "average_weight_g",

            "temperature",

            "ph",

            "dissolved_oxygen",

            "ammonia",

            "nitrite",

            "alkalinity",

            "feed_protein"

        ]


        missing_fields = [

            field

            for field in required_fields

            if field not in data
        ]


        if missing_fields:

            return jsonify({

                "success": False,

                "message": "Missing required fields.",

                "missing_fields": missing_fields

            }), 400


        # ====================================================
        # CONVERT NUMERIC INPUTS
        # ====================================================

        result = calculate_biofloc(

            fish_name=str(
                data["fish_name"]
            ),

            tank_volume_liter=float(
                data["tank_volume_liter"]
            ),

            fish_count=int(
                data["fish_count"]
            ),

            average_weight_g=float(
                data["average_weight_g"]
            ),

            temperature=float(
                data["temperature"]
            ),

            ph=float(
                data["ph"]
            ),

            dissolved_oxygen=float(
                data["dissolved_oxygen"]
            ),

            ammonia=float(
                data["ammonia"]
            ),

            nitrite=float(
                data["nitrite"]
            ),

            alkalinity=float(
                data["alkalinity"]
            ),

            feed_protein=float(
                data["feed_protein"]
            )
        )


        # ====================================================
        # RESPONSE
        # ====================================================

        return jsonify({

            "success": True,

            "message": "Biofloc prediction completed.",

            "result": result

        })


    except ValueError as e:

        return jsonify({

            "success": False,

            "message": "Invalid input value.",

            "error": str(e)

        }), 400


    except Exception as e:

        print(
            "BIOFLOC API ERROR:",
            repr(e)
        )

        return jsonify({

            "success": False,

            "message": "Internal server error.",

            "error": str(e)

        }), 500


# ============================================================
# DEBUG ROUTES
# ============================================================

print("\n========== BIOFLOC API ROUTES ==========")

for rule in app.url_map.iter_rules():
    print(
        rule,
        "->",
        sorted(rule.methods)
    )

print("========================================")


# ============================================================
# RUN SERVER
# ============================================================

if __name__ == "__main__":

    print("\n========================================")
    print("BIOFLOC API SERVER")
    print("========================================")

    print(
        "API: http://127.0.0.1:5000"
    )

    print(
        "Health: http://127.0.0.1:5000/api/biofloc/health"
    )

    print(
        "Prediction: POST /api/biofloc/predict"
    )

    print("========================================\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
