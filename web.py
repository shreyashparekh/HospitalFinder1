# import tabula

# df = ("D:/Desktop/portrait.pdf")
# output = ("D:/Desktop/test.csv")
# tabula.convert_into(df, output, output_format="csv", stream=True)

# from selenium import webdriver
# import pandas as pd
# driver = webdriver.Chrome('D:/Downloads/chromedriver_win32/chromedriver.exe')
# driver.get('https://www.fiverr.com/mountdesign/design-3-professional-logo-for-you-in-24-hours?context_referrer=logo_maker_banner&source=category_tree&ref_ctx_id=440fd5aeea59353470cb43e8a22eb18c&pckg_id=1&pos=1&context_type=rating&funnel=ac40e72a-1c3e-4808-a676-68fb73932fe7&seller_online=true')

# user_date = driver.find_elements_by_xpath('//*[@id="Comment_5561090"]/div/div[2]/div[2]/span[1]/a/time')[0]
# date = user_date.get_attribute('title')

# import os
# import selenium
# from selenium import webdriver
# import time
# from PIL import Image
# import io
# import requests
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import ElementClickInterceptedException


import requests
from bs4 import BeautifulSoup

# url = input("Enter URL: ")
page = requests.get('https://www.fiverr.com/timcvo?source=gig_cards&referrer_gig_slug=be-your-british-male-singer&ref_ctx_id=a17a22bb16bac39e071e85c01288660f')

soup = BeautifulSoup(page.content, 'html.parser')
head = soup.find('div', class_='username-line')  
foot = soup.find('div', id="perseus-app")
a = soup.find_all(id='perseus-app')
print(head)

print(foot)
print(a)