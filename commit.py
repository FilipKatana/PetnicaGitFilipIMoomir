import os
import shutil
import add
import revert
import GitLog
import datetime
import getpass
import getLatestCommit

def getStagingArea(repository_path = os.getcwd):
    return repository_path + '/stgarea'

def commit(flag = ''):
    #Kopira sve iz staging area u backupove i brise sve fajlove koji nisu bili addovani
    #Na kraju trazi od korisnika da doda komentar i isti cuva u log.txt
    
    repository_path = os.getcwd()
    latestCommit = getLatestCommit.getLatestCommit()
    if latestCommit == None:
        print('Can not get latest commit')
        return None
    
    if(flag == '-a'):
        print('a');
        for the_file in os.listdir(repository_path):
            if not (the_file == '.backups') and (not the_file == 'stgarea') and (not the_file == 'log.txt') and (not the_file == '.newestcommit.txt'):
                add.add(the_file,repository_path)
                
    commitId = str(getLatestCommit.getLatestCommit() + 1)
    
    if not os.path.exists(revert.getBackupPath(repository_path) + '/' + commitId):
        print('Commit already exists')
        return None
    elif not os.path.existsgetStagingArea(repository_path):
        print('Staging area does not exist')
    elif not os.path.exists(repository_path + '/' + 'log.txt'):
        print('The log file does not exist')
        return None
    elif not os.path.exists(repository_path + '/.newestcommit.txt'):
        print('Can not store latest commit')
        return None
    
    commitPath = revert.getBackupPath(repository_path) + '/' + commitId
    os.mkdir(commitPath)
    for the_file in os.listdir(getStagingArea(repository_path)):
        add.copy(getStagingArea(repository_path) + '/' + the_file, commitPath + '/' + the_file)
        
    for the_file in os.listdir(getStagingArea(repository_path)):
        file_path = os.path.join(getStagingArea(repository_path), the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): 
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    if os.path.isdir(revert.getBackupPath(repository_path) + '/' + str(int(commitId) - 1)):        
        for the_file in os.listdir(revert.getBackupPath(repository_path) + '\\' + str(int(commitId) - 1)):
            if not(os.path.isdir(commitPath + '/'  + os.path.basename(the_file)) or os.path.isfile(commitPath + '/'  + os.path.basename(the_file))):
                add.copy(revert.getBackupPath(repository_path) + '/' + str(int(commitId) - 1) + '\\' + the_file, commitPath + '\\' + the_file)
    
    commitMsg = input("Type in your commit comment\n>")
    GitLog.WriteToLog(repository_path + '/' + 'log.txt', commitId, str(datetime.datetime.now()), getpass.getuser(), commitMsg)
    
    with open(repository_path + '/.newestcommit.txt','w') as LatestCommit:
        LatestCommit.write(commitId)

