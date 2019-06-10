sch-core-python
===============

[![License](https://img.shields.io/badge/License-BSD%202--Clause-green.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Build Status](https://travis-ci.org/jrl-umi3218/sch-core-python.svg?branch=master)](https://travis-ci.org/jrl-umi3218/sch-core-python)
[![AppVeyor status](https://ci.appveyor.com/api/projects/status/0xoexolfeqxkgxye/branch/master?svg=true)](https://ci.appveyor.com/project/gergondet/sch-core-python/branch/master)
[ ![Download](https://api.bintray.com/packages/gergondet/multi-contact/sch-core-python%3Agergondet/images/download.svg) ](https://bintray.com/gergondet/multi-contact/sch-core-python%3Agergondet/_latestVersion)

Python bindings for [sch-core][core]. These bindings were initially part of
[Tasks][tasks] by @jorisv.

Installing
------

## Ubuntu LTS (14.04, 16.04, 18.04): PPA

Use the [multi-contact-unstable](https://launchpad.net/~pierre-gergondet+ppa/+archive/ubuntu/multi-contact-unstable) ppa:
```bash
sudo add-apt-repository ppa:pierre-gergondet+ppa/multi-contact-unstable
sudo apt-get update
sudo apt-get install python-sch-core python3-sch-core
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
