import os
import add
import commit
import revert

def init():
    return None


komande = {'init' : init, 'add' : add.add, 'commit' : commit.commit, 'revert' : revert.revertToCommit}

def parser(komanda,repath):
    #Pretvara komandu u funkciju
    #Prima ukucanu komandu i put do repozitorijuma kao parametre
    operacija = komanda.split()
    operacija.append('')
    operacija.append('')
    #print(operacija[0])
    #print(operacija[1])
   #if operacija[0] in komande:
        #print('da')
    if operacija[0] == 'commit':
        if operacija[1] == '-a':
            for the_file in os.listdir(repath):
                if not(the_file == '.backups' or the_file == 'stgarea'):
                    add.add(the_file,repath)
        komande[operacija[0]](repath,'2')
    elif operacija[0] == 'revert':
        komande[operacija[0]](repath, operacija[1])
    elif operacija[0] == 'add':
        komande[operacija[0]](operacija[1],repath)
    else:
       komande[operacija[0]](operacija[1])
        

#parser('add tekst.txt','repozitorijum')
#parser('commit -a','repozitorijum')
#parser('revert 2','repozitorijum')
    