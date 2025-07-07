from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir
import pybind11
from setuptools import setup, Extension

# Define the extension module
ext_modules = [
    Pybind11Extension(
        "example",  # Module name
        ["src/example.cpp"],  # Source files
        include_dirs=[
            # Path to pybind11 headers
            pybind11.get_include(),
        ],
        cxx_std=14,  # C++14 standard
    ),
]

setup(
    name="pybind_example",
    version="0.1.0",
    author="Your Name",
    author_email="akseldkw@example.com",
    description="A minimal pybind11 example",
    long_description="A simple example demonstrating pybind11 functionality",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.8",
)
