cmake_minimum_required(VERSION 2.8.12)
project(libfoo CXX)

file(GLOB_RECURSE SOURCES src/*.cpp)
file(GLOB_RECURSE HEADERS include/*.h)

include_directories(${PROJECT_SOURCE_DIR}/include)

add_library(libfoo SHARED ${SOURCES} ${HEADERS})
#target_link_libraries(libfoo someStaticLib)
