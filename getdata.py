import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
headers = {
    'authority': 'medigaku.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '^\\^Google',
}

response = requests.get('https://medigaku.com/2021-123/', headers=headers)
soup = bs(response.text,"html.parser")
data1 = soup.findAll('tr', style="height: 70px;")
data2 = soup.findAll('tr',style ="height: 71px;")
data = data1 + data2
data_raw = []
for i in range(1,len(data)):
    text_raw = data[i].findAll("td")
    for i in range(len(text_raw)):
        text_raw2 = text_raw[i].get_text()
        data_raw.append(text_raw2)
for i in data_raw:
    if len(i) < 2:
        data_raw.remove(i)
cot0 = []
cot1 = []
for i in range(0,len(data_raw)):
    if i%2 == 0 and data_raw[i].split("位")[0] != "":
        cot0.append(data_raw[i].split("位")[0])
for i in range(0,len(data_raw)):
    if i%2 != 0 and data_raw[i].split("月")[0] != "":
        cot1.append(data_raw[i].split("月")[0])
print(len(cot1))
cot2 = []
for i in range(0,len(data_raw)):
    if i%2 != 0 and data_raw[i].split("日") != "":
        temp = data_raw[i].split("日")[0]
        try:
             cot2.append(temp.split("月")[1])
        except:
            pass
percentile_list = pd.DataFrame(
    {'rank': cot0,
     'month': cot1,
     'day': cot2
    })
percentile_list.to_csv("lucky.csv",index=False)


