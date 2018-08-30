import os

def getLatestCommit(repository_path = os.getcwd()):
    #Vraca id poslednjeg komita (kao string)
    #kao parametar uzima put do repozitorijuma (default je cwd)
    
    if os.path.exists(repository_path + '/.newestcommit.txt'):
        with open(repository_path + '/.newestcommit.txt','r') as LatestCommit:
            return int(LatestCommit.readline())
    else:
        print('Newest commit cannot be found (Repository probably does not exist)')
        return None