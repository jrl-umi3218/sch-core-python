#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eigen
import sva
import sch

from math import sqrt

sphere = sch.Sphere(0.1)
box = sch.Box(0.1, 0.1, 0.1)
box.transform(sva.PTransformd(eigen.Vector3d(0.2, 0, 0)))
pair = sch.CD_Pair(sphere, box)
print("Distance between sphere and box: {}".format(sqrt(pair.distance())))
