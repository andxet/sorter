from tvdb_api import Tvdb as tvbd

db = tvbd(language='it')
print db['griffin'][1][1]['episodename']

def by_title(title, year=""):
    q='http://www.omdbapi.com/?t=%s&y=%s' % (title, year)
    return get_json(q)

def by_id(idi):
    q='http://www.omdbapi.com/?i=%s' % idi
    return get_json(q)

def search_title(title, year=""):
    q='http://www.omdbapi.com/?s=%s&y=%s' % (title, year)
    return get_json(q)

def get_json(query):
    r=requests.get(query)
    return r.json()