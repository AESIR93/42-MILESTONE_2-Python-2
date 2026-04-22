def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"Caught input_temperature error: {temp}°C is"
                         " too cold for plants (min 0°C)")
    if 40 < temp:
        raise ValueError(f"Caught input_temperature error: {temp}°C is"
                         " too hot for plants (max 40°C)")
    return temp


def test_temperature(input_temp: str) -> None:
    try:
        temp = input_temperature(input_temp)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        if "invalid literal" in str(e):
            print(f"Caught input_temperature error: {e}")
        else:
            print(e)
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
    print("")
    input_temp_3 = "100"
    print(f"Input data is '{input_temp_3}'")
    test_temperature(input_temp_3)
    print("")
    input_temp_4 = "-100"
    print(f"Input data is '{input_temp_4}'")
    test_temperature(input_temp_4)
