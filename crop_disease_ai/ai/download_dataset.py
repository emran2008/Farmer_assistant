from datasets import load_dataset
from pathlib import Path


DATASET_NAME = "Saon110/bd-crop-vegetable-plant-disease-dataset"

OUTPUT_DIR = Path("dataset")


def main():

    print("=" * 60)
    print(" Bangladesh Crop Disease Dataset")
    print("=" * 60)

    print("\nDataset download শুরু হচ্ছে...")
    print("প্রথমবার কিছু সময় লাগতে পারে।\n")

    dataset = load_dataset(DATASET_NAME)

    print("\nDataset downloaded successfully.")

    print(dataset)

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print("\nDataset information:")

    for split_name, split_data in dataset.items():

        print(
            f"{split_name}: "
            f"{len(split_data)} images"
        )

    print("\nDataset প্রস্তুত।")


if __name__ == "__main__":
    main()