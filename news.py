from bs4 import BeautifulSoup
import requests

#검색어 입력
# search = input("검색할 키워드를 입력해주세요:")
search = '서울 대학생 원룸'
#검색할 페이지 입력
page = int(input("크롤링할 페이지를 입력해주세요. ex)1(숫자만입력):")) # ex)1 =1페이지,2=2페이지...
print("크롤링할 페이지: ",page,"페이지")
#start수를 1, 11, 21, 31 ...만들어 주는 함수
page_num = 0

if page == 1:
    page_num =1
elif page == 0:
    page_num =1
else:
    page_num = page+9*(page-1)

#url 생성
url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page_num)
print("생성url: ",url)

# ConnectionError방지
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75" }

#html불러오기
original_html = requests.get(url, headers=headers)
html = BeautifulSoup(original_html.text, "html.parser")

# 검색결과
articles = html.select("div.group_news > ul.list_news > li div.news_area > a")
print(articles)
# 검색된 기사의 갯수
print(len(articles),"개의 기사가 검색됌.")

#뉴스기사 제목 가져오기
news_title = []
for i in articles:
    news_title.append(i.attrs['title'])
news_title

#뉴스기사 URL 가져오기
news_url = []
for i in articles:
    news_url.append(i.attrs['href'])
news_url

#뉴스기사 내용 크롤링하기
contents = []
for i in news_url:
    #각 기사 html get하기
    news = requests.get(i,headers=headers)
    news_html = BeautifulSoup(news.text,"html.parser")
    #기사 내용 가져오기 (p태그의 내용 모두 가져오기)
    contents.append(news_html.find_all('p'))

real_contents.append((contents))
