# Description: Used to migrate ~25 .zip files from a central repository to an individual repository

import os
loc = "/tartarus/tylernass"
nw = "/tartarus/DATASETS/SmartMeterData"

def migrate(loc):
    for i in os.listdir():
        loc = loc + str(i)
        shutil.move("/tartarus/DATASETS/SmartMeterData", loc)

def crtdir(nw):
    a=0
    for i in range(0, 25):
        a += 1
        os.mkdir(nw + str(a))

