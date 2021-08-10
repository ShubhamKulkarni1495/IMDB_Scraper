import json,os
from task1 import *
task8=scrape_top_list()
def scrape_movie_id(b):
    for i in b:
        url=i["Url"][27:-1]+".json"
        if not(os.path.exists(url)):
            a=open(f"{url}","w+")
            c=json.dump(i,a,indent=4)
            a.close()
        else:
            print("file is already there")
scrape_movie_id(task8)