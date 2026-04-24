def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)\n")
    if 40 < temp:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)\n")
    return temp


def test_temperature(input_temp: str) -> None:
    print(f"Input data is '{input_temp}'")
    try:
        temp = input_temperature(input_temp)
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("All tests completed - program didn't crash!")
