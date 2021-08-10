from requests import models
from  task5 import*
import json
task6=get_movie_list_details(url5)
movie_language={}
def analyse_movies_language(movies_list):
    language1=[]
    b=""
    for i in movies_list:
        c=b.join(i["language"])
        language1.append(c)
        movie_language [c]=language1.count(c)
    # pprint(movie_language)
    a=open("task66.json","w")
    b=json.dump(movie_language,a,indent=4)
    a.close()
analyse_movies_language(task6)