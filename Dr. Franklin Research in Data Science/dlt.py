# Description: Script to delete repeat files in a directory

def dlt():
    for i in os.listdir():
        if i[-3:] == "zip":
            os.remove(i) 
