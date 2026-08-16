import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import matplotlib.pyplot as plt


# =====================================================
# PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = (
    BASE_DIR
    / "Dataset"
    / "cleaned_pond_dataset.csv"
)

MODEL_PATH = BASE_DIR / "pond_fish_model.pkl"


# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv(DATASET_PATH)

print("\nDataset loaded successfully.")
print("Total rows:", len(df))


# =====================================================
# FEATURES AND TARGET
# =====================================================

features = [
    "ph",
    "temperature",
    "turbidity"
]

target = "fish"


X = df[features]
y = df[target]


# =====================================================
# TRAIN / TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# =====================================================
# MODEL
# =====================================================

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)


print("\nTraining Random Forest model...")

model.fit(X_train, y_train)


# =====================================================
# PREDICTION
# =====================================================

y_pred = model.predict(X_test)
# =====================================================
# CONFUSION MATRIX
# =====================================================

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=model.classes_
)

print("\n========================================")
print("CONFUSION MATRIX")
print("========================================")

print("Fish classes:")
print(model.classes_)

print("\nConfusion Matrix:")
print(cm)


# =====================================================
# FEATURE IMPORTANCE
# =====================================================

print("\n========================================")
print("FEATURE IMPORTANCE")
print("========================================")

for feature, importance in zip(
    features,
    model.feature_importances_
):
    print(
        f"{feature}: {importance:.4f}"
    )


# =====================================================
# SAVE CONFUSION MATRIX IMAGE
# =====================================================

plt.figure(figsize=(10, 8))

plt.imshow(cm)

plt.title("Fish Prediction Confusion Matrix")
plt.xlabel("Predicted Fish")
plt.ylabel("Actual Fish")

plt.xticks(
    range(len(model.classes_)),
    model.classes_,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(model.classes_)),
    model.classes_
)

plt.colorbar()

plt.tight_layout()

confusion_matrix_path = (
    BASE_DIR / "confusion_matrix.png"
)

plt.savefig(confusion_matrix_path)

plt.close()

print("\nConfusion matrix saved to:")
print(confusion_matrix_path)


# =====================================================
# EVALUATION
# =====================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n========================================")
print("MODEL PERFORMANCE")
print("========================================")

print(f"Accuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(model, MODEL_PATH)

print("\n========================================")
print("MODEL SAVED SUCCESSFULLY")
print("========================================")

print("Model path:")
print(MODEL_PATH)