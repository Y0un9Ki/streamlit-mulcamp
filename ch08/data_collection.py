#_*_ coding:utf-8 _*_
import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os

#
load_dotenv()

SERVICE_KEY = os.getenv('SEOUL_API_KEY')
print(SERVICE_KEY)

def main():
    data=None
    num_list=1
    while num_list<=3000:
        URL = f'http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/{num_list}/{num_list+999}/'
        # print(URL)
        num_list+=1000
        req=requests.get(URL)
        js=req.json()
        result=js['tbLnOpendataRtmsV']['row']
        df=pd.DataFrame(result)
        data=pd.concat([data, df])

    data.head()
    
if __name__=="__main":
    main()
