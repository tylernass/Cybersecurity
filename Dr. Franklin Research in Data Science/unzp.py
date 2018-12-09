# Description: Script to open zipped files in a directory

import os, zipfile
loc = "/tartarus/tylernass" # In this location, there are n directories (where n = # of zip files)

# UNZIP SCRIPT
def zip():
     for i in os.listdir():
         if i[-7:] == "csv.zip":
                     zp = zipfile.ZipFile(i)
                     zp.extractall()
                
