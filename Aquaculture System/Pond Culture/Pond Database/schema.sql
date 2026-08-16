CREATE TABLE IF NOT EXISTS fish_species (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fish_name TEXT UNIQUE NOT NULL,

    min_temperature REAL,
    max_temperature REAL,

    min_ph REAL,
    max_ph REAL,

    min_do REAL,

    stocking_density_min REAL,
    stocking_density_max REAL,
    stocking_density_unit TEXT,
    feeding_rate REAL,
    expected_growth REAL,
    culture_period_days INTEGER
    survival_rate REAL,

    target_weight REAL,

    feeding_rate REAL,

    expected_growth REAL,

    culture_period_days INTEGER,

    data_source TEXT
);


CREATE TABLE IF NOT EXISTS pond_training_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pond_size REAL,
    pond_depth REAL,
    temperature REAL,
    ph REAL,
    do REAL,

    fish_name TEXT
);


CREATE TABLE IF NOT EXISTS fish_species (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fish_name TEXT UNIQUE NOT NULL,

    min_temperature REAL,
    max_temperature REAL,

    min_ph REAL,
    max_ph REAL,

    min_do REAL,

    stocking_density_min REAL,
    stocking_density_max REAL,
    stocking_density_unit TEXT,

    feeding_rate REAL,
    expected_growth REAL,
    culture_period_days INTEGER,

    survival_rate REAL,
    target_weight REAL,

    data_source TEXT
);