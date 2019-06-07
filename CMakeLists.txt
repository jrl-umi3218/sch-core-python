#
# Copyright 2012-2019 CNRS-UM LIRMM, CNRS-AIST JRL
#

cmake_minimum_required(VERSION 2.8)

option(PYTHON_BINDING_USER_INSTALL "Install the Python bindings in user space" OFF)
option(DISABLE_TESTS "Disable unit tests." OFF)

set(PIP_EXTRA_OPTIONS "")
if(${PYTHON_BINDING_USER_INSTALL})
  set(PIP_EXTRA_OPTIONS "--user")
endif()

# Build the bindings locally
add_custom_target(sch-python-bindings ALL
  COMMAND python setup.py build_ext --inplace
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  COMMENT "Generating sch Python bindings"
  DEPENDS include/sch_wrapper.hpp
          sch/c_sch.pxd
          sch/c_sch_private.pxd
          setup.py
)

# Test the bindings
if(NOT ${DISABLE_TESTS})
  enable_testing()
  add_test(NAME schPythonBindingsTest
    COMMAND nosetests
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
endif()

# Install the bindings
add_custom_target(install-sch-python-bindings
  COMMAND pip install . ${PIP_EXTRA_OPTIONS}
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  COMMENT "Install sch Python bindings"
)
install(CODE "execute_process(COMMAND ${CMAKE_MAKE_PROGRAM} install-sch-python-bindings)")
