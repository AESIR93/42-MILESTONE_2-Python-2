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
    try:
        raise PlantError("Whatever plant error")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Whatever water error")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("Whatever plant error")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError("Whatever water error")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo === \n")
    test_plant_error()
    print("")
    test_water_error()
    print("")
    test_garden_error()
    print("")
    print("All custom error types work correctly!")
