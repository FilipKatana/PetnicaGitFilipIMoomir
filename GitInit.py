
"""
©This file has been made by Filip Katana for the purpose
of its usage in the git project. Any copying or unauthorised
selling of this file is strictly forbidden by law.
"""


import os

from subprocess import call


class private:
    def hide(folder_path):
        call(["attrib", "+H", folder_path])


    def unhide(folder_path):
        call(["attrib", "-H", folder_path])


"""
Function takes in no arguments and sets up the hidden folder
and the staging area folder titled stgarea inside the folder from which the
program was ran.
"""
def init():
    if os.path.exists(os.path.join(os.getcwd(), ".backups")):
        return -1
    os.mkdir(".backups")
    os.mkdir(os.path.join(os.getcwd(), "stgarea"))
    private.hide(os.path.join(os.getcwd(), ".backups"))



