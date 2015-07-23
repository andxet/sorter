from media.Media import MediaFactory as mp
#import Config
from media import Media
import os.path as p
import sys

def sort():
    argv= sys.argv
    #Config.loadConfig()
    if len(argv) < 2:
        print "Utilizzo: [nome cartelle di origine]* nome cartella di destinazione"
        exit()
    
    if len(argv) == 2:
        paths = ['.']
    else:
        paths = argv[1:-1]
    
    
    Media.Paths.addRoot(paths)
    Media.Paths.setStore(argv[-1])
    mp.sortAll()

if __name__ == "__main__":
    sort()