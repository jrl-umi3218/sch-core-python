#
# Copyright 2012-2019 CNRS-UM LIRMM, CNRS-AIST JRL
#

from eigen.c_eigen cimport Vector3d
from sva.c_sva cimport *

from c_sch cimport *

cdef extern from "sch_wrapper.hpp" namespace "sch":
  void transform(S_Object & obj, const PTransformd&)
  S_Object* Sphere(double)
  S_Object* Box(double, double, double)
  S_Object* STPBV(const string&)
  S_Object* Polyhedron(const string&)
  double distance(CD_Pair&, Vector3d& p1, Vector3d& p2)

