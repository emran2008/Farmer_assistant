const API_URL =
    "http://127.0.0.1:5000/api/biofloc/predict";


// ============================================================
// HELPER
// ============================================================

function getValue(id) {

    return document
        .getElementById(id)
        .value;
}


// ============================================================
// SHOW / HIDE
// ============================================================

function showElement(id) {

    document
        .getElementById(id)
        .classList
        .remove("hidden");
}


function hideElement(id) {

    document
        .getElementById(id)
        .classList
        .add("hidden");
}


// ============================================================
// ANALYZE BIOFLOC
// ============================================================

async function analyzeBiofloc() {

    const button =
        document.getElementById("analyzeBtn");

    const loading =
        document.getElementById("loading");

    const errorBox =
        document.getElementById("errorBox");


    // --------------------------------------------------------
    // Reset
    // --------------------------------------------------------

    hideElement("errorBox");

    hideElement("results");

    showElement("loading");

    button.disabled = true;


    try {

        // ====================================================
        // COLLECT INPUT
        // ====================================================

        const data = {

            fish_name:
                getValue("fish_name"),

            tank_volume_liter:
                getTankVolumeInLiters(),

            fish_count:
                Number(
                    getValue("fish_count")
                ),

            average_weight_g:
                Number(
                    getValue("average_weight_g")
                ),

            temperature:
                Number(
                    getValue("temperature")
                ),

            ph:
                Number(
                    getValue("ph")
                ),

            dissolved_oxygen:
                Number(
                    getValue("dissolved_oxygen")
                ),

            ammonia:
                Number(
                    getValue("ammonia")
                ),

            nitrite:
                Number(
                    getValue("nitrite")
                ),

            alkalinity:
                Number(
                    getValue("alkalinity")
                ),

            feed_protein:
                Number(
                    getValue("feed_protein")
                )
        };


        // ====================================================
        // VALIDATION
        // ====================================================

        for (
            const [key, value]
            of Object.entries(data)
        ) {

            if (
                key !== "fish_name" &&
                (
                    Number.isNaN(value) ||
                    value === null
                )
            ) {

                throw new Error(
                    `Invalid value for ${key}`
                );
            }
        }


        // ====================================================
        // API REQUEST
        // ====================================================

        const response =
            await fetch(
                API_URL,
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify(data)
                }
            );


        const responseText =
    await response.text();

console.log("API STATUS:", response.status);
console.log("API RESPONSE:", responseText);

let responseData;

try {

    responseData =
        JSON.parse(responseText);

} catch (error) {

    throw new Error(
        `API returned invalid response. Status: ${response.status}. Response: ${responseText.substring(0, 200)}`
    );
}


        // ====================================================
        // API ERROR
        // ====================================================

        if (
            !response.ok ||
            !responseData.success
        ) {

            throw new Error(

                responseData.message ||
                "Biofloc analysis failed."

            );
        }


        // ====================================================
        // DISPLAY RESULT
        // ====================================================

        displayResults(
            responseData.result
        );


        showElement("results");


    }

    catch (error) {

        console.error(
            "BIOFLOC ERROR:",
            error
        );

        errorBox.textContent =
            error.message;

        showElement("errorBox");

    }

    finally {

        hideElement("loading");

        button.disabled = false;

    }
}


// ============================================================
// DISPLAY RESULTS
// ============================================================

