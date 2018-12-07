# Description: Script to open zipped files in a directory

import os, zipfile
loc = "/tartarus/tylernass"

a=0
def zip(x):
    global a
    a += 1
    for i in os.listdir(x):
        x = x + "/" + str(i) # This is the location of the files being looped through
        if i[-3:] == "zip" and i[-7:] != "csv.zip":
            zp = zipfile.ZipFile(x)
            zp.extractall(x)
        if i[-3:] == "csv" or i[-7:] == "csv.zip":
            zip("/tartarus/tylernass" + str(a))
        # zip(x)
        # for files in os.listdir(i):
        #     print(files)
        # # for root, dirs, files in os.walk("."):
        #     if files[-3:] == "zip":
        #         zp = zipfile.ZipFile(files)
        #         zp.extractall()


a=0

zip(loc)



def zip():
...     for i in os.listdir():
...             if i[-7:] == "csv.zip":
...                     zp = zipfile.ZipFile(i)
...                     zp.extractall()
