from pathlib import Path
import json
import random

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import transforms, models

from datasets import load_dataset


DATASET_NAME = (
    "Saon110/bd-crop-vegetable-plant-disease-dataset"
)

MODEL_DIR = Path(__file__).resolve().parent.parent / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)


IMAGE_SIZE = 224

BATCH_SIZE = 16

EPOCHS = 8

LEARNING_RATE = 0.0001

SEED = 42


random.seed(SEED)

torch.manual_seed(SEED)


device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)


print("=" * 60)

print("CROP DISEASE AI TRAINING")

print("=" * 60)

print(
    "Device:",
    device
)


def get_dataset():

    print("\nDataset loading...")

    dataset = load_dataset(
        DATASET_NAME
    )

    print(dataset)

    return dataset


def prepare_image(image):

    if image.mode != "RGB":

        image = image.convert("RGB")

    return image


def create_transforms():

    train_transform = transforms.Compose([

        transforms.Resize(
            (IMAGE_SIZE, IMAGE_SIZE)
        ),

        transforms.RandomHorizontalFlip(),

        transforms.RandomRotation(15),

        transforms.ColorJitter(
            brightness=0.2,
            contrast=0.2,
            saturation=0.2
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


    test_transform = transforms.Compose([

        transforms.Resize(
            (IMAGE_SIZE, IMAGE_SIZE)
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

    return train_transform, test_transform
def create_pytorch_dataset(dataset, transform):

    dataset = dataset.remove_columns(
        ["label_name"]
    )

    dataset = dataset.with_transform(
        lambda examples: {
            "image": [
                transform(
                    prepare_image(image)
                )
                for image in examples["image"]
            ],
            "label": examples["label"]
        }
    )

    return dataset


def build_model(num_classes):

    print(
        "\nModel তৈরি হচ্ছে..."
    )

    model = models.resnet18(
        weights=models.ResNet18_Weights.DEFAULT
    )

    for parameter in model.parameters():
        parameter.requires_grad = False

        # শেষের layer trainable
    for parameter in model.layer4.parameters():
        parameter.requires_grad = True

        # classifier
    model.fc = nn.Linear(
        model.fc.in_features,
        num_classes
    )

    model = model.to(device)

    return model
def collate_fn(batch):

    images = torch.stack(
        [item["image"] for item in batch]
    )

    labels = torch.tensor(
        [item["label"] for item in batch],
        dtype=torch.long
    )

    return {
        "image": images,
        "label": labels
    }
def train_model(
    model,
    train_loader,
    valid_loader,
    criterion,
    optimizer
):

    best_accuracy = 0.0
    start_epoch = 0

    checkpoint_path = (
        MODEL_DIR /
        "training_checkpoint.pth"
    )

    best_model_path = (
        MODEL_DIR /
        "best_crop_disease_model.pth"
    )

    # =====================================================
    # RESUME FROM CHECKPOINT
    # =====================================================

    if checkpoint_path.exists():

        print("\nCheckpoint found!")
        print("Loading previous training...")

        checkpoint = torch.load(
            checkpoint_path,
            map_location=device
        )

        model.load_state_dict(
            checkpoint["model_state_dict"]
        )

        optimizer.load_state_dict(
            checkpoint["optimizer_state_dict"]
        )

        start_epoch = (
            checkpoint["epoch"] + 1
        )

        best_accuracy = (
            checkpoint["best_accuracy"]
        )

        print(
            f"Resuming from "
            f"Epoch {start_epoch + 1}/{EPOCHS}"
        )

    # =====================================================
    # TRAINING
    # =====================================================

    for epoch in range(
        start_epoch,
        EPOCHS
    ):

        print(
            f"\nEpoch {epoch + 1}/{EPOCHS}"
        )

        model.train()

        running_loss = 0.0
        correct = 0
        total = 0

        total_batches = len(
            train_loader
        )

        for batch_index, batch in enumerate(
            train_loader,
            start=1
        ):

            images = batch["image"]
            labels = batch["label"]

            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            outputs = model(images)

            loss = criterion(
                outputs,
                labels
            )

            loss.backward()

            optimizer.step()

            running_loss += (
                loss.item() *
                images.size(0)
            )

            predictions = outputs.argmax(
                dim=1
            )

            correct += (
                (predictions == labels)
                .sum()
                .item()
            )

            total += labels.size(0)

            if (
                batch_index % 50 == 0
                or batch_index == total_batches
            ):

                accuracy = (
                    100.0 *
                    correct /
                    total
                )

                print(
                    f"Batch "
                    f"{batch_index}/"
                    f"{total_batches} | "
                    f"Loss: "
                    f"{loss.item():.4f} | "
                    f"Accuracy: "
                    f"{accuracy:.2f}%",
                    flush=True
                )

        # =================================================
        # TRAINING RESULTS
        # =================================================

        train_loss = (
            running_loss /
            total
        )

        train_accuracy = (
            100.0 *
            correct /
            total
        )

        print(
            f"\nTrain Loss: "
            f"{train_loss:.4f}"
        )

        print(
            f"Train Accuracy: "
            f"{train_accuracy:.2f}%"
        )

        # =================================================
        # VALIDATION
        # =================================================

        model.eval()

        valid_loss = 0.0
        valid_correct = 0
        valid_total = 0

        with torch.no_grad():

            for batch in valid_loader:

                images = batch["image"]
                labels = batch["label"]

                images = images.to(device)
                labels = labels.to(device)

                outputs = model(images)

                loss = criterion(
                    outputs,
                    labels
                )

                valid_loss += (
                    loss.item() *
                    images.size(0)
                )

                predictions = outputs.argmax(
                    dim=1
                )

                valid_correct += (
                    (predictions == labels)
                    .sum()
                    .item()
                )

                valid_total += labels.size(0)

        validation_loss = (
            valid_loss /
            valid_total
        )

        validation_accuracy = (
            100.0 *
            valid_correct /
            valid_total
        )

        print(
            f"\nValidation Loss: "
            f"{validation_loss:.4f}"
        )

        print(
            f"Validation Accuracy: "
            f"{validation_accuracy:.2f}%"
        )

        # =================================================
        # SAVE BEST MODEL
        # =================================================

        if validation_accuracy > best_accuracy:

            best_accuracy = validation_accuracy

            torch.save(
                model.state_dict(),
                best_model_path
            )

            print(
                "\nBest model saved."
            )

        # =================================================
        # SAVE CHECKPOINT
        # =================================================

        torch.save(
            {
                "epoch": epoch,
                "model_state_dict":
                    model.state_dict(),

                "optimizer_state_dict":
                    optimizer.state_dict(),

                "best_accuracy":
                    best_accuracy,

                "train_accuracy":
                    train_accuracy,

                "validation_accuracy":
                    validation_accuracy
            },
            checkpoint_path
        )

        print(
            "Checkpoint saved."
        )

    return model

def save_model(
    model,
    class_names
):

    model_path = (
        MODEL_DIR /
        "crop_disease_model.pth"
    )

    classes_path = (
        MODEL_DIR /
        "classes.json"
    )


    torch.save(
        model.state_dict(),
        model_path
    )


    with open(
        classes_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            class_names,
            file,
            ensure_ascii=False,
            indent=4
        )


    print(
        "\nModel saved:"
    )

    print(model_path)

    print(
        "\nClasses saved:"
    )

    print(classes_path)
def test_model(
    model,
    test_loader,
    criterion
):

    model.eval()

    test_loss = 0.0
    correct = 0
    total = 0

    print("\n" + "=" * 60)
    print("TESTING MODEL")
    print("=" * 60)

    with torch.no_grad():

        for batch_index, batch in enumerate(
            test_loader,
            start=1
        ):

            images = batch["image"]
            labels = batch["label"]

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            loss = criterion(
                outputs,
                labels
            )

            test_loss += (
                loss.item() *
                images.size(0)
            )

            predictions = outputs.argmax(
                dim=1
            )

            correct += (
                (predictions == labels)
                .sum()
                .item()
            )

            total += labels.size(0)

            if (
                batch_index % 50 == 0
                or batch_index == len(test_loader)
            ):

                accuracy = (
                    100.0 *
                    correct /
                    total
                )

                print(
                    f"Test Batch "
                    f"{batch_index}/"
                    f"{len(test_loader)} | "
                    f"Accuracy: "
                    f"{accuracy:.2f}%",
                    flush=True
                )

    test_loss = test_loss / total

    test_accuracy = (
        100.0 *
        correct /
        total
    )

    print(
        f"\nTest Loss: "
        f"{test_loss:.4f}"
    )

    print(
        f"Test Accuracy: "
        f"{test_accuracy:.2f}%"
    )

    return test_accuracy

def main():

    # =====================================================
    # DATASET
    # =====================================================

    dataset = get_dataset()

    print("\nDataset columns:")
    print(dataset["train"].column_names)

    labels = sorted(
        set(
            dataset["train"]["label_name"]
        )
    )

    print(
        "\nNumber of classes:",
        len(labels)
    )


    # =====================================================
    # TRANSFORMS
    # =====================================================

    train_transform, test_transform = (
        create_transforms()
    )


    # =====================================================
    # TRAIN / VALIDATION SPLIT
    # =====================================================

    print("\nCreating Train / Validation split...")

    train_valid = dataset["train"].train_test_split(
        test_size=0.20,
        seed=SEED
    )

    train_data = train_valid["train"]

    valid_data = train_valid["test"]


    print(
        "Training images:",
        len(train_data)
    )

    print(
        "Validation images:",
        len(valid_data)
    )

    print(
        "Test images:",
        len(dataset["test"])
    )


    # =====================================================
    # PYTORCH DATASETS
    # =====================================================

    train_dataset = create_pytorch_dataset(
        train_data,
        train_transform
    )

    valid_dataset = create_pytorch_dataset(
        valid_data,
        test_transform
    )

    test_dataset = create_pytorch_dataset(
        dataset["test"],
        test_transform
    )


    # =====================================================
    # DATALOADERS
    # =====================================================

    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        collate_fn=collate_fn
    )

    valid_loader = DataLoader(
        valid_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        collate_fn=collate_fn
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        collate_fn=collate_fn
    )


    print("\nDataLoaders created.")


    # =====================================================
    # MODEL
    # =====================================================

    model = build_model(
        len(labels)
    )


    # =====================================================
    # LOSS
    # =====================================================

    criterion = nn.CrossEntropyLoss()


    # =====================================================
    # OPTIMIZER
    # =====================================================

    optimizer = torch.optim.AdamW(

        filter(
            lambda p: p.requires_grad,
            model.parameters()
        ),

        lr=LEARNING_RATE,

        weight_decay=1e-4
    )


    # =====================================================
    # TRAINING
    # =====================================================

    print("\n")
    print("=" * 60)
    print("STARTING TRAINING")
    print("=" * 60)

    train_model(
        model,
        train_loader,
        valid_loader,
        criterion,
        optimizer
    )


    # =====================================================
    # LOAD BEST MODEL
    # =====================================================

    best_model_path = (
        MODEL_DIR /
        "best_crop_disease_model.pth"
    )


    print(
        "\nLoading best validation model..."
    )


    model.load_state_dict(
        torch.load(
            best_model_path,
            map_location=device
        )
    )


    print(
        "Best model loaded."
    )


    # =====================================================
    # SAVE FINAL MODEL + CLASSES
    # =====================================================

    save_model(
        model,
        labels
    )


    # =====================================================
    # FINAL TEST
    # =====================================================

    print("\n")
    print("=" * 60)
    print("FINAL TEST")
    print("=" * 60)


    test_accuracy = test_model(
        model,
        test_loader,
        criterion
    )


    print(
        "\nFinal Test Accuracy:",
        f"{test_accuracy:.2f}%"
    )


if __name__ == "__main__":

    main()