function displayResults(result) {


    // ========================================================
    // OVERALL
    // ========================================================

    document
        .getElementById("bioflocSuitability")
        .textContent =
            result.biofloc_suitability ||
            "Not available";


    // ========================================================
    // PRODUCTION
    // ========================================================

    document
        .getElementById("currentBiomass")
        .textContent =
            formatValue(
                result.current_biomass_kg,
                " kg"
            );


    document
        .getElementById("stockingDensity")
        .textContent =
            formatValue(
                result.stocking_density_fish_m3,
                " fish/m³"
            );


    document
        .getElementById("dailyFeed")
        .textContent =
            formatValue(
                result.estimated_daily_feed_kg,
                " kg/day"
            );


    // ========================================================
    // WATER QUALITY
    // ========================================================

    document
        .getElementById("temperatureStatus")
        .textContent =
            result.temperature_status ||
            result.temperature ||
            "-";


    document
        .getElementById("phStatus")
        .textContent =
            result.ph_status ||
            result.ph ||
            "-";


    document
        .getElementById("doStatus")
        .textContent =
            result.dissolved_oxygen_status ||
            result.dissolved_oxygen ||
            "-";


    document
        .getElementById("ammoniaStatus")
        .textContent =
            result.ammonia_status ||
            result.ammonia ||
            "-";


    document
        .getElementById("nitriteStatus")
        .textContent =
            result.nitrite_status ||
            result.nitrite ||
            "-";


    document
        .getElementById("alkalinityStatus")
        .textContent =
            result.alkalinity_status ||
            result.alkalinity ||
            "-";


    // ========================================================
    // BIOFLOC
    // ========================================================

    document
        .getElementById("carbonSource")
        .textContent =
            result.carbon_source ||
            "-";


    document
        .getElementById("cnRatio")
        .textContent =
            result.target_cn_ratio ||
            "-";


    document
        .getElementById("carbonAmount")
        .textContent =
            formatValue(
                result.estimated_carbon_amount_kg,
                " kg"
            );


        // ========================================================
    // ML PREDICTION
    // ========================================================

    const mlPrediction =
        result.ml_prediction || {};

    const predictionElement =
        document.getElementById("mlPrediction");

    if (predictionElement) {

        predictionElement.textContent =
            mlPrediction.predicted_fish ||
            mlPrediction.prediction ||
            result.predicted_fish ||
            "Not available";
    }


    const confidenceElement =
        document.getElementById("mlConfidence");

    if (confidenceElement) {

        confidenceElement.textContent =
            formatValue(
                mlPrediction.confidence,
                "%"
            );
    }


  
    document
        .getElementById("finalWeight")
        .textContent =
            formatValue(
                result.predicted_final_weight,
                " g"
            );


    document
        .getElementById("finalBiomass")
        .textContent =
            formatValue(
                result.predicted_final_biomass,
                " kg"
            );


    document
        .getElementById("survivalRate")
        .textContent =
            formatValue(
                result.predicted_survival_rate,
                "%"
            );


    document
        .getElementById("fcr")
        .textContent =
            result.predicted_fcr ??
            "-";


        // ========================================================
    // RECOMMENDATIONS
    // ========================================================

    displayRecommendations(
        result
    );


    // ========================================================
    // FARM ACTION PLAN
    // ========================================================

    displayActionPlan(
        result
    );


    // ========================================================
    // BIOFLOC MANAGEMENT PLAN
    // ========================================================

    displayManagementRecommendation(
        result
    );

} // displayResults শেষ


// ============================================================
// FORMAT VALUE
// ============================================================
function formatValue(
    value,
    suffix = ""
) {

    if (
        value === undefined ||
        value === null ||
        value === ""
    ) {

        return "-";
    }


    if (
        typeof value === "number"
    ) {

        return value + suffix;
    }


    return value + suffix;
}




// ============================================================
// DISPLAY RECOMMENDATIONS
// ============================================================

function displayRecommendations(result) {

    const container =
        document.getElementById("recommendations");

    if (!container) {
        console.warn("Recommendations container not found.");
        return;
    }

    container.innerHTML = "";

    const recommendations =
        result.water_recommendations || [];

    if (!recommendations.length) {

        container.innerHTML = `
            <div class="recommendation-item">
                ✓ No additional recommendations available.
            </div>
        `;

        return;
    }

    recommendations.forEach((recommendation) => {

        const item =
            document.createElement("div");

        item.className =
            "recommendation-item";

        // Object হলে সুন্দরভাবে display
        if (
            typeof recommendation === "object" &&
            recommendation !== null
        ) {

            const title =
                recommendation.title ||
                recommendation.name ||
                recommendation.category ||
                "";

            const message =
                recommendation.message ||
                recommendation.description ||
                recommendation.text ||
                recommendation.recommendation ||
                "";

            if (title && message) {

                item.innerHTML = `
                    <strong>✓ ${title}</strong>
                    <br>
                    <span>${message}</span>
                `;

            } else {

                item.textContent =
                    "✓ " +
                    Object.values(recommendation)
                        .filter(value =>
                            value !== null &&
                            value !== undefined
                        )
                        .join(" — ");
            }

        } else {

            item.textContent =
                "✓ " + recommendation;
        }

        container.appendChild(item);
    });
}
// ============================================================
// ACTION PLAN
// ============================================================

