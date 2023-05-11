import sys, os

class IniFile():

    def __init__(self):
        #Initializes a void class
        self.refnum=None    #this is a reference pointing to the specific path indicated in OpenConfigData

    #Declaring private methods
    #this methods will only be available inside this class and not outside
    def __saveRefNum(self):
        pass


    #Declaring the interface
    #The user will have access to this public methods
    def OpenConfigData(self, path):
        #Gets only the reference for the file assossiated with path
        try:
            self.refnum=open(path,'w+')
        except FileNotFoundError :
            print("File not found! Please verify the path.")

    def readKey(self, sectionName, keyName, value):
        """
	    -section is the name of the section in which to write the specified key.
        -key is the name of the key to write.
        -value is the value to write to the key.
        -found? is TRUE if the VI found the key in the specified section.
        """
        pass

    def writeKey(self, sectionName, keyName, value):
        """
        -section is the name of the section in which to write the specified key.
        -key is the name of the key to write.
        -value is the value to write to the key.
        found? is TRUE if the VI found the key in the specified section.
        """
        pass

    def removeKey(self, sectionName, keyName):
        """
        section is the name of the section from which to remove the specified key.
        refnum is the reference number of the configuration data.
        key is the name of the key to remove.
        found? is TRUE if the VI found the key in the specified section.
        """
        pass

    def removeSection(self, sectionName):
        """
        section is the name of the section to remove.
        section exists? is TRUE if the VI found the specified section.
        """
        pass

    def CloseConfigData(self, writeFileIfChanged):
        """
        write file if changed (T) configures the VI to write the configuration data 
        to the platform-independent configuration file you specify with the Open Config Data VI.
        You must set write file if changed (T) to the default value of TRUE for the VI to write 
        the configuration data. If the value is FALSE, the VI does not write the configuration data.
        """
        if(writeFileIfChanged==True):
            self.__saveRefNum()
        
        self.refnum.close()

    def getKeyNames(self, sectionName):
        """
        section is the name of the section from which to get the key names.
        section exists? is TRUE if the VI found the specified section.
        """
        pass

    def getSectionNames(self):
        """
        Gets the names of all sections from the configuration data identified by refnum 
        """
        pass
