ConfigFileINI
=============

An INI File or initialization file is widely used to initialize operational
systems, applications and anything that needs to load any predefined parameters
from the memory.

This simple class allows any developer to be capable to retrive data from an INI
File. The methods and the constructors are :

 

|                                                | Type              | Description                                                                                              |
|------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------------------|
| IniFile()                                      | Class Constructor | Create a new object from the IniFile() template                                                          |
| setCommentCars(ListOfCommentCars)              | Class Method      | specify the caracters set to indicate a comment in the INI File (the default caracters are "; \# // \t"  |
| OpenConfigData(path)                           | Class Method      | Open the INI File from the path you specify                                                              |
| readKey(sectionName, keyName, defaultValue=-1) | Class Method      | Read the value of a key within the section specified                                                     |
| writeKey(sectionName, keyName, value)          | Class Method      | Write or change the value of a key within the section specified                                          |
| removeKey(sectionName, keyName)                | Class Method      | Remove the line in the section where "KeyName" shows up                                                  |
| removeSection(sectionName)                     | Class Method      | Remove the all section with its keys                                                                     |
| getKeyNames(sectionName)                       | Class Method      | Returns the keys with a section of the INI File                                                          |
| getSectionNames()                              | Class Method      | Returns the SectionNames within the INI File                                                             |
| CloseConfigData(writeFileIfChanged=False)      | Destructor        | Release memory of the created object                                                                     |

 
