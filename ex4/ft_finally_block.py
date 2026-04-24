class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_garden_error() -> None:
    print("Testing catching all garden errors...")
    for error in [PlantError("The tomato plant is wilting!"),
                  WaterError("Not enough water in the tank! \n")]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plant_name: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_name:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(f".. ending test and returning to main {e}")
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering Systems ===\n")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print("\nCleanup always happens, even with errors!")
