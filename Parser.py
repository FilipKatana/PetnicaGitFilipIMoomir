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
    
    if operacija[0] == 'commit':
        if operacija[1] == '-a':
            for the_file in os.listdir(repath):
                if not(the_file == '.backups' or the_file == 'stgarea'):
                    add.add(the_file,repath)
        komande[operacija[0]]()
    elif operacija[0] == 'revert':
        komande[operacija[0]](operacija[1], repath)
    elif operacija[0] == 'add':
        komande[operacija[0]](operacija[1],repath)
    elif operacija[1] == '':
       komande[operacija[0]]()
    else:
        komande[operacija[0]](operacija[1])
        

#parser('add tekst.txt','repozitorijum')
#parser('commit -a','repozitorijum')
#parser('revert 2','repozitorijum')
#komanda = input()
#parser(komanda, 'repo')
