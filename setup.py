import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Pythonspace",
        version = "1.0.0",
        description = "Python planet description generator",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Pythonspace2.py", base=base)])

