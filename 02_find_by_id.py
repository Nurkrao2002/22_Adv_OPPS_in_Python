# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# class fbc():
#     def fbid(self):
#         driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
#         driver.maximize_window()
#         driver.find_element_by_id('login-input').send_keys('hd@josh')
#         time.sleep(5)
# g=fbc()
# g.fbid()


import time
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

class facebook():
    def fbid(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.facebook.com/')
        driver.maximize_window()
        driver.find_element_by_id('email').send_keys('Joshinnovations@gmail.com')
        driver.find_element_by_id('pass').send_keys('josh')
        driver.find_element_by_name('login').click()
        time.sleep(15)

a=facebook()
a.fbid()
