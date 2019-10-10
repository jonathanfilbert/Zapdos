import selenium
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

chromedriver = "./chromedriver"
company_list = []
random_names = []
link_form = "https://skycruiser8.typeform.com/to/iLt5F6"

def open_file():
    with open("./us_agencies.csv") as csv_file:
        reader = csv.reader(csv_file,delimiter=',')
        for items in reader:
            name = items[6]
            if(name not in company_list):
                company_list.append(name)
            else:
                continue

def choose_companies():
    name1 = random.choice(company_list)
    name2 = random.choice(company_list)
    name3 = random.choice(company_list)
    random_names.append(name1)
    random_names.append(name2)
    random_names.append(name3)

def isiForm():
    # SEARCH COMPANY
    time.sleep(5)
    button = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]/div/div/div[2]/div/div/div/div/div/div/div[1]/button')
    button.click()
    time.sleep(5)
    enter = browser.find_element_by_xpath('//*[@id="block-e6ec484b-4d00-43e5-be39-bc41c7324851"]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/button')
    enter.click()
    time.sleep(5)
    yes1 = browser.find_element_by_xpath('//*[@id="choice-6f9e19be-5767-4255-bd46-d057a0963afe-yes"]/div')
    yes1.click()
    time.sleep(4)
    yes2 = browser.find_element_by_xpath('//*[@id="choice-7db8ba55-866f-486c-866d-8695790af08c-yes"]/div')
    yes2.click()
    time.sleep(4)
    yes3 = browser.find_element_by_xpath('//*[@id="choice-cc2954dd-1f93-430b-be39-8135a159cc51-yes"]/div')
    yes3.click()
    time.sleep(4)
    yes4 = browser.find_element_by_xpath('//*[@id="choice-ee70249d-154b-4b35-879b-a7e5a009bac9-yes"]/div')
    yes4.click()
    time.sleep(4)
    yes5 = browser.find_element_by_xpath('//*[@id="choice-8990dc40-d07f-47a5-9d44-a6ff58a447d2-yes"]/div')
    yes5.click()
    time.sleep(4)
    name_input = browser.find_element_by_xpath('//*[@id="shortText-941f5e44-b5ac-4b1d-9eca-45ea48bd2e33"]')
    inputan = random_names[0] + ", " + random_names[1] + ", sama "+ random_names[2]
    name_input.send_keys(inputan)
    time.sleep(5)
    ok = browser.find_element_by_xpath('//*[@id="block-941f5e44-b5ac-4b1d-9eca-45ea48bd2e33"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/button')
    ok.click()
    time.sleep(4)
    resiko = browser.find_element_by_xpath('//*[@id="block-71ad9825-2fe6-4828-8842-382932a21d21"]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/textarea')
    resiko.send_keys("gatau")
    time.sleep(5)
    ok2 = browser.find_element_by_xpath('//*[@id="block-71ad9825-2fe6-4828-8842-382932a21d21"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/button')
    ok2.click()
    time.sleep(4)
    gaspol = browser.find_element_by_xpath('//*[@id="choice-dbe1f273-913c-4362-8e46-a31011e41fca"]/div')
    gaspol.click()
    time.sleep(4)
    submit = browser.find_element_by_xpath('//*[@id="block-0dccb4a9-6a31-40fe-afe6-e67f83572ce9"]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/button')
    submit.click()
    time.sleep(4)
    ovo = browser.find_element_by_xpath('//*[@id="block-520e6307-abe7-44b3-8eed-04fd1a05798c"]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/button')
    ovo.click()
    time.sleep(4)
    hape = browser.find_element_by_xpath('//*[@id="shortText-8de19b10-1c23-4701-a01a-983c56be1253"]')
    hape.send_keys("088809952050")
    time.sleep(5)
    hapekelar = browser.find_element_by_xpath('//*[@id="block-8de19b10-1c23-4701-a01a-983c56be1253"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/button')
    hapekelar.click()
    time.sleep(4)
    final = browser.find_element_by_xpath('//*[@id="unfixedFooter"]/div/div/div[1]/div/div/div/div/button')
    final.click()

def main():
    open_file()
    browser.get(link_form)
    while(True):
        random_names.clear()
        choose_companies()
        print(random_names)
        time.sleep(5)
        isiForm()
        time.sleep(3)
        browser.refresh()

if __name__ == "__main__":
    browser = webdriver.Chrome(chromedriver)
    main()