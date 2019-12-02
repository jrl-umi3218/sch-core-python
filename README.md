sch-core-python
===============

[![License](https://img.shields.io/badge/License-BSD%202--Clause-green.svg)](https://opensource.org/licenses/BSD-2-Clause)
[ ![Download](https://api.bintray.com/packages/gergondet/multi-contact/sch-core-python%3Agergondet/images/download.svg) ](https://bintray.com/gergondet/multi-contact/sch-core-python%3Agergondet/_latestVersion)
[![CI](https://github.com/jrl-umi3218/sch-core-python/workflows/CI%20of%20sch-core-python/badge.svg?branch=master)](https://github.com/jrl-umi3218/sch-core-python/actions?query=workflow%3A%22CI+of+sch-core-python%22)

Python bindings for [sch-core][core]. These bindings were initially part of
[Tasks][tasks] by @jorisv.

Installing
------

## Ubuntu LTS (16.04, 18.04, 20.04)

Note: the packaged version is the BSD-2-Clause library, if you require inter-penetration depth computation, you should build the library yourself.

```bash
# Make sure you have required tools
sudo apt install apt-transport-https lsb-release
# Add our key
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key 892EA6EE273707C6495A6FB6220D644C64666806
# Add our repository (stable versions)
sudo sh -c 'echo "deb https://dl.bintray.com/gergondet/multi-contact-release $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/multi-contact.list'
# Use this to setup the HEAD version
# sudo sh -c 'echo "deb https://dl.bintray.com/gergondet/multi-contact-release $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/multi-contact.list'
# Update packages list
sudo apt update
# Install packages
sudo apt install python-sch-core python3-sch-core
```

## Build from source

### Dependencies

* [sch-core][core]
* Python 2 or 3
* [Cython][cython]
* [SpaceVecAlg][sva] (including Python bindings)
* [Eigen 3][eigen] (including [Python bindings][eigenpython])

### Building

```sh
git clone --recursive https://github.com/jrl-umi3218/sch-core-python
cd sch-core-python
mkdir _build
cd _build
cmake [options] ..
make && make intall
```

#### CMake options

By default, the build will use the `python` and `pip` command to install the bindings for the default system version (this behaviour can be used to build the bindings in a given virtualenv). The following options allow to control this behaviour:

 * `PYTHON_BINDING` Build the python binding (ON/OFF, default: ON)
 * `PYTHON_BINDING_USER_INSTALL` Install using the `--user` switch (ON/OFF, default: OFF, ON for Windows)
 * `PYTHON_BINDING_FORCE_PYTHON2`: use `python2` and `pip2` instead of `python` and `pip`
 * `PYTHON_BINDING_FORCE_PYTHON3`: use `python3` and `pip3` instead of `python` and `pip`
 * `PYTHON_BINDING_BUILD_PYTHON2_AND_PYTHON2`: builds two sets of bindings one with `python2` and `pip2`, the other with `python3` and `pip3`
 * `DISABLE_TESTS` Disable unit tests building (ON/OFF, default: OFF)

[core]:      https://github.com/jrl-umi3218/sch-core
[cython]: http://cython.org/
[eigen]:     http://eigen.tuxfamily.org
[eigenpython]: https://github.com/jrl-umi3218/Eigen3ToPython
[sva]:       https://github.com/jorisv/SpaceVecAlg
[tasks]:     https://github.com/jorisv/Tasks
