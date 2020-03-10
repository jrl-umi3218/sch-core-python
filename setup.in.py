#
# Copyright 2012-2019 CNRS-UM LIRMM, CNRS-AIST JRL
#

from __future__ import print_function
try:
  from setuptools import setup
  from setuptools import Extension
except ImportError:
  from distutils.core import setup
  from distutils.extension import Extension

from Cython.Build import cythonize

import hashlib
import numpy
import os
import subprocess
import sys

win32_build = os.name == 'nt'

this_path  = os.path.dirname(os.path.realpath(__file__))
with open(this_path + '/sch/__init__.py', 'w') as fd:
    fd.write('from .sch import *\n')

sha512 = hashlib.sha512()
src_files = ['sch/c_sch_private.pxd', 'sch/sch.pyx', 'sch/c_sch.pxd', 'sch/sch.pxd', 'include/sch_wrapper.hpp']
src_files = [ '{}/{}'.format(this_path, f) for f in src_files ]
for f in src_files:
  chunk = 2**16
  with open(f, 'r') as fd:
    while True:
      data = fd.read(chunk)
      if data:
        sha512.update(data.encode('ascii'))
      else:
        break
version_hash = sha512.hexdigest()[:7]

class pkg_config(object):
  def __init__(self):
    self.compile_args = [ '-D' + x for x in '@COMPILE_DEFINITIONS@'.split(';') if len(x) ]
    self.compile_args += ['-std=c++11']
    if win32_build:
        self.compile_args.append('-DWIN32')
    self.include_dirs = [ x for x in '$<TARGET_PROPERTY:SpaceVecAlg::SpaceVecAlg,INTERFACE_INCLUDE_DIRECTORIES>;$<TARGET_PROPERTY:sch-core::sch-core,INTERFACE_INCLUDE_DIRECTORIES>'.split(';') if len(x) ]
    self.include_dirs.append('@Boost_INCLUDE_DIR@')
    self.include_dirs.append(this_path + '/include')
    self.include_dirs = filter(len, self.include_dirs)
    self.library_dirs = [ x for x in '$<TARGET_PROPERTY:sch-core::sch-core,LINK_FLAGS>'.split(';') if len(x) ]
    location = '$<TARGET_PROPERTY:sch-core::sch-core,LOCATION_$<CONFIGURATION>>'
    self.library_dirs.append(os.path.dirname(location) + "/../lib/")
    if "$<CONFIGURATION>".lower() == "debug":
        self.libraries = ['sch-core_d']
    else:
        self.libraries = ['sch-core']

configs = pkg_config()

def GenExtension(name, pkg, ):
  pyx_src = name.replace('.', '/')
  cpp_src = pyx_src + '.cpp'
  pyx_src = pyx_src + '.pyx'
  ext_src = pyx_src
  pkg.include_dirs=list(pkg.include_dirs)
  return Extension(name, [ext_src], extra_compile_args = pkg.compile_args, include_dirs = pkg.include_dirs + [numpy.get_include()], library_dirs = pkg.library_dirs, libraries = pkg.libraries)

extensions = [
  GenExtension('sch.sch', configs)
]

extensions = [ x for x in extensions if x is not None ]
packages = ['sch']
data = ['__init__.py', 'c_sch.pxd', 'sch.pxd']

cython_packages = [ x for x in packages if any([ext.name.startswith(x) for ext in extensions]) ]

extensions = cythonize(extensions)

setup(
    name = 'sch',
    version='@PROJECT_VERSION@-{}'.format(version_hash),
    ext_modules = extensions,
    packages = packages,
    package_data = { 'sch': data }
)
