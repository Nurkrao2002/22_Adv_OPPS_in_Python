import time
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import  ChromeDriverManager

class gb():
    def fn(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element_by_name('login-input').send_keys('ham@hd')
        time.sleep(5)
g=gb()
g.fn()