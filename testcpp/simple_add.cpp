#include <pybind11/pybind11.h>

namespace py = pybind11;

// 原有加法函数
double add(double a, double b) {
    return a + b;
}

std::string hello(const std::string& s) {
    return "receive: " + s;
}

PYBIND11_MODULE(simple_add, m) {
    m.doc() = "A simple module using pybind11 (UTF-8 string support)";
    m.def("add", &add, "Add two numbers", py::arg("a"), py::arg("b"));
    m.def("hello", &hello, "Take a string and return it with prefix", py::arg("input"));
}
