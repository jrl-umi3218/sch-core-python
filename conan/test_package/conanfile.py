from conans import ConanFile, tools
import os
import subprocess

class SCHCorePythonTestConan(ConanFile):
    requires = "sch-core-python/1.0.0@gergondet/stable"

    def test(self):
      subprocess.check_call(['python', os.path.join(os.path.dirname(__file__), 'test.py')])
