import os.path as p 
from ConfigParser import SafeConfigParser
import ConfigParser
import Media


config_path = p.expanduser('~/.sorter')
paths='paths'

def loadConfig():
    try:
        config=SafeConfigParser()
        if config.read(config_path) == []:
            raise NoOptionError("File .sorter non esistente")
        Media.Paths.addRoot(config.get(paths, 'source_folder'))
        Media.Paths.setStore(config.get(paths, 'destination_folder'))
    except Exception as e:
        config = createNew()
        print e
        print 'Modifica il file "~/.sorter" e specifica la cartella di destinazione.'
        exit()
        
    
def createNew():
    config=SafeConfigParser()
    config.add_section(paths)
    config.set(paths, 'source_folder', '')
    config.set(paths, 'destination_folder', '')
    with open(config_path, 'wb') as configfile:
        config.write(configfile)
    return config