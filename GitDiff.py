
import os



"""
The class Private contains functions only to
be used by this file.
"""
class Private:

    def ShowFileDiff(a, b):
        result = []

        for x in range(len(a)):
            if not(a[x] in b) and not(a[x] == ""):
                print("+ " + a[x])

        
        for x in range(len(b)):
            if not(b[x] in a) and not(b[x] == ""):
                print("- " + b[x])



"""
The function takes in commit1 and commit2 arguments, two names that
represent commit names in the hidden folder. It returns output that shows the difference between
the two. If an error occurs such as a non-existant commit, the function returns -1.
"""
def Diff(commit1, commit2):
    if not(os.path.exists(os.path.join(os.getcwd(), ".backups")) or
           os.path.exists(os.path.join(os.getcwd(), ".backups", commit1)) or
           os.path.exists(os.path.join(os.getcwd(), ".backups", commit1))):
        return -1

    

    path1 = os.path.join(os.getcwd(), ".backups", commit1)
    path2 = os.path.join(os.getcwd(), ".backups", commit2)

    for item in os.listdir(path1):
        if item in os.listdir(path2):
            print("---------------------------------------------")
            #print("In file '" + item + "':")
            #print("")
            f1 = open(os.path.join(path1, item), "r")
            f2 = open(os.path.join(path2, item), "r")
            Private.ShowFileDiff(f1.read().split("\n"), f2.read().split("\n"))
            f1.close()
            f2.close()

        else:
            print("")
            print("")
            print("New file: " + item)
                        






print(Diff("Malo", "Alo"))



    
