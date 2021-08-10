import json,os,time,random
from task1 import *
task9=scrape_top_list()
def scrapping_time(b):
    j=0
    for i in b:
        url=i["Url"][27:-1]+".json"
        time.sleep(random.randint(2,3))
        if not(os.path.exists(url)):
            a=open(f"{url}","w+")
            c=json.dump(i,a,indent=4)
            a.close()
        else:
            print(j+1,"file is already there")
            j+=1
scrapping_time(task9)