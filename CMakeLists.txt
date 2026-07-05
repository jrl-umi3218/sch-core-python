#
# Copyright 2012-2026 CNRS-UM LIRMM, CNRS-AIST JRL
#

cmake_minimum_required(VERSION 3.22)

project(sch-core-python)
set(PROJECT_VERSION 1.0.7)

find_package(SpaceVecAlg REQUIRED NO_MODULE)
find_package(sch-core REQUIRED NO_MODULE)

get_directory_property(COMPILE_DEFINITIONS COMPILE_DEFINITIONS)

option(PYTHON_BINDING "Generate Python binding" ON)
option(DISABLE_TESTS "Disable unit tests." OFF)

configure_file(setup.in.py ${CMAKE_CURRENT_BINARY_DIR}/setup.py)

macro(ADD_BINDINGS PYTHON PYTHON_EXECUTABLE SOURCES)
  # Create the build directory
  set(SETUP_LOCATION "${CMAKE_CURRENT_BINARY_DIR}/${PYTHON}/$<CONFIGURATION>")
  if(DEFINED CMAKE_BUILD_TYPE)
    file(MAKE_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/${PYTHON}/${CMAKE_BUILD_TYPE}")
  else()
    foreach(CFG ${CMAKE_CONFIGURATION_TYPES})
      file(MAKE_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/${PYTHON}/${CFG}")
    endforeach()
  endif()
  # Copy the configured setup script there
  file(GENERATE
    OUTPUT "${SETUP_LOCATION}/setup.py"
    INPUT "${CMAKE_CURRENT_BINARY_DIR}/setup.py"
  )
  # Generate __init__.py
  file(GENERATE
    OUTPUT "${SETUP_LOCATION}/sch/__init__.py"
    INPUT "${PROJECT_SOURCE_DIR}/sch/__init__.py"
  )
  # Target to build the bindings
  set(TARGET_NAME sch-${PYTHON}-bindings)
  add_custom_target(${TARGET_NAME} ALL
    COMMAND ${CMAKE_COMMAND} -E chdir "${SETUP_LOCATION}" ${PYTHON_EXECUTABLE} setup.py build_ext --inplace
    COMMENT "Generating local sch-core ${PYTHON} bindings"
    DEPENDS ${SOURCES} SOURCES ${SOURCES}
  )
  # Copy sources
  set(I 0)
  foreach(SRC ${SOURCES})
    set(FILE_IN "${CMAKE_CURRENT_SOURCE_DIR}/${SRC}")
    set(FILE_OUT "${SETUP_LOCATION}/${SRC}")
    add_custom_target(copy-sources-${I}-${TARGET_NAME}
      COMMAND ${CMAKE_COMMAND} -E copy_if_different ${FILE_IN} ${FILE_OUT}
      DEPENDS ${FILE_IN}
    )
    add_dependencies(${TARGET_NAME} copy-sources-${I}-${TARGET_NAME})
    math(EXPR I "${I} + 1")
  endforeach()
  # Manual target to force regeneration
  add_custom_target(force-${TARGET_NAME}
    COMMAND ${CMAKE_COMMAND} -E chdir "${SETUP_LOCATION}" ${PYTHON_EXECUTABLE} setup.py build_ext --inplace --force
    COMMENT "Generating local sch-core ${PYTHON} bindings (forced)"
  )
  if(NOT ${DISABLE_TESTS})
    enable_testing()
    add_test(NAME test-${TARGET_NAME}
      COMMAND ${CMAKE_COMMAND} -E chdir "${SETUP_LOCATION}" ${PYTHON_EXECUTABLE} -m pytest
    )
  endif()
  # Install targets
  if(DEFINED PYTHON_DEB_ROOT)
    add_custom_target(install-${TARGET_NAME}
      COMMAND ${CMAKE_COMMAND} -E chdir "${SETUP_LOCATION}" ${PYTHON_EXECUTABLE} setup.py install --root=${PYTHON_DEB_ROOT} --install-layout=deb
      COMMENT "Install sch-core ${PYTHON} bindings (Debian layout)"
    )
  else()
    set(PIP_EXTRA_OPTIONS "--no-build-isolation")
    add_custom_target(install-${TARGET_NAME}
      COMMAND ${CMAKE_COMMAND} -E chdir "${SETUP_LOCATION}" ${PYTHON_EXECUTABLE} -m pip install . ${PIP_EXTRA_OPTIONS} --upgrade
      COMMENT "Install sch-core ${PYTHON} bindings"
    )
  endif()
  # Install requirements
  install(CODE "EXECUTE_PROCESS(COMMAND \"${CMAKE_COMMAND}\" --build \"${CMAKE_BINARY_DIR}\" --config \${CMAKE_INSTALL_CONFIG_NAME} --target install-${TARGET_NAME})")
endmacro()

set(BINDINGS_SOURCES
  include/sch_wrapper.hpp
  sch/c_sch.pxd
  sch/c_sch_private.pxd
  sch/sch.pxd
  sch/sch.pyx
  tests/test_sch.py
)

if(${PYTHON_BINDING})
  if(NOT DEFINED Python3_EXECUTABLE)
    # Look for the python3 currently available in the PATH environment
    find_program(Python3_EXECUTABLE python3)

    if(NOT Python3_EXECUTABLE)
      message(FATAL_ERROR "Could not find python3 executable in your environment PATH.")
    else()
      message(STATUS "Found Python interpreter: ${Python3_EXECUTABLE}")
    endif()
  endif()
  ADD_BINDINGS(python3 "${Python3_EXECUTABLE}" "${BINDINGS_SOURCES}")
else()
  enable_testing()
  install(CODE "message(\"Nothing to install\")")
endif()
