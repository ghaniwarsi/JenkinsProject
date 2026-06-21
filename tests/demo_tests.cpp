#include "demo_sdk.h"

#include <exception>
#include <iostream>
#include <stdexcept>
#include <string>

namespace {

void require(bool condition, const std::string& message) {
    if (!condition) {
        throw std::runtime_error(message);
    }
}

void test_add() {
    require(demo_sdk::add(2, 3) == 5, "add should return the sum of two integers");
    require(demo_sdk::add(-2, 2) == 0, "add should handle negative values");
}

void test_greeting() {
    require(demo_sdk::greeting("Build VM") == "Hello, Build VM!", "greeting should format the name");

    bool threw = false;
    try {
        demo_sdk::greeting("");
    } catch (const std::invalid_argument&) {
        threw = true;
    }

    require(threw, "greeting should reject an empty name");
}

} // namespace

int main() {
    try {
        test_add();
        test_greeting();
    } catch (const std::exception& error) {
        std::cerr << "Test failed: " << error.what() << '\n';
        return 1;
    }

    std::cout << "All demo SDK tests passed.\n";
    return 0;
}
