#!/usr/bin/env python3
"""
Demo script showing all the features of the pybind11 example module.
"""


def demo():
    try:
        import example

        print("🎉 Pybind11 Example Demo")
        print("=" * 30)

        # Basic functions
        print("\n📊 Function Examples:")
        print(f"  add(10, 15) = {example.add(10, 15)}")
        print(f"  multiply_by_two(7.5) = {example.multiply_by_two(7.5)}")
        print(f"  greet('Pybind11') = '{example.greet('Pybind11')}'")

        # List processing
        print("\n📋 List Processing:")
        numbers = [1, 2, 3, 4, 5]
        squared = example.process_list(numbers)
        print(f"  Input: {numbers}")
        print(f"  Squared: {squared}")

        # Class usage
        print("\n🧮 Calculator Class:")
        calc = example.Calculator(100.0)
        print(f"  Initial value: {calc.get_value()}")

        calc.add(25.0)
        print(f"  After adding 25: {calc.get_value()}")

        calc.multiply(1.5)
        print(f"  After multiplying by 1.5: {calc.get_value()}")

        # Interactive mode
        print("\n🎮 Interactive Mode (press Enter to skip):")
        try:
            a = input("  Enter first number (or press Enter for 10): ").strip()
            b = input("  Enter second number (or press Enter for 5): ").strip()

            a = float(a) if a else 10
            b = float(b) if b else 5

            result = example.add(int(a), int(b))
            print(f"  {int(a)} + {int(b)} = {result}")

        except (ValueError, KeyboardInterrupt):
            print("  Skipping interactive mode...")

        print("\n✨ Demo completed successfully!")

    except ImportError:
        print("❌ Could not import 'example' module.")
        print("   Make sure you've built the extension first:")
        print("   ./build.sh  or  python3 setup.py build_ext --inplace")


if __name__ == "__main__":
    demo()
