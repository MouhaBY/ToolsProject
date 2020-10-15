"""Fichier d'installation de notre script main.py."""

import sys

from cx_Freeze import setup, Executable

# # On appelle la fonction setup
# setup(
#     name="STOCK",
#     version="0.1",
#     description="Ce programme gère voter stock",
#     executables=[Executable("main.py")],
# )


#main
exe = Executable(script="main.py", base="Win32GUI")

buildOptions = dict(excludes=[], includes=[], packages=[], optimize=1)

setup(
    name = "TOOLS PROJECT by MBY",
    version = "1.0",
    description = "test",
    executables = [exe],
    options =dict(build_exe = buildOptions)
)