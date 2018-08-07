import shutil
import errno
 
def copy(src, dest):
#Kopira fajl ili direktorijum 
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        #Ako nije direktorijum onda je fajl
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)
def add(fileToAdd, repo):
    #Dodaje fajl u staging area
    #Parametri su fajl koji se dodaje i put do repozitorijuma
    copy(repo + '\\' + fileToAdd, repo + '\\stgarea' + '\\' + fileToAdd)     

