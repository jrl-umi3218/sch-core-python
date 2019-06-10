# -*- coding: utf-8 -*-
#
# Copyright 2012-2019 CNRS-UM LIRMM, CNRS-AIST JRL
#

from conans import python_requires
import subprocess

base = python_requires("Eigen3ToPython/1.0.0@gergondet/stable")

def get_python_version():
    # Get the version of the Python executable, not this one
    return '.'.join(subprocess.check_output('python -V'.split(), stderr = subprocess.STDOUT).strip().split()[1].decode().split('.')[0:2])

class SCHCorePythonConan(base.Eigen3ToPythonConan):
    name = "sch-core-python"
    version = "1.0.0"
    description = "Python bindings for the sch-core library"
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("robotics", "collision", "proximity", "convex", "python")
    url = "https://github.com/jrl-umi3218/sch-core-python"
    homepage = "https://github.com/jrl-umi3218/sch-core-python"
    author = "Pierre Gergondet <pierre.gergondet@gmail.com>"
    license = "BSD-2-Clause"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    exports = ["LICENSE"]      # Packages the license for the conanfile.py
    # Remove following lines if the target lib does not use cmake.
    exports_sources = ["CMakeLists.txt", "setup.in.py", "conan/CMakeLists.txt", "sch/*", "include/*", "tests/*"]
    generators = "cmake"
    options = { "python_version": ["2.7", "3.3", "3.4", "3.5", "3.6", "3.7"] }
    default_options = { "python_version": get_python_version() }
    settings = "os", "arch", "compiler", "build_type"

    requires = (
        "SpaceVecAlg/1.1.0@gergondet/stable",
        "sch-core/1.0.0@gergondet/stable"
    )

    def package_info(self):
        self.env_info.PYTHONPATH.append(self._extra_python_path())
