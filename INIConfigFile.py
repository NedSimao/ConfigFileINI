import sys, os
import re


class IniFile():
    def __init__(self):
        #Initializes a void class
        super().__init__()
        self.initialFilePosition=0

    #Declaring private methods
    #this methods will only be available inside this class and not outside
    def __saveRefNum(self):
        pass

    def __goToBegin(self):
        self.refnum.seek(self.initialFilePosition)


    #Declaring the interface
    #The user will have access to this public methods
    def OpenConfigData(self, path):
        #Gets only the reference for the file assossiated with path
        try:
             #this is a reference pointing to the specific path indicated in OpenConfigData
            self.refnum=open(path,"r")
            #line=self.refnum
            #print("self.refnum=", self.refnum)
            self.NiDict={} #the key is the position in bytes of the value (value is the ni file section name)
            self.initialFilePosition=self.refnum.tell()
            trackPosition=0
            sectionName=""
            right_brack=']'
            left_brack='['
            count_line=self.initialFilePosition
            
            stop=False
            while(not stop):
                line=self.refnum.readline()
                if(line):
                    line=line.strip("\n")
                    #print(line)
                    if (left_brack in line) and (right_brack in line):  
                        trackPosition=self.refnum.tell()
                        #print("key position : ", trackPosition)
                        sectionName=line.strip("[]")
                        self.NiDict.update({sectionName:trackPosition})
                else:
                    stop=True
        
            #position the cursor in the begginning once more
            #self.refnum.seek(self.initialFilePosition)
            self.__goToBegin()

        

        except FileNotFoundError :
            print("File not found! Please verify the path.")

    def readKey(self, sectionName, keyName, defaultValue):
        """
        -section is the name of the section from which to read the specified key.
        -key is the name of the key to read.
        -default value is the value to return if the VI does not find the key in the specified section or if an error occurs.
        -found? is TRUE if the VI found the key in the specified section.
        -value is the value of the key.
        """

        self.comment_patterns=[';','#']
        self.skip_patterns=["\n"," "]

        self.__goToBegin()
        if (sectionName in self.getSectionNames()):
            self.refnum.seek(self.NiDict[sectionName]) #entered in the section specified
            for key in self.refnum:
                key=key.strip("\n")
                if('=' in key):
                    key=key.strip(" ")
                    key=key.split("=") #Gives a list containing the key and the value
                    

                    if(keyName == key[0%2].strip(" ")):
                                return key[1%2].strip(" ")
            return defaultValue
                
                
                    

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

    def CloseConfigData(self, writeFileIfChanged=False):
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
        return self.NiDict.keys()
    


if __name__=='__main__':
    #_path="/Users/happyuser/Documents/GitProjects/ConfigFileINI/example.ini"
    _path=os.getcwd()+'/copie.ini'
    print(_path)


    file=IniFile()
    file.OpenConfigData(_path)
    print(file.readKey("database","file", 1))
    print(file.getSectionNames())
    file.CloseConfigData()
