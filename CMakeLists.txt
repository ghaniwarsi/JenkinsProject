cmake_minimum_required(VERSION 3.20)

project(CppJenkinsDemo
    VERSION 1.0.0
    DESCRIPTION "Small C++ SDK-style project for learning Jenkins on Windows"
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(demo_sdk
    src/demo_sdk.cpp
)

target_include_directories(demo_sdk
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

add_executable(demo_cli
    app/main.cpp
)

target_link_libraries(demo_cli
    PRIVATE
        demo_sdk
)

add_executable(demo_tests
    tests/demo_tests.cpp
)

target_link_libraries(demo_tests
    PRIVATE
        demo_sdk
)

enable_testing()
add_test(NAME demo_tests COMMAND demo_tests)

install(TARGETS demo_sdk demo_cli
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
)

install(DIRECTORY include/ DESTINATION include)
