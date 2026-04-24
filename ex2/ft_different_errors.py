def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        print("Testing operation 0...")
        int("abc")
    elif operation_number == 1:
        print("Testing operation 1...")
        8/0
    elif operation_number == 2:
        print("Testing operation 2...")
        open("/non/existent/file")
    elif operation_number == 3:
        print("Testing operation 3...")
        "abc" + 4
    else:
        print("Testing operation 4...")
        print("Operation completed successfully")


def test_error_types(operation_number: int) -> None:
    try:
        garden_operations(operation_number)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    test_error_types(4)
    print("\nAll error types tested successfully!")
