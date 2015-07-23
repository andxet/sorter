from configobj import ConfigObj
import os.path as p

cm = null

def loadConfig(f='~/.sorter'):
    path = p.expanduser(f)
    cm=ConfigObj(path)
    
        

'''
from configobj import ConfigObj
import os.path as p
c = ConfigObj()
c.filename = p.expanduser('~/.configobj')

c['personaggio']={}
c['personaggio']['nome']='Hero'

c.write()

c2=ConfigObj('.configobj')

print c2['personaggio']['nome']'''