import os
import tempfile
from pathlib import Path
import os.path

class IniFile():
    def __init__(self):
        #Initializes a void class
        super().__init__()
        self.initialFilePosition=0
        self.setCommentCars()

    def setCommentCars(self, CommentList="; # // \t"):
        """
        These are the caracters used to work as comments in the INI File
        """
        self.comment=CommentList
    #Declaring private methods
    #this methods will only be available inside this class and not outside

    def __FindComments(self, _text):
        """
        After a first split with the key-value separateur, the comment takes the value after the separateur caracter
        and do the evaluation on the second element of the list comming from the split("=")
        """
        found=True
        commentCar_list=self.comment.split(" ")

        for comment in commentCar_list:
            if comment in _text:
                #_text=_text.replace(" ", "")
                #print("split : ", temp_key[1].split(";"))

                #_text=_text.strip(" ")
                text_list=_text.split(comment)
                return found, text_list[0]
        
        return not found, _text
    
    def __GetComment(self, _text):

        commentCar_list=self.comment.split(" ")

        for comment in commentCar_list:
            if comment in _text:
                #_text=_text.replace(" ", "")
                text_list=_text.split(comment)
                return comment, text_list[1]
        
        return  " "," "


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
            self._path=path
            self.refnum=open(path,"r+")
            self.NiDict={} #the key is the position in bytes of the value (value is the ni file section name)
            self.initialFilePosition=self.refnum.tell()

            tmp=self.getSectionNames()

        

        except FileNotFoundError :
            print("File not found! Please verify the path.")

    def readKey(self, sectionName, keyName, defaultValue=-1):
        """
        -section is the name of the section from which to read the specified key.
        -key is the name of the key to read.
        -default value is the value to return if the VI does not find the key in the specified section or if an error occurs.
        -found? is TRUE if the VI found the key in the specified section.
        -value is the value of the key.
        """

        self.__goToBegin()
        if (sectionName in self.getSectionNames()):
            self.refnum.seek(self.NiDict[sectionName]) #entered in the section specified

            for key in self.refnum:
                #print(key)
                #key=key.replace(" ","")
                key=key.strip(" ")
                key=key.strip("\n")
                if('=' in key):
                    key=key.split("=") #Gives a list containing the key and the value

                    #evaluating the split
                    found, key[1]=self.__FindComments(key[1].strip(" "))


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

        self.__goToBegin()

        try:
            with tempfile.TemporaryDirectory() as td:
                f_name = os.path.join(td, 'tempFileNi.ini')

                with open(f_name, 'a+') as fh:
                    for line in self.refnum:
                        line=line.strip('\n')
                        #print(line)

                        if(('=' in line)):
                            temp_key=line.split("=")
                            #print("key", temp_key)
                            #if there is = in the line
                            #then look for comments too
                            key_name=temp_key[0].strip(" ")
                            #print("split : ", temp_key[1].split(";"))
                            found, key_value=self.__FindComments(temp_key[1])

                            if((temp_key[0].strip(" ")==keyName) or (temp_key[0]==keyName) or key_name==keyName):
                                if(found):
                                    comment_car, comment=self.__GetComment(temp_key[1])
                                    #write key is done diferently
                                    #print("{0:} = {1:}".format(temp_key[0], value))
                                    fh.write("{0:} = {1:}{2:}{3:}\n".format(key_name, value, comment_car, comment))
                                else:
                                    fh.write("{0:} = {1:}\n".format(key_name, value))
                                    #fh.write("{0:} = {1:}{2:}{3:}\n".format(key_name, value))
                            else:
                                #print("{0:} = {1:}".format(temp_key[0], temp_key[1]))
                                #fh.write("{0:} = {1:}\n".format(key_name, temp_key[1].strip(" ")))
                                fh.write(line+"\n")

                        else:
                            #print(line)
                            fh.write(line+"\n")

                        #data from src has been copied to dst
                        #now we do the copy back
                with open(f_name,'r') as fh:
                    class_file=open(self._path,'w')
                    class_file.seek(0)
                    for tempFile in fh:
                        class_file.write(tempFile)
                        
            return True
            
        except Exception:
            return False
        finally:
            pass
            #The os.fdopen wraps the file descriptor in a Python file object, that closes automatically 
            #when the with exits. The call to os.remove deletes the file when no longer needed.
            
        

    def removeKey(self, sectionName, keyName):
        """
        section is the name of the section from which to remove the specified key.
        refnum is the reference number of the configuration data.
        key is the name of the key to remove.
        found? is TRUE if the VI found the key in the specified section.
        """

        self.__goToBegin()

        #fd, path = tempfile.mkstemp(suffix=".ini")
        #path=path_dir+'/tmp.ini'
        try:
            keyRemoved=False
            with tempfile.TemporaryDirectory() as td:
                f_name = os.path.join(td, 'tempFileNi.ini')

                with open(f_name, 'a+') as fh:
                    for line in self.refnum:
                        line=(line.strip('\n')).strip(" ")

                        if(('=' in line)):
                            temp_key=line.split("=")

                            #print(self.__FindComments(temp_key[1]))
                            if(temp_key[0].strip(" ")==keyName or temp_key[0]==keyName):
                                keyRemoved=True
                                #dont write this key in the file
                                continue
                            else:
                                fh.write(line+"\n")

                        else:
                            fh.write(line+"\n")

                        #data from src has been copied to dst
                        #now we do the copy back
                with open(f_name,'r') as fh:
                    class_file=open(self._path,'w')
                    class_file.seek(0)
                    for tempFile in fh:
                        class_file.write(tempFile)
                
            return keyRemoved
            
        except Exception:
            return False
        finally:
                self.__goToBegin()
            #The os.fdopen wraps the file descriptor in a Python file object, that closes automatically 
            #when the with exits. The call to os.remove deletes the file when no longer needed.
            
        


    def removeSection(self, sectionName):
        """
        section is the name of the section to remove.
        section exists? is TRUE if the VI found the specified section.
        """

        try:
            #start by removing each key
            keys=self.getKeyNames(sectionName)
            names=self.getSectionNames()

            for i in keys:
                self.removeKey(sectionName, i)
            self.__goToBegin()

            #than remove the section
            sectionRemoved=False
            doWrite=True
            
            
            with tempfile.TemporaryDirectory() as td:
                f_name = os.path.join(td, 'tempFileNi.ini')

                with open(f_name, 'w') as fh:
                    for line in self.refnum:
                        line=line.strip("\n")
                        doWrite=True

                        #find section
                        for section in names:
                            formated_pattern="[{0:}]".format((section.strip("\n")))
                            formated_pattern=formated_pattern.strip("\n")

                            if((formated_pattern in line) and (sectionName == section)):
                                sectionName=True
                                doWrite=False
                                break
                        
                        if(doWrite):
                            #print(line)
                            fh.write(line+"\n")

             
                #data from src has been copied to dst
                #now we do the copy back

                
                with open(f_name,'r') as fh:
                    class_file=open(self._path,'w')
                    class_file.seek(0)
                    for tempFile in fh:
                        class_file.write(tempFile)
                

            #self.NiDict.pop(sectionName)
            return sectionRemoved
            
        except Exception:
            return False
        finally:
            pass
            #The os.fdopen wraps the file descriptor in a Python file object, that closes automatically 
            #when the with exits. The call to os.remove deletes the file when no longer needed.
            
    

    

    def getKeyNames(self, sectionName):
        """
        section is the name of the section from which to get the key names.
        section exists? is TRUE if the VI found the specified section.
        """
        break_section=self.getSectionNames()
        keyNames=[]

        self.__goToBegin()

        if (sectionName in self.getSectionNames()):
            self.refnum.seek(self.NiDict[sectionName]) #entered in the section specified

            for key in self.refnum:
                #check if we havent reached the next section (marked with a "\n" caracter)
                if((key != "\n")):#if it haven't find a newline than do
                    key=key.strip('\n')
                    found, key=self.__FindComments(key)

                    if(('=' in key) and (not '[' in key) and (not ']' in key)):
                            temp_key=key.split("=")
                            keyNames.append(temp_key[0].strip(" "))
                else:
                    break

        return keyNames

    def getSectionNames(self):
        """
        Gets the names of all sections from the configuration data identified by refnum 
        """

        self.NiDict={}
        trackPosition=0
        sectionName=""
        right_brack=']'
        left_brack='['
        count_line=self.initialFilePosition
        self.__goToBegin()
 
        stop=False
        while(not stop):
            line=self.refnum.readline()
            if(line):
                line=line.strip("\n")
                if (left_brack in line) and (right_brack in line):
                    trackPosition=self.refnum.tell()
                    #print("key position : ", trackPosition)
                    found, line=self.__FindComments(line)
                    line=line.replace("["," ")
                    line=line.replace("]"," ")
                    #line=line.strip("[")
                    #line=line.strip("]")
                    sectionName=line.replace(" ","").strip("")
                    self.NiDict.update({sectionName:trackPosition})
            else:
                stop=True
        
        #position the cursor in the begginning once more
        #self.refnum.seek(self.initialFilePosition)
        self.__goToBegin()
        
        return self.NiDict.keys()

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
    


if __name__=='__main__':
    #_path="/Users/happyuser/Documents/GitProjects/ConfigFileINI/example.ini"
    _path=os.getcwd()+'/copie.ini'


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
