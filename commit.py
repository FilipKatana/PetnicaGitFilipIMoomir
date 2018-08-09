import os
import shutil
import add
import revert

def getStagingArea(repository_path):
    return repository_path + '\\stgarea'

def commit(repository_path, commitId):
    commitPath = revert.getBackupPath(repository_path) + '\\' + commitId
    os.mkdir(commitPath)
    for the_file in os.listdir(getStagingArea(repository_path)):
        print('prva')
        add.copy(getStagingArea(repository_path) + '\\' + the_file, commitPath + '\\' + the_file)
        
    for the_file in os.listdir(getStagingArea(repository_path)):
        file_path = os.path.join(getStagingArea(repository_path), the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): 
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    if os.path.isdir(revert.getBackupPath(repository_path) + '\\' + str(int(commitId) - 1)):        
        for the_file in os.listdir(revert.getBackupPath(repository_path) + '\\' + str(int(commitId) - 1)):
            if not(os.path.isdir(commitPath + '\\'  + os.path.basename(the_file)) or os.path.isfile(commitPath + '\\'  + os.path.basename(the_file))):
                add.copy(revert.getBackupPath(repository_path) + '\\' + str(int(commitId) - 1) + '\\' + the_file, commitPath + '\\' + the_file)
    
    revert.revertToCommit(repository_path, commitId)

#add.add('Folder', 'repozitorijum')
#commit('repozitorijum', '2')
revert.revertToCommit('repozitorijum', '1')
    
    
    
