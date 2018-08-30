import os
import shutil
from add import copy
import commit

def getBackupPath(repositoryPath):
    #Vraca backups file
    return repositoryPath + '/.backups'
    
def revertToCommit(commitID,repository = os.getcwd()):
    #Kao parametar prima pud do repozitorijuma i sting u kom je broj komita na koji se vraca
    #Vraca repozitorijum u stanje nekog prošlog komita
       
    backupPath = getBackupPath(repository)
    
    if not(os.path.exists(backupPath)):
        print('Backup path not found (Repository does not exist)')
        return None
    elif  not(os.path.exists(repository)):
        print('Repository does not exist')
        return None
    elif  not(os.path.exists(backupPath + '/' + commitID)):
        print('Repository does not exist')
        return None
        
    #Brise working directory
    for the_file in os.listdir(repository):
        file_path = os.path.join(repository, the_file)
        try:
            if os.path.isfile(file_path) and (not(file_path == repository + '/log.txt')) and (not(file_path == repository + '/.newestcommit.txt')):
                os.unlink(file_path)
            elif os.path.isdir(file_path) and (not(file_path == backupPath)) and (not(file_path == commit.getStagingArea(repository))): 
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
           
    file_path = os.path.join(backupPath, commitID)
    for the_file in os.listdir(file_path):
        copy_path = os.path.join(file_path, the_file)
        copy(copy_path, repository + '/' + the_file) 
               
    
