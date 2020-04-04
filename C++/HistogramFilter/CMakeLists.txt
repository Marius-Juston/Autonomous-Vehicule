# CMakeList.txt : CMake project for Example, include source and define
# project specific logic here.
#
cmake_minimum_required(VERSION 3.8)

# Add source to this project's executable.
add_executable(HistogramFilter "tests.cpp" "simulate.cpp" "localizer.cpp" "helpers.cpp" "debugging_helpers.cpp")
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/maps/half_red.txt ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/maps/m1.txt ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/maps/m2.txt ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)