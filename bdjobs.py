from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
browser = webdriver.Chrome(chrome_options=chrome_options,
                           executable_path=r'D:\\1Softwares\\64\\seleniumwebdriver\\chromedriver_win32\\chromedriver.exe')

browser.get('https://www.bdjobs.com/')
search = browser.find_element_by_id('txtKeyword')
search.send_keys('python')
search.send_keys(Keys.ENTER)
