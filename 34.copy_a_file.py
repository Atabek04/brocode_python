# copyFile()  =  copies the content of a file
# copy()      =  copyFile() + permission mode + destination can be a directory
# copy2()     =  copy() + copies metadata

import shutil

shutil.copy("C:\\Users\\107\\Desktop\\text.txt", "C:\\Users\\107\\Desktop\\copy.txt") #src, dst
