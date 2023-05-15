IniConfigFile
=============

Developed by SIMAO Nedved  (c) 16-05-2023

Examples of How To Use the class
--------------------------------

 

Creating an INI File Object

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from INIConfigFile import*

_path=os.getcwd() #set the directory for the .ini file 


file=IniFile()    #Create a new instance of IniFile()
file.OpenConfigData(_path) #Open the .ini file pointed by _path

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Reading a key from a section

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(file.readKey("owner","name"))
print(file.readKey("owner","organization"))

print(file.readKey("database","server"))
print(file.readKey("database","port"))
print(file.readKey("database","file"))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Closing the object

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
file.CloseConfigData()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
