import os, sys
import os.path
from package.INIConfigFile import *

if __name__=='__main__':
    _path=os.getcwd()+'/ConfigFile/copie.ini'
    print("path : ", _path)


    file=IniFile()
    file.OpenConfigData(_path)
    #file.removeSection("owner")
    #file.removeSection("database")


    #print(file.readKey("owner","name"))
    #print(file.readKey("owner","organization"))

    #print(file.readKey("database","server"))
    #print(file.readKey("database","port"))
    #print(file.readKey("database","file"))
    
    #print(file.writeKey("database","file", '"payforfor.dat"'))
    #print(file.writeKey("database","port", 12))
    #print(file.writeKey("siteweb","site1", '"pypo.org"'))
    #print(file.removeSection("siteweb"))

    #print(file.readKey("database","file"))
    #print(file.removeKey("database","port"))
    #print(file.removeKey("database","file"))
    #print(file.readKey("database","file",'"not found"'))
    
    print(file.getSectionNames())
    print("KeyNames of [owner]:", file.getKeyNames("owner"))
    print("KeyNames of [database]:",file.getKeyNames("database"))

    file.CloseConfigData()
