# Description: Script to migrate files in a database

import os
loc = "/tartarus/tylernass"
nw = "/tartarus/DATASETS/SmartMeterData"

def migrate(loc):
    for i in os.listdir():
        loc = loc + str(i)
        shutil.move("/tartarus/DATASETS/SmartMeterData", loc)

def crtdir(nw):
    a=0
    for i in os.listdir():
        a += 1
        os.mkdir(nw + str(a))

