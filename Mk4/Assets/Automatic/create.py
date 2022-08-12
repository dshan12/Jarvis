import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config
from dotenv import load_dotenv
import time

load_dotenv()
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
web_driver = webdriver.Chrome("chromedriver.exe")


def create():
    folderName = str(sys.argv[1])
    os.makedirs(config.path + str(folderName))
    web_driver.get("https://github.com/")
    web_driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
    t1 = web_driver.find_element_by_id("login_field")
    t1.send_keys(config.username)
    t2 = web_driver.find_element_by_id("password")
    time.sleep(2)
    print("logged in")
    time.sleep(3)
    t2.send_keys(config.password)
    web_driver.find_element_by_xpath('// *[ @ id = "login"] / div[4] / form / input[14]').click()
    web_driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
    textbox = web_driver.find_element_by_xpath('//*[@id="repository_name"]')
    textbox.send_keys(folderName)
    time.sleep(5)
    web_driver.find_element_by_xpath('//*[@id="repository_auto_init"]').click()
    web_driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").send_keys(Keys.ENTER)
    print("Succesfully created repository {}".format(folderName))


if __name__ == "__main__":
    create()
