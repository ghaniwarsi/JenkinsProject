#include "demo_sdk.h"

#include <iostream>

int main() {
    std::cout << demo_sdk::greeting("Jenkins") << '\n';
    std::cout << "2 + 3 = " << demo_sdk::add(2, 3) << '\n';
    return 0;
}
