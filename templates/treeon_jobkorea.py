import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
jobkorea_url = f"http://www.jobkorea.co.kr/recruit/joblist?menucode=duty&dutyCtgr=10013"

data = requests.get(jobkorea_url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 크롤링 명칭
jobkorea_startdate = soup.select("#dev-gi-list > div > div.tplList.tplJobList > table > tbody > tr > td.odd > span.time.dotum")
jobkorea_title = soup.select("#dev-gi-list > div > div.tplList.tplJobList > table > tbody > tr > td.tplTit > div > strong > a")
jobkorea_position = soup.select("#dev-gi-list > div > div.tplList.tplJobList > table > tbody > tr > td.tplTit > div > p.dsc")
jobkorea_name = soup.select("#dev-gi-list > div > div.tplList.tplJobList > table > tbody > tr > td.tplCo > a")
jobkorea_rejion = soup.select("#dev-gi-list > div > div.tplList.tplJobList > table > tbody > tr > td.tplTit > div > p.etc > span:nth-child(3)")
jobkorea_enddate = soup.select("#dev-gi-list > div > div.tplList.tplJobList > table > tbody > tr > td.odd > span.date.dotum > span")

# 크롤링 내용
result = []

for item in zip(jobkorea_startdate, jobkorea_title, jobkorea_position, jobkorea_name, jobkorea_rejion, jobkorea_enddate):
    result.append({
        "시작일": item[0].text.strip(), 
        "제목": item[1].text.strip(), 
        "직종": item[2].text.strip(), 
        "이름": item[3].text.strip(), 
        "지역": item[4].text.strip(), 
        "마감일": item[5].text.strip()})
    print(result)