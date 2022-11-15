import os
if hasattr(os, 'add_dll_directory'):
    os.add_dll_directory("$<TARGET_FILE_DIR:sch-core::sch-core>")
    os.add_dll_directory("$<TARGET_FILE_DIR:Boost::serialization>")

from . sch import *
