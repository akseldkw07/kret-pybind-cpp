#!/bin/bash

# build_and_test.sh - Simple script to build and test the pybind11 example

set -e # Exit on any error

echo "🚀 Building and Testing Pybind11 Example"
echo "========================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is available
if ! command -v python3 &>/dev/null; then
    print_error "Python 3 is required but not found"
    exit 1
fi

print_status "Using Python: $(which python3)"
print_status "Python version: $(python3 --version)"

# Check if pybind11 is installed, install if not
if ! python3 -c "import pybind11" &>/dev/null; then
    print_warning "pybind11 not found, installing..."
    python3 -m pip install pybind11
    print_status "pybind11 installed successfully"
else
    print_status "pybind11 is already installed"
fi

# Clean any existing builds
print_status "Cleaning previous builds..."
rm -f example*.so example*.dylib example*.pyd
rm -rf build/ dist/ *.egg-info/

# Build the extension
print_status "Building C++ extension..."
if command -v make &>/dev/null; then
    make
else
    print_warning "Make not found, using setuptools..."
    python3 setup.py build_ext --inplace
fi

# Check if build was successful
if ls example*.so example*.dylib example*.pyd 1>/dev/null 2>&1; then
    print_status "Build successful! Extension file created."
else
    print_error "Build failed! No extension file found."
    exit 1
fi

# Run tests
print_status "Running tests..."
if python3 test_example.py; then
    echo ""
    print_status "🎉 All tests passed! Your pybind11 example is working correctly."
else
    print_error "Tests failed!"
    exit 1
fi

echo ""
print_status "You can now use the module in Python:"
echo "  python3 -c \"import example; print(example.add(5, 3))\""
