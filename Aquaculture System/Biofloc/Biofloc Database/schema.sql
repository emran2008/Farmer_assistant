CREATE TABLE IF NOT EXISTS fish_species (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    fish_name TEXT NOT NULL UNIQUE,

    min_temperature REAL,
    max_temperature REAL,

    min_ph REAL,
    max_ph REAL,

    min_do REAL,
    max_do REAL,

    min_alkalinity REAL,
    max_alkalinity REAL,

    recommended_stocking_density REAL,

    feeding_rate REAL,

    expected_growth REAL,

    culture_period_days INTEGER
);


CREATE TABLE IF NOT EXISTS biofloc_predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    fish_name TEXT,

    tank_volume REAL,

    fish_count INTEGER,

    average_weight REAL,

    temperature REAL,

    ph REAL,

    dissolved_oxygen REAL,

    ammonia REAL,

    nitrite REAL,

    alkalinity REAL,

    feed_protein REAL,

    daily_feed REAL,

    carbon_source TEXT,

    carbon_amount REAL,

    predicted_final_weight REAL,

    predicted_final_biomass REAL,

    predicted_survival_rate REAL,

    predicted_fcr REAL,

    recommendation TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- ============================================================
-- BIOFLOC PREDICTION HISTORY
-- ============================================================

CREATE TABLE IF NOT EXISTS biofloc_predictions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    fish_name TEXT NOT NULL,

    tank_volume REAL,

    fish_count INTEGER,

    average_weight REAL,

    temperature REAL,

    ph REAL,

    dissolved_oxygen REAL,

    ammonia REAL,

    nitrite REAL,

    alkalinity REAL,

    feed_protein REAL,

    daily_feed REAL,

    carbon_source TEXT,

    carbon_amount REAL,

    predicted_final_weight REAL,

    predicted_final_biomass REAL,

    predicted_survival_rate REAL,

    predicted_fcr REAL,

    recommendation TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);