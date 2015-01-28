# coding: utf-8

tvdb_key = "4176B22AB48E79F6"
trackt_key = "fe1f0b78fae4e54f06e9c1a84dd4e2e9"
tmdb_key = "c5cccb4d1f13b38c6a98c9258bf0a2f7"


import os
import requests


a=os.listdir(os.path.expanduser("~/Media/Film"))

#Recuperare un file json dal web
r=requests.get("http://www.imdb.com/xml/find?json=1&nr=1&nm=on&q="+"RobinHood-UnUomoInCalzamaglia")
r.json()

#richiedere una password senza visualizzarla
from getpass import getpass
getpass("messaggio da mostrare")

#Elencare i file in una cartella
a=os.listdir(os.path.expanduser("~/Media/Film"))
b=[]
for i in a:
    b.append(i.split('.')[0])#Elimino le estensioni


######
#TvDB#
######
#Utilizzo di TvDB per ottenere le info sulle serie tv
import tvdb_api as tvdb
t = tvdb.Tvdb(language='it')#Setto la lingua italiana

a=os.listdir(os.path.expanduser("~/Media/Serie TV"))
t['Adventure Time']

for i in a:
    try:
        print i + str(t[i][1][5])
    except:
        print "ERROR %s" % i
        

t['bobs burgers']
t['i simpson'].search("La Paura Fa Novanta", key = 'episodename')
t['i simpson'].search("Gli Piace Volare E D'oh Lo Fa", key = 'episodename')
t['i simpson'].search("Gli Piace Volare", key = 'episodename')

#######
#trakt#
#######
#trackt. installare con: pip install git+https://github.com/z4r/python-trakt
import trakt.tv as tv
tv.setup(api_k)#settare l'api_key

#Ottengo la serie tv su trackt con l'id di TvDB
tv.show.summary(u'76580')['title']

j = []
for i in a:
    try:
        j.append(t[i]['id'])
    except:
        print "ERROR %s" % i
        
for i in j:
    try:
        print tv.show.summary(i)['title']
    except:
        print i


####
# tmdb
# To install: pip install git+https://github.com/doganaydin/themoviedb.git fuzzywuzzy
####
import tmdb
tmdb.configure(api-key)
movies=tmdb.Movies('Simpson')
movies=tmdb.Movies('fantozzi')
a=movies.get_best_match()
m = tmdb.Movie(a[1]['id'])
for m in movies.iter_results():
    print m['title'].encode('utf-8')

#####
# Mutagen
#####
from mutagen.easyid3 import EasyID3
a=EasyID3('/Volumes/Macintosh HD/andrea/JdownloaderScaricati/Violetta (2012)/08 Are you ready for the ride.mp3')
print a