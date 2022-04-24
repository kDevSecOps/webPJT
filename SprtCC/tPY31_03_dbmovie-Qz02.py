# 14. Quiz_웹스크래핑 결과 이용하기
# 1) insert 연습하기 - 웹스크래핑 결과를 DB에 저장하기

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://mgDBusr:<password>@cluster0.bllxi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')


# # movies (tr들) 의 반복문을 돌리기
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         # rank = movie.select_one('td:nth-child(1) > img')['alt'] # img 태그의 alt 속성값을 가져오기
#         rank = movie.select_one('td.ac > img')['alt']    # img 태그의 alt 속성값을 가져오기
#         title = a_tag.text                                      # a 태그 사이의 텍스트를 가져오기
#         star = movie.select_one('td.point').text                # td 태그 사이의 텍스트를 가져오기
#         print(rank,title,star)

target_movie = db.movies.find_one({'title':'가버나움'})
target_star =target_movie['star']

movies = list(db.movies.find({'star':target_star}))

print(movies)

for movie in movies:
    print(movie['title'])