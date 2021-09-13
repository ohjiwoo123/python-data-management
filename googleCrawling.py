from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time 

# 구글 접속 후 조코딩 검색 후 나오는 첫번째 사진 다운로드 코드

# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
# elem = driver.find_element_by_name("q")
# elem.send_keys("조코딩")
# elem.send_keys(Keys.RETURN)
# driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
# time.sleep(3)
# imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
# urllib.request.urlretrieve(imgUrl, "test.jpg")

# 반복문을 통해 검색 결과 모든 이미지 다운로드 (최대 50장)

# driver = webdriver.Chrome('/Users/jwoh/Desktop/python/chromedriver')
# driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
# elem = driver.find_element_by_name("q")
# elem.send_keys("outlet")
# elem.send_keys(Keys.RETURN)
# images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# count =1 
# for image in images : 
#     image.click()
#     time.sleep(3)
#     imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
#     urllib.request.urlretrieve(imgUrl, "IU" + str(count) + ".jpg")
#     count = count + 1 

# 반복문을 통해 검색 결과 모든 이미지 다운로드 (스크롤 내려서 50장 ++ 끝까지 다운로드 가능)

driver = webdriver.Chrome('/Users/jwoh/Desktop/python/tutorial-env/chromedriver4')
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("fire extinguisher")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height


images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count =1 
ouputPath = "/Users/jwoh/Desktop/python/tutorial-env/fire-extinguisher/"
for image in images : 
    try:
        image.click()
        time.sleep(1)
        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, ouputPath + "fire-extinguisher" + str(count) + ".jpg")
        count = count + 1 
    except: 
        pass
driver.close()