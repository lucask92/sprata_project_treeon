import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.projectTreeon                      # 'dbsparta'라는 이름의 db를 만듭니다.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
wanted_url = f"https://www.wanted.co.kr/wdlist/523?country=kr&job_sort=job.latest_order&years=-1&locations=all"

data = requests.get(wanted_url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 크롤링 명칭
# wanted_startdate = soup.select("")
wanted_title = soup.select("#__next > div > div._1yHloYOs_bDD0E-s121Oaa > div._2y4sIVmvSrf6Iy63okz9Qh > div > ul > li > div > a > div > dl")
#__next > div > div._1yHloYOs_bDD0E-s121Oaa > div._2y4sIVmvSrf6Iy63okz9Qh > div > ul > li > div > a > div > dl

# wanted_position = soup.select("")
# wanted_name = soup.select("")
# wanted_region = soup.select("")
# wanted_enddate = soup.select("#")
print(wanted_title)

# # 크롤링 내용
# result = []

# for item in zip(wanted_startdate, wanted_title, wanted_position, wanted_name, wanted_region, wanted_enddate):
#     result.append({
#         "시작일": item[0].text.strip(), 
#         "제목": item[1].text.strip(), 
#         "직종": item[2].text.strip(), 
#         "이름": item[3].text.strip(), 
#         "지역": item[4].text.strip(), 
#         "마감일": item[5].text.strip()})
#     print(result)