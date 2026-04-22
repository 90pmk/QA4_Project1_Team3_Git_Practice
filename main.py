import os
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

# ✅ 최신 크롬 드라이버 자동 업데이트
chromedriver_autoinstaller.install()

# Chrome WebDriver 실행  
driver = webdriver.Chrome()  
# 로그인 페이지 이동
driver.get("http://localhost:3000/login")

# 현재 페이지 제목 출력
print("현재 페이지 제목:", driver.title)

# 현재 URL 출력
print("현재 URL:", driver.current_url)


# ✅ 창이 닫히지 않도록 대기
input("Enter를 누르면 창이 닫힙니다...")
driver.quit()