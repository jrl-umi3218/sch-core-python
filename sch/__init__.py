import os
if hasattr(os, 'add_dll_directory'):
    os.add_dll_directory("$<TARGET_FILE_DIR:sch-core::sch-core>")

from . sch import *
