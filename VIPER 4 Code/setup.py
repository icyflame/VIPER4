import sys
from cx_Freeze import setup, Executable

##Uncomment the following lines if it is a GUI application and you don't want the CONSOLE WINDOw.

base = None

if (sys.platform== "win32"):

	base = "win32GUI"

setup(
	name ="viper4.py" , 
	version = "0.1" , 
	description = "test" , 
	executables = [Executable("viper4.py",base=base)] 
       )

##The command line: c:\python32\python.exe setup.py build
##NOTE: first go to the python32 folder in command prompt.
##then use the command above.
