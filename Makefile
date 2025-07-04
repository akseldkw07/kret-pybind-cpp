# Makefile for pybind11 example

# Detect the platform
UNAME_S := $(shell uname -s)

# Python executable
PYTHON ?= python3

# Compiler settings
CXX ?= g++
CXXFLAGS = -O3 -Wall -shared -std=c++14 -fPIC

# Python and pybind11 includes
PYTHON_INCLUDE = $(shell $(PYTHON) -m pybind11 --includes)
PYTHON_EXT_SUFFIX = $(shell $(PYTHON)-config --extension-suffix)

# Source and target
SRC = src/example.cpp
TARGET = example$(PYTHON_EXT_SUFFIX)

.PHONY: all clean test install dev-install

all: $(TARGET)

# Build the extension module
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(PYTHON_INCLUDE) $< -o $@

# Clean build artifacts
clean:
	rm -f example*.so example*.dylib example*.dll
	rm -rf build/ dist/ *.egg-info/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

# Install dependencies
install:
	$(PYTHON) -m pip install pybind11 setuptools wheel

# Development install
dev-install: install
	$(PYTHON) -m pip install pytest black isort autopep8 autoflake

# Build using setuptools
setup-build:
	$(PYTHON) setup.py build_ext --inplace

# Test the module
test: $(TARGET)
	$(PYTHON) test_example.py

# Help
help:
	@echo "Available targets:"
	@echo "  all          - Build the extension module"
	@echo "  clean        - Remove build artifacts"
	@echo "  install      - Install required dependencies"
	@echo "  dev-install  - Install development dependencies"
	@echo "  setup-build  - Build using setuptools"
	@echo "  test         - Run the test script"
	@echo "  help         - Show this help message"
