# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
cmake_minimum_required(VERSION 3.8)

project("C++")

# Include sub-projects.
add_subdirectory("Example")
add_subdirectory("VectorAndLoops")
add_subdirectory("MultiDVector")
add_subdirectory("ReadingTextFiles")
add_subdirectory("OneDimensionalRobot")
add_subdirectory("Gaussian")
add_subdirectory("Matrix")
add_subdirectory("HistogramFilter")
add_subdirectory("DeadCode")
add_subdirectory("IfStatements")
add_subdirectory("ForLoop")
add_subdirectory("IntermediateVariables")
add_subdirectory("VectorStorage")
add_subdirectory("References")
add_subdirectory("Static")
