import os
import add
import commit
import revert
import GitInit
import diff
import GitLog

komande = {'init' : GitInit.init, 'add' : add.add, 'commit' : commit.commit, 
           'revert' : revert.revertToCommit, 'diff' : diff.diff, 'log' : GitLog.ReadLog}

def parser(komanda,repath = os.getcwd()):
    #Pretvara komandu u funkciju
    #Prima ukucanu komandu i put do repozitorijuma kao parametre
    
    operacija = komanda.split()
    operacija.append('')
    operacija.append('')
    
    if not operacija[0] in komande:
        print('Invalid command');
        return None;
    
    if operacija[0] == 'exit':
        return -1
    
    if operacija[1] == '':
       komande[operacija[0]]()
    elif operacija[2] == '':
        komande[operacija[0]](operacija[1])
    else:
        komande[operacija[0]](operacija[1], operacija[2])
        
