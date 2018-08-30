import difflib
import os
import revert
import getLatestCommit

def diff(file):
    #Kao parametar uzima ime fajla koji poredimo
    #Poredi ga sa njegovom verzijom u poslednjem komitu (potrebno je implementirati trazenje istog komita)
    
    latestCommit = str(getLatestCommit.getLatestCommit())
    if(os.path.exists(os.getcwd() + '/' + file) and os.path.exists(os.getcwd() + '/' + latestCommit + '/' + file)) and not latestCommit == None:
        with open(os.getcwd() + '/' + file, 'r') as first_file:
            with open(revert.getBackupPath(os.getcwd()) + '/' + latestCommit + '/' + file, 'r') as second_file:
                diff = difflib.unified_diff(first_file.readlines(), second_file.readlines(), fromfile = file + ' new', tofile = file + ' current',)
                for line in diff:
                    print(line)
    else:
        print('File does not exist at all or in the latest commit') 