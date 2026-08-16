from database import get_fish_by_name


def show_fish(fish_name):

    fish = get_fish_by_name(fish_name)

    if fish is None:
        print(f"\nFish '{fish_name}' not found.")
        return

    print("\n========================================")
    print("BIOFLOC FISH INFORMATION")
    print("========================================")

    print(f"Fish Name                 : {fish['fish_name']}")

    print(
        f"Temperature Range        : "
        f"{fish['min_temperature']} - "
        f"{fish['max_temperature']} °C"
    )

    print(
        f"pH Range                : "
        f"{fish['min_ph']} - "
        f"{fish['max_ph']}"
    )

    print(
        f"DO Range                : "
        f"{fish['min_do']} - "
        f"{fish['max_do']} mg/L"
    )

    print(
        f"Alkalinity Range        : "
        f"{fish['min_alkalinity']} - "
        f"{fish['max_alkalinity']} mg/L"
    )

    print(
        f"Stocking Density        : "
        f"{fish['recommended_stocking_density']} fish/m³"
    )

    print(
        f"Feeding Rate            : "
        f"{fish['feeding_rate']} % biomass/day"
    )

    print(
        f"Expected Growth         : "
        f"{fish['expected_growth']} g"
    )

    print(
        f"Culture Period          : "
        f"{fish['culture_period_days']} days"
    )

    print("========================================")


if __name__ == "__main__":

    fish_name = input("Enter fish name: ")

    show_fish(fish_name)