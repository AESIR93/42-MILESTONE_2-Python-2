def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature(input_temp: str) -> None:
    try:
        temp = input_temperature(input_temp)
        print(f"Temperature is now {temp}°C")
    except ValueError:
        print("Caught input_temperature error: invalid literal for "
              f"int() with base 10: '{input_temp}'")
    finally:
        print("Program still runs")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    input_temp = "25"
    print(f"Input data is '{input_temp}'")
    test_temperature(input_temp)
    print("")
    input_temp_2 = "abc"
    print(f"Input data is '{input_temp_2}'")
    test_temperature(input_temp_2)
