#include "dlc_core/array.h"
#include "dlc_core/dp.h"
#include "dlc_core/linked_list.h"
#include "dlc_core/math.h"
#include "dlc_core/stack.h"
#include "dlc_core/tree.h"
#include "dlc_core/vector.h"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(dlc_core, m) {
    m.doc() = "dlc";

    // Array functions
    m.def("productExceptSelf", &productExceptSelf, 
        "Product of array except self",
        py::arg("nums"));

    // You can add bindings for other functions here as they are needed
    // For example:
    // m.def("someFunction", &someFunction, "Description", py::arg("param"));
}
