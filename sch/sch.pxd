#
# Copyright 2012-2019 CNRS-UM LIRMM, CNRS-AIST JRL
#

cimport c_sch
from libcpp cimport bool as cppbool

cdef extern from "<memory>" namespace "std" nogil:
  cdef cppclass shared_ptr[T]:
    T* get()

cdef class S_Object(object):
  cdef c_sch.S_Object * impl
  cdef cppbool __own_impl

cdef S_ObjectFromPtr(c_sch.S_Object *)

cdef class CD_Pair(object):
  cdef c_sch.CD_Pair * impl

cdef class S_Polyhedron(S_Object):
  cdef c_sch.S_Polyhedron * poly

cdef S_Polyhedron S_PolyhedronFromPtr(shared_ptr[c_sch.S_Polyhedron])
