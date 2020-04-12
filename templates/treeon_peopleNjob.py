import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
peoplenjob_url = f"https://www.peoplenjob.com/jobs?period=all&field=all&q=%EB%A7%88%EC%BC%80%ED%8C%85"

data = requests.get(peoplenjob_url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 크롤링 명칭
peoplenjob_startdate = soup.select("#content-main > div > table > tbody > tr > td.date")
peoplenjob_title = soup.select("#content-main > div > table > tbody > tr > td.job-title > a")
peoplenjob_position = soup.select("#content-main > div > table > tbody > tr > td.job_type > a")
peoplenjob_name = soup.select("#content-main > div > table > tbody > tr > td.name > a")
peoplenjob_rejion = soup.select("#content-main > div > table > tbody > tr > td:nth-child(5) > a")
peoplenjob_enddate = soup.select("#content-main > div > table > tbody > tr > td:nth-child(6) > span")


# 크롤링 내용
result = []

for item in zip(peoplenjob_startdate, peoplenjob_title, peoplenjob_position, peoplenjob_name, peoplenjob_rejion, peoplenjob_enddate):
    result.append({
        "시작일": item[0].text.strip(), 
        "제목": item[1].text.strip(), 
        "직종": item[2].text.strip(), 
        "이름": item[3].text.strip(), 
        "지역": item[4].text.strip(), 
        "마감일": item[5].text.strip()})
    print(result)