function displayActionPlan(result) {

    const container =
        document.getElementById("actionPlan");


    container.innerHTML = "";


    const actions = [];


    // --------------------------------------------------------
    // TEMPERATURE
    // --------------------------------------------------------

    if (
        result.temperature_status &&
        result.temperature_status
            .toString()
            .toUpperCase()
            !== "GOOD"
    ) {

        actions.push(
            "Monitor water temperature closely and keep it within the recommended range for the selected fish."
        );
    }


    // --------------------------------------------------------
    // pH
    // --------------------------------------------------------

    if (
        result.ph_status &&
        result.ph_status
            .toString()
            .toUpperCase()
            !== "GOOD"
    ) {

        actions.push(
            "Check and stabilize pond pH. Avoid making sudden changes."
        );
    }


    // --------------------------------------------------------
    // DO
    // --------------------------------------------------------

    if (
        result.dissolved_oxygen_status &&
        result.dissolved_oxygen_status
            .toString()
            .toUpperCase()
            !== "GOOD"
    ) {

        actions.push(
            "Increase aeration and monitor dissolved oxygen regularly."
        );
    }


    // --------------------------------------------------------
    // AMMONIA
    // --------------------------------------------------------

    if (
        result.ammonia_status &&
        result.ammonia_status
            .toString()
            .toUpperCase()
            !== "GOOD"
    ) {

        actions.push(
            "Ammonia needs attention. Reduce excessive feeding, improve aeration and monitor ammonia again."
        );
    }


    // --------------------------------------------------------
    // NITRITE
    // --------------------------------------------------------

    if (
        result.nitrite_status &&
        result.nitrite_status
            .toString()
            .toUpperCase()
            !== "GOOD"
    ) {

        actions.push(
            "Nitrite needs attention. Maintain good aeration and monitor water quality frequently."
        );
    }


    // --------------------------------------------------------
    // ALKALINITY
    // --------------------------------------------------------

    if (
        result.alkalinity_status &&
        result.alkalinity_status
            .toString()
            .toUpperCase()
            !== "GOOD"
    ) {

        actions.push(
            "Check alkalinity and maintain stable buffering capacity for the biofloc system."
        );
    }


    // --------------------------------------------------------
    // NO PROBLEM
    // --------------------------------------------------------

    if (actions.length === 0) {

        const message =
            document.createElement("div");

        message.className =
            "recommendation-item";

        message.textContent =
            "✅ Current water quality looks suitable. Continue regular monitoring and maintain the recommended feeding and aeration schedule.";

        container.appendChild(message);

        return;
    }


    // --------------------------------------------------------
    // SHOW ACTIONS
    // --------------------------------------------------------

    actions.forEach(action => {

        const item =
            document.createElement("div");

        item.className =
            "warning-item";

        item.textContent =
            "⚠️ " + action;

        container.appendChild(item);

    });
}
// ============================================================
// BIOFLOC MANAGEMENT RECOMMENDATION
// ============================================================

