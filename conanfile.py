# -*- coding: utf-8 -*-
#
# Copyright 2012-2020 CNRS-UM LIRMM, CNRS-AIST JRL
#

from conans import python_requires

base = python_requires("Eigen3ToPython/latest@multi-contact/dev")

class SCHCorePythonConan(base.Eigen3ToPythonConan):
    name = "sch-core-python"
    version = "1.0.1"
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
    generators = ["cmake_find_package", "cmake_paths"]
    settings = "os", "arch", "compiler", "build_type"
    requires = (
        "SpaceVecAlg/latest@multi-contact/dev",
        "sch-core/latest@multi-contact/dev"
    )

    def package_info(self):
        self.env_info.PYTHONPATH.append(self._extra_python_path())
