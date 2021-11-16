import sys
from cx_Freeze import setup, Executable


build_exe_options = {'packages': ['pygame','socket', 'pickle']
}

base = None
if sys.platform == "win32":
    base = "win32GUI"


setup(name='sang-kaghaz-gheychi',
 version = '1', 
 description = "python game project for tnb university", 
 options = {'build_exe': build_exe_options}, 
 executables = [
    Executable('server.py'), 
    Executable('client.py', base=base, icon='index.ico')]
)