from task5 import *
import json
task10=get_movie_list_details(url5)
def scrape_director_details(movies):
    lang_dic={}
    for i in movies:
        for director in i['director']:
            lang_dic[director]={}
    for i in range(len(movies)):
        for director in lang_dic:
            if director in movies[i]['director']:
                for language in movies[i]['language']:
                    lang_dic[director][language]=0
    for i in range(len(movies)):
        for director in lang_dic:
            if director in movies[i]['director']:
                for language in movies[i]['language']:
                    lang_dic[director][language]+=1
    return lang_dic
    a=open("task100.json","w")
    b=json.dump(lang_dic,a,indent=4)
    a.close()
pprint(scrape_director_details(task10))