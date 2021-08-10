from requests import models
from  task5 import*
import json
task7=get_movie_list_details(url5)
movie_director={}
def analyse_movies_directors(movies_list):
    director_movie=[]
    b=""
    for i in movies_list:
        c=b.join(i["director"])
        director_movie.append(c)
        movie_director [c]=director_movie.count(c)
    pprint(movie_director)
    a=open("task77.json","w")
    b=json.dump(movie_director,a,indent=4)
    a.close()
analyse_movies_directors(task7)