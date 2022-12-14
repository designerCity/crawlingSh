# 블로그 내용 크롤링
## "검색 지역"의 해당 위치 (지오 코딩 전까지)

from selenium import webdriver
import time
 
# 크롬 웹브라우저 실행
path = "/Users/파일경로" # Chrome driver 가 있는 file 위치는 지정해줘야 한다.
driver = webdriver.Chrome(path)
url_list = []
content_list = ''
contents_list = []
text = "검색 단어"
 
for i in range(1, 300):  # 1~300페이지까지의 블로그 내용을 읽어옴
    url = 'https://section.blog.naver.com/Search/Post.nhn?pageNo='+ str(i) + '&rangeType=ALL&orderBy=sim&keyword=' + text
    driver.get(url)
    time.sleep(0.5)
 
    for j in range(1, 7): # 각 블로그 주소 저장
        titles = driver.find_element_by_xpath('/html/body/ui-view/div/main/div/div/section/div[2]/div['+str(j)+']/div/div[1]/div[1]/a[1]')
        title = titles.get_attribute('href')
        url_list.append(title)
 
print("url 수집 끝, 해당 url 데이터 크롤링")
 
for url in url_list: # 수집한 url 만큼 반복
    driver.get(url)  # 해당 url로 이동
 
    driver.switch_to.frame('mainFrame')
    overlays = ".se-viewer .se-section-placesMap .se-map-address" # 내용 크롤링
    
    contents = driver.find_elements_by_css_selector(overlays)
  
    for content in contents:
        content_list = content_list, content.text # content_list 라는 값에 + 하면서 점점 누적
        contents_list.append(content.text)
print('데이터 크롤이 완료되었습니다')

# print(content.text)
# print(contents_list)

import pandas as pd

df = pd.DataFrame()
for i in range(len(contents_list)):
    df.loc[i,'adr'] = contents_list[i]
  
df
df.to_csv('./저장 이름.csv', encoding='UTF-8')
