CREATE TABLE IF NOT EXISTS crops (
    crop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_name_bn TEXT NOT NULL,
    crop_name_en TEXT NOT NULL,
    scientific_name TEXT,
    category TEXT,
    active INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS diseases (
    disease_id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_id INTEGER NOT NULL,
    disease_name_bn TEXT NOT NULL,
    disease_name_en TEXT NOT NULL,
    pathogen_type TEXT,
    pathogen_name TEXT,
    description TEXT,
    symptoms TEXT,
    favorable_conditions TEXT,
    prevention TEXT,
    treatment TEXT,
    severity TEXT,
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id)
);

CREATE TABLE IF NOT EXISTS disease_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_id INTEGER NOT NULL,
    image_path TEXT,
    source_name TEXT,
    source_url TEXT,
    license_info TEXT,
    verified INTEGER DEFAULT 0,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id)
);

CREATE TABLE IF NOT EXISTS disease_sources (
    source_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_id INTEGER NOT NULL,
    organization TEXT,
    source_title TEXT,
    source_url TEXT,
    source_type TEXT,
    verified INTEGER DEFAULT 0,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id)
);

CREATE TABLE IF NOT EXISTS symptoms (
    symptom_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_id INTEGER NOT NULL,
    symptom_bn TEXT NOT NULL,
    affected_part TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id)
);

CREATE TABLE IF NOT EXISTS treatments (
    treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_id INTEGER NOT NULL,
    treatment_type TEXT,
    treatment_title TEXT,
    instructions TEXT,
    precaution TEXT,
    verified INTEGER DEFAULT 0,
    source_url TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id)
);

CREATE TABLE IF NOT EXISTS pesticides (
    pesticide_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    active_ingredient TEXT,
    formulation TEXT,
    manufacturer TEXT,
    registration_number TEXT,
    approved INTEGER DEFAULT 0,
    source_url TEXT
);

CREATE TABLE IF NOT EXISTS pesticide_usage (
    usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pesticide_id INTEGER NOT NULL,
    crop_id INTEGER NOT NULL,
    disease_id INTEGER NOT NULL,
    dose TEXT,
    water_volume TEXT,
    application_method TEXT,
    application_timing TEXT,
    waiting_period TEXT,
    safety_instruction TEXT,
    verified INTEGER DEFAULT 0,
    FOREIGN KEY (pesticide_id) REFERENCES pesticides(pesticide_id),
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id),
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id)
);