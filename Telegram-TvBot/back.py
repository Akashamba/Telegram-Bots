import json
import requests


def get_deets(name):
    deets = get_url("http://www.omdbapi.com/?apikey=56069cac&t="+name)
    js = json.loads(deets)
    return get_str(js)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_str(movie):
    for i in range(len(movie)):
        if movie[list(movie.keys())[i]] == "N/A":
            movie[list(movie.keys())[i]] = "Not Available"

    req = ['Title', 'Type', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot',
           'Language', 'Awards']
    l = []
    for i in range(len(req)):
        if req[i] == 'Type':
            l.append("\n" + str(req[i]) + " : " + str(movie[req[i]]).capitalize())
        else:
            l.append("\n" + str(req[i]) + " : " + str(movie[req[i]]))

    st = ""
    for i in range(len(l)):
        st = st + l[i] + "\n"
    return st + "\nFind more at imdb.com"


get_deets("contagion")

