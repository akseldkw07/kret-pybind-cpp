#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <string>

// Simple function that adds two numbers
int add(int a, int b)
{
    return a + b;
}

// Function that multiplies a number by 2
double multiply_by_two(double x)
{
    return x * 2.0;
}

// Function that works with strings
std::string greet(const std::string &name)
{
    return "Hello, " + name + "!";
}

// Function that works with vectors
std::vector<int> process_list(const std::vector<int> &input)
{
    std::vector<int> result;
    for (int x : input)
    {
        result.push_back(x * x); // Square each element
    }
    return result;
}

// Class example
class Calculator
{
public:
    Calculator(double initial_value) : value(initial_value) {}

    void add(double x) { value += x; }
    void multiply(double x) { value *= x; }
    double get_value() const { return value; }
    void reset() { value = 0.0; }

private:
    double value;
};

// Pybind11 module definition
PYBIND11_MODULE(example, m)
{
    m.doc() = "pybind11 example plugin";

    // Export functions
    m.def("add", &add, "A function that adds two integers");
    m.def("multiply_by_two", &multiply_by_two, "A function that multiplies by 2");
    m.def("greet", &greet, "A function that greets someone");
    m.def("process_list", &process_list, "A function that squares list elements");

    // Export class
    pybind11::class_<Calculator>(m, "Calculator")
        .def(pybind11::init<double>())
        .def("add", &Calculator::add)
        .def("multiply", &Calculator::multiply)
        .def("get_value", &Calculator::get_value)
        .def("reset", &Calculator::reset);
}
