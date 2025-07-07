#!/usr/bin/env ~/micromamba/envs/kret_312/bin/python
"""
Test script for the pybind11 example module.
This script demonstrates how to use the compiled C++ extension.
"""


def test_example_module():
    try:
        import example

        print("✓ Successfully imported the example module!")
    except ImportError as e:
        print(f"✗ Failed to import example module: {e}")
        print("Make sure you've compiled the extension first!")
        return False

    print("\n" + "=" * 50)
    print("Testing pybind11 example functions")
    print("=" * 50)

    # Test basic functions
    print("\n1. Testing add function:")
    result = example.add(5, 3)
    print(f"   add(5, 3) = {result}")
    assert result == 8, f"Expected 8, got {result}"

    print("\n2. Testing multiply_by_two function:")
    result = example.multiply_by_two(3.5)
    print(f"   multiply_by_two(3.5) = {result}")
    assert result == 7.0, f"Expected 7.0, got {result}"

    print("\n3. Testing greet function:")
    result = example.greet("World")
    print(f"   greet('World') = '{result}'")
    assert result == "Hello, World!", f"Expected 'Hello, World!', got '{result}'"

    print("\n4. Testing process_list function:")
    input_list = [1, 2, 3, 4, 5]
    result = example.process_list(input_list)
    expected = [1, 4, 9, 16, 25]
    print(f"   process_list({input_list}) = {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\n5. Testing Calculator class:")
    calc = example.Calculator(10.0)
    print(f"   Calculator(10.0).get_value() = {calc.get_value()}")
    assert calc.get_value() == 10.0

    calc.add(5.0)
    print(f"   After add(5.0): {calc.get_value()}")
    assert calc.get_value() == 15.0

    calc.multiply(2.0)
    print(f"   After multiply(2.0): {calc.get_value()}")
    assert calc.get_value() == 30.0

    calc.reset()
    print(f"   After reset(): {calc.get_value()}")
    assert calc.get_value() == 0.0

    print("\n" + "=" * 50)
    print("✓ All tests passed successfully!")
    print("=" * 50)
    return True


if __name__ == "__main__":
    success = test_example_module()
    if not success:
        exit(1)
