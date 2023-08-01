#
# Copyright 2012-2019 CNRS-UM LIRMM, CNRS-AIST JRL
#

from libcpp.string cimport string

cdef extern from "<sch/S_Object/S_Object.h>" namespace "sch":
  cdef cppclass S_Object:
    S_Object()

cdef extern from "<sch/S_Polyhedron/S_Polyhedron.h>" namespace "sch":
  cdef cppclass S_Polyhedron(S_Object):
    S_Polyhedron()

cdef extern from "<sch/CD/CD_Pair.h>" namespace "sch":
  cdef cppclass CD_Pair:
    CD_Pair(S_Object*, S_Object*)
    double getDistance()
