
import os.path



"""
Takes in the name with the full path, the id, date and username and comment
Appends this comment entry to the file or creates it if the file doesn't exist
NOTE: id can be taken in as an integer initially, but not as a double or float
      The date should be entered as a string
"""
def WriteToLog(file_name = os.path.join(os.getcwd(), "log.txt"), idd, date, user, comment):
    idd = str(idd)
    if not(os.path.exists(file_name)):
        f = open(file_name, "w")
        f.write(idd + "," + date + "," + user + "," + comment + "\n")
    else:
        f = open(file_name, "a")
        f.write(idd + "," + date + "," + user + "," + comment + "\n")


"""
The function takes in the file name of the log and prints it out in a
presentable manner.
"""
def ReadLog(file_name = os.path.join(os.getcwd(), "log.txt")):
    if not(os.path.exists(file_name)):
        return -1

    f = open(file_name, "r")

    for line in reversed(f.read().split("\n")):
        entry = line.split(",")
        if len(entry) == 4:
            print("Id: " + entry[0] + ", Date: " + entry[1],
                  "Author: " + entry[2])
            print("Personal comment: " + entry[3])
            print("")


ReadLog("FF.txt")

    
