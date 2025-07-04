## PYBIND

### This is a repo containing a minimal pybind example. The initial goal is to define a simple C++ function and expose it to Python using pybind11.

## Project Structure

```
pybind/
├── src/
│   └── example.cpp          # C++ source code with functions and classes
├── setup.py                 # Python setuptools build configuration
├── Makefile                 # Build automation
├── test_example.py          # Python test script
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## Features

This example demonstrates:
- **Simple functions**: Basic arithmetic operations
- **String handling**: String manipulation functions
- **STL containers**: Working with std::vector
- **Classes**: C++ class exposure to Python
- **Type conversions**: Automatic conversion between Python and C++ types

## Installation and Setup

### 1. Install Dependencies

```bash
# Install required Python packages
pip install -r requirements.txt

# Or install manually
pip install pybind11 setuptools wheel
```

### 2. Compilation Options

You have several ways to compile the C++ extension:

#### Option A: Using Makefile (Recommended)
```bash
# Build the extension
make

# Or install dependencies and build
make install
make
```

#### Option B: Using setuptools
```bash
python setup.py build_ext --inplace
```

#### Option C: Manual compilation
```bash
# Get the correct flags
python -m pybind11 --includes

# Compile (example for macOS/Linux)
g++ -O3 -Wall -shared -std=c++14 -fPIC \
    $(python -m pybind11 --includes) \
    src/example.cpp \
    -o example$(python3-config --extension-suffix)
```

## Quick Start

The fastest way to get started:

```bash
# 1. Install dependencies
pip install pybind11

# 2. Build the extension
./build.sh

# 3. Test it
python3 test_example.py

# 4. Try the demo
python3 demo.py
```

## Testing

Run the test script to verify everything works:

```bash
# Using Make
make test

# Or directly
python test_example.py
```

Expected output:
```
✓ Successfully imported the example module!

==================================================
Testing pybind11 example functions
==================================================

1. Testing add function:
   add(5, 3) = 8

2. Testing multiply_by_two function:
   multiply_by_two(3.5) = 7.0

3. Testing greet function:
   greet('World') = 'Hello, World!'

4. Testing process_list function:
   process_list([1, 2, 3, 4, 5]) = [1, 4, 9, 16, 25]

5. Testing Calculator class:
   Calculator(10.0).get_value() = 10.0
   After add(5.0): 15.0
   After multiply(2.0): 30.0
   After reset(): 0.0

==================================================
✓ All tests passed successfully!
==================================================
```

## Usage Examples

After successful compilation, you can use the module in Python:

```python
import example

# Use functions
result = example.add(10, 20)
greeting = example.greet("Python")
squared_list = example.process_list([1, 2, 3, 4])

# Use classes
calc = example.Calculator(100.0)
calc.add(50.0)
calc.multiply(2.0)
value = calc.get_value()  # 300.0
```

## Platform-Specific Notes

### macOS
- Ensure you have Xcode command line tools: `xcode-select --install`
- The extension will have a `.so` suffix

### Linux
- Ensure you have build essentials: `sudo apt-get install build-essential`
- The extension will have a `.so` suffix

### Windows
- Requires Visual Studio or MinGW
- The extension will have a `.pyd` suffix

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure the extension is compiled and in the same directory
2. **Compiler not found**: Install appropriate development tools for your platform
3. **Python headers missing**: Install python-dev package on Linux
4. **pybind11 not found**: Run `pip install pybind11`

### Clean Build
```bash
make clean
make
```

## Advanced Usage

For more complex projects, consider:
- Using CMake for cross-platform builds
- Adding unit tests with pytest
- Setting up continuous integration
- Creating Python wheels for distribution