import json
from pathlib import Path

import torch
from PIL import Image
from torchvision import models, transforms
from huggingface_hub import hf_hub_download


MODEL_REPO = "Saon110/bd-crop-vegetable-plant-disease-model"

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# --------------------------------------------------
# MODEL DOWNLOAD
# --------------------------------------------------

def download_model():

    print("AI model download হচ্ছে...")

    model_path = hf_hub_download(
        repo_id=MODEL_REPO,
        filename="crop_veg_plant_disease_model.pth"
    )

    class_path = hf_hub_download(
        repo_id=MODEL_REPO,
        filename="class_mapping.json"
    )

    return model_path, class_path


# --------------------------------------------------
# MODEL LOAD
# --------------------------------------------------

model_path, class_path = download_model()


with open(
    class_path,
    "r",
    encoding="utf-8"
) as f:

    class_mapping = json.load(f)


# class_mapping হতে পারে dictionary
# অথবা list

if isinstance(class_mapping, dict):

    CLASS_NAMES = [
        class_mapping[str(i)]
        for i in range(len(class_mapping))
    ]

else:

    CLASS_NAMES = class_mapping


print(
    "Total AI classes:",
    len(CLASS_NAMES)
)


# --------------------------------------------------
# RESNET50
# --------------------------------------------------

model = models.resnet50(
    weights=None
)


num_features = model.fc.in_features


model.fc = torch.nn.Sequential(

    torch.nn.Linear(
        num_features,
        512
    ),

    torch.nn.ReLU(),

    torch.nn.Dropout(0.2),

    torch.nn.Linear(
        512,
        len(CLASS_NAMES)
    )
)


checkpoint = torch.load(
    model_path,
    map_location=DEVICE
)


if isinstance(checkpoint, dict):

    if "state_dict" in checkpoint:

        checkpoint = checkpoint["state_dict"]


    elif "model_state_dict" in checkpoint:

        checkpoint = checkpoint["model_state_dict"]


model.load_state_dict(
    checkpoint,
    strict=False
)


model = model.to(DEVICE)

model.eval()


# --------------------------------------------------
# IMAGE TRANSFORM
# --------------------------------------------------

transform = transforms.Compose([

    transforms.Resize(
        (224, 224)
    ),

    transforms.ToTensor(),

    transforms.Normalize(

        mean=[
            0.485,
            0.456,
            0.406
        ],

        std=[
            0.229,
            0.224,
            0.225
        ]
    )
])


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

def predict_disease(image_path):

    image = Image.open(
        image_path
    ).convert("RGB")


    image_tensor = transform(
        image
    ).unsqueeze(0)


    image_tensor = image_tensor.to(
        DEVICE
    )


    with torch.no_grad():

        output = model(
            image_tensor
        )


        probabilities = torch.softmax(
            output,
            dim=1
        )


        confidence, index = torch.max(
            probabilities,
            dim=1
        )


    confidence = (
        confidence.item() * 100
    )


    index = index.item()


    disease_name = CLASS_NAMES[index]


    return {

        "disease": disease_name,

        "confidence": round(
            confidence,
            2
        )

    }