function displayManagementRecommendation(result) {

    const container =
        document.getElementById("managementRecommendation");

    if (!container) {
        return;
    }

    container.innerHTML = "";

    const recommendations = [];


    // ========================================================
    // CARBON SOURCE
    // ========================================================

    if (result.carbon_source) {

        recommendations.push(
            `🧫 Carbon Source: ${result.carbon_source}`
        );
    }


    // ========================================================
    // C:N RATIO
    // ========================================================

    if (result.target_cn_ratio !== undefined) {

        recommendations.push(
            `📊 Target C:N Ratio: ${result.target_cn_ratio}`
        );
    }


    // ========================================================
    // CARBON AMOUNT
    // ========================================================

    if (
        result.estimated_carbon_amount_kg !== undefined
    ) {

        recommendations.push(
            `⚖️ Estimated Carbon Required: ${result.estimated_carbon_amount_kg} kg`
        );
    }


    // ========================================================
    // FEED
    // ========================================================

    if (
        result.estimated_daily_feed_kg !== undefined
    ) {

        recommendations.push(
            `🍽️ Estimated Daily Feed: ${result.estimated_daily_feed_kg} kg/day`
        );
    }


    // ========================================================
    // DO / AERATION
    // ========================================================

    const doStatus =
        String(
            result.dissolved_oxygen_status || ""
        ).toUpperCase();


    if (doStatus === "GOOD") {

        recommendations.push(
            "💨 Aeration: Current dissolved oxygen condition is suitable. Continue regular aeration."
        );

    } else {

        recommendations.push(
            "🚨 Aeration: Increase aeration and monitor dissolved oxygen closely."
        );
    }


    // ========================================================
    // AMMONIA
    // ========================================================

    const ammoniaStatus =
        String(
            result.ammonia_status || ""
        ).toUpperCase();


    if (ammoniaStatus === "GOOD") {

        recommendations.push(
            "🧪 Ammonia: Current level is within the acceptable range."
        );

    } else {

        recommendations.push(
            "⚠️ Ammonia: Take corrective action, avoid overfeeding and improve aeration."
        );
    }


    // ========================================================
    // NITRITE
    // ========================================================

    const nitriteStatus =
        String(
            result.nitrite_status || ""
        ).toUpperCase();


    if (nitriteStatus === "GOOD") {

        recommendations.push(
            "🧪 Nitrite: Current level is within the acceptable range."
        );

    } else {

        recommendations.push(
            "⚠️ Nitrite: Monitor closely and maintain strong aeration."
        );
    }


    // ========================================================
    // ALKALINITY
    // ========================================================

    const alkalinityStatus =
        String(
            result.alkalinity_status || ""
        ).toUpperCase();


    if (alkalinityStatus === "GOOD") {

        recommendations.push(
            "💧 Alkalinity: Suitable for the current biofloc condition."
        );

    } else {

        recommendations.push(
            "⚠️ Alkalinity: Check alkalinity and maintain stable buffering capacity."
        );
    }


    // ========================================================
    // DISPLAY
    // ========================================================

    recommendations.forEach(
        recommendation => {

            const item =
                document.createElement("div");

            item.className =
                "recommendation-item";

            item.textContent =
                recommendation;

            container.appendChild(item);

        }
    );
}
// ============================================================
// ADVANCED PARAMETERS TOGGLE
// ============================================================

function toggleAdvancedParameters() {

    const section =
        document.getElementById(
            "advancedParameters"
        );

    const arrow =
        document.getElementById(
            "advancedArrow"
        );


    section.classList.toggle(
        "hidden"
    );


    if (
        section.classList.contains(
            "hidden"
        )
    ) {

        arrow.textContent = "▼";

    } else {

        arrow.textContent = "▲";

    }
}
// ============================================================
// TANK VOLUME CONVERSION
// ============================================================

function getTankVolumeInLiters() {

    const value =
        Number(
            document.getElementById(
                "tank_volume_input"
            ).value
        );

    const unit =
        document.getElementById(
            "tank_volume_unit"
        ).value;


    if (!value || value <= 0) {

        throw new Error(
            "Please enter a valid tank/pond volume."
        );
    }


    // m³ → Liter
    if (unit === "m3") {

        return value * 1000;
    }


    // Liter
    return value;
}
// ============================================================
// UPDATE VOLUME DISPLAY
// ============================================================

function updateVolumeConversion() {

    const input =
        document.getElementById(
            "tank_volume_input"
        );

    const unit =
        document.getElementById(
            "tank_volume_unit"
        );

    const display =
        document.getElementById(
            "volumeConversionText"
        );


    const value =
        Number(input.value);


    if (!value || value <= 0) {

        display.textContent =
            "Enter a valid volume.";

        return;
    }


    let liters;


    if (unit.value === "m3") {

        liters =
            value * 1000;

    } else {

        liters =
            value;
    }


    display.textContent =
        `${liters.toLocaleString()} Liter`;
}
document
    .getElementById("tank_volume_input")
    .addEventListener(
        "input",
        updateVolumeConversion
    );


document
    .getElementById("tank_volume_unit")
    .addEventListener(
        "change",
        updateVolumeConversion
    );