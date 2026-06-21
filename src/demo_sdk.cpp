#include "demo_sdk.h"

#include <stdexcept>

namespace demo_sdk {

int add(int left, int right) {
    return left + right;
}

std::string greeting(const std::string& name) {
    if (name.empty()) {
        throw std::invalid_argument("name must not be empty");
    }

    return "Hello, " + name + "!";
}

} // namespace demo_sdk
