import json
from task5 import *
task11=get_movie_list_details(url5)
def  analyse_movies_genre(movies):
    list1=[]
    genre_dic={}
    for i in movies:
        task11=i['genre']
        list1.append(task11)
    for k in list1:
        count=0
        for j in list1:
            if k==j:
                count+=1
        genre_dic[k]=count
    a=open("task111.json","w")
    b=json.dump(genre_dic,a,indent=4)
    a.close()
    return genre_dic
pprint(analyse_movies_genre(task11))