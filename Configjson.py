import os.path as p 
import json

class Config(object):
    cfgfile = p.expanduser("~/.sorter")
    __config = {}

    def __init__(self):
        cfgfile = p.expanduser("~/.sorter")
        try:
            with open(cfgfile, "r") as f_cfgfile:
                self.__config = json.loads(f_cfgfiles)
        except:
            cfg = {"media": {
                        "Video" : {"ext": ["flv", "avi", "mkv", "mp4"], "storepath": "Video/"},
                        "Document" : {"ext": ["pdf", "chm", "epub"], "storepath": "Documenti/"},
                        "Image" : {"ext": ["dmg", "iso", "mdf"], "class": "Image",  "storepath": "Immagini disco/"},
                        "Picture" : {"ext": ["jpg", "png", "gif", "jpeg"], "storepath": "Foto/"},
                        "Music" : {"ext": ["mp3", "flac"],  "storepath": "Musica/"},
                        "Subtitles": {"ext": ["srt"], "storepath": "Video/"},
                        "Archives": {"ext": ["7z", "zip", "rar"], "storepath": "Archivi/"},
                        "Ignore": {"ext": ["utpart", ".ds_store", ""], "storepath": "ignorati/"},
                        "Draft": {"ext": ["nfo", "txt", "diz"], "storepath": "monnezza/"},
                        "Comic": {"ext": ["cbr", "cbz"], "storepath": "Fumetti/"}
                        },
                    "path": {
                        
                    }
                    
            }
            with open(cfgfile, "w") as f_cfgfile:
                json.dump(cfg, f_cfgfile)
            self.__config = cfg
        print cfg

    def config(self):
        return self.__config