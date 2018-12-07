# Description: Script to delete repeat files in a directory

# NOTE: To be run after files have been 1. Migrated (see migrate script) and 2.
import os
# loc = "/tartarus/tylernass/"
# Needs to be recursive
for i in os.listdir(:
    print(i)
    for j in os.i:
        if j[-3] == "zip":
            os.remove('%s' % i)
