# CMakeList.txt : CMake project for Example, include source and define
# project specific logic here.
#
cmake_minimum_required(VERSION 3.8)

# Add source to this project's executable.
add_executable(HistogramFilterOptimization "main.cpp" "blur.cpp" "initialize_beliefs.cpp" "move.cpp" "normalize.cpp" "print.cpp" "sense.cpp" "zeros.cpp")

#set(CMAKE_CXX_FLAGS "-ofast ${CMAKE_C_FLAGS}")
#SET(GCC_COVERAGE_COMPILE_FLAGS "-ofast")
#add_definitions(${GCC_COVERAGE_COMPILE_FLAGS})
#SET(CMAKE_CXX_FLAGS  "${GCC_COVERAGE_COMPILE_FLAGS}")