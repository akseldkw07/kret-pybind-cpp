#!/bin/bash

# build.sh - Simple reliable build script for the pybind11 example

set -e

echo "Building pybind11 extension..."

# Clean previous builds
rm -f example*.so example*.dylib example*.pyd
rm -rf build/ dist/ *.egg-info/

# Build using setuptools (most reliable method)
echo "Using setuptools to build..."
python3 setup.py build_ext --inplace

# Copy the extension to the current directory
echo "Copying extension file..."
find build -name "example*" -type f \( -name "*.so" -o -name "*.dylib" -o -name "*.pyd" \) -exec cp {} . \;

# Verify the extension was created
if ls example*.so example*.dylib example*.pyd 1>/dev/null 2>&1; then
    echo "✓ Build successful!"
    echo "Extension file: $(ls example*.so example*.dylib example*.pyd 2>/dev/null | head -1)"
else
    echo "✗ Build failed - no extension file found"
    exit 1
fi
