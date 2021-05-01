from selenium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
import time
import re

# Main Test Class
@allure.severity(allure.severity_level.NORMAL)
class TestqupsAssignment:

    # Test Case1
    def test_Case01(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bikroy.com/")
        self.driver.maximize_window()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        txt = self.driver.find_elements_by_xpath("//*[text()='Copyright © Saltside Technologies']")[0].text
        assert txt == 'Copyright © Saltside Technologies'
        allure.attach(self.driver.get_screenshot_as_png(), name="CopyrightAssert True", attachment_type=AttachmentType.PNG)

        time.sleep(2)

        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        btn_existance = self.driver.find_elements_by_xpath("/html/body/nav/div/ul[3]/li[5]/a")[0].is_displayed()
        if btn_existance == True:
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name="Button Existance True", attachment_type=AttachmentType.PNG)
        else:
            assert False
            allure.attach(self.driver.get_screenshot_as_png(), name="Button Existance False", attachment_type=AttachmentType.PNG)
        time.sleep(1)
        self.driver.close()

    # Test Case2
    def test_Case02(self, initial = 0, stop=1):
        self.stop = stop
        self.initial = initial
        self.cities = ['dhaka', 'chattogram', 'sylhet', 'khulna', 'barishal', 'rangpur', 'mymensingh', 'rajshahi']
        self.min = 9999999999999999

        for i in range(self.initial, self.stop):
            self.driver = webdriver.Chrome()
            self.driver.get(f"https://bikroy.com/en/ads/{self.cities[i]}")
            self.driver.maximize_window()
            allure.attach(self.driver.get_screenshot_as_png(), name="Accessed city Page", attachment_type=AttachmentType.PNG)

            self.driver.implicitly_wait(5)
            p = self.driver.find_elements_by_class_name('price--3SnqI')

            for x in p:
                tmp_txt = x.text
                txt = tmp_txt.replace(",", "")
                temp = re.findall(r'\d+', txt)
                res = list(map(int, temp))
                if len(res) > 0:
                    now = int(res[0])
                    if now < self.min:
                        self.min = now
                        el = x
                i+=1

            self.driver.implicitly_wait(5)
            try:
                el.click()
                allure.attach(self.driver.get_screenshot_as_png(), name="Min product from Page 1", attachment_type=AttachmentType.PNG)

                try:
                    posted_on = self.driver.find_elements_by_class_name("sub-title--37mkY")[0]
                    assert posted_on.is_displayed() == True
                except:
                    print("Post date Not found")
                    allure.attach(self.driver.get_screenshot_as_png(), name="Post date not found", attachment_type=AttachmentType.PNG)  

                try:
                    description_text = self.driver.find_elements_by_class_name("description--1nRbz")[0]
                    assert description_text.is_displayed() == True
                except:
                    print("Description is not given by seller")
                    allure.attach(self.driver.get_screenshot_as_png(), name="Description not found", attachment_type=AttachmentType.PNG)

                try:
                    hidden_number = self.driver.find_elements_by_xpath("//*[text()='Click to show phone number']")[0]
                    hidden_number.click()
                    mobile_number = self.driver.find_elements_by_class_name("phone-numbers--2COKR")[0]
                    assert mobile_number.is_displayed() == True
                except:
                    print('Phone Number is not given by seller')
                    allure.attach(self.driver.get_screenshot_as_png(), name="Phone Number not found", attachment_type=AttachmentType.PNG)
            
            except:
                print(f"Page loading got issue, clicking skipped for {self.cities[i]}")
                allure.attach(self.driver.get_screenshot_as_png(), name="Page lod issue occured", attachment_type=AttachmentType.PNG)


            self.driver.close()
        
    def test_Case03(self):
        self.st = 1
        self.stp = 2

        while self.stp < 9:
            self.test_Case02(self.st, self.stp)
            time.sleep(3)
            self.st+=1
            self.stp+=1

    def test_Case04(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://bikroy.com/en/ads")
        self.driver.maximize_window()
        

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        txt = self.driver.find_elements_by_xpath("//*[text()='Copyright © Saltside Technologies']")[0].text
        assert txt == 'Copyright © Saltside Technologies'
        allure.attach(self.driver.get_screenshot_as_png(), name="CopyrightAssert True", attachment_type=AttachmentType.PNG)
        time.sleep(2)

        def link_open(tr, sp):
            for m in range(1,sp):
                link = self.driver.find_element_by_xpath(f'//*[@id="app-wrapper"]/div[1]/div[6]/div/div/div/div[1]/div[{tr}]/ul/li[{m}]/a/span')
                time.sleep(1)
                link.click()
                time.sleep(2)
                allure.attach(self.driver.get_screenshot_as_png(), name="Link Page Accessed", attachment_type=AttachmentType.PNG)

                self.driver.back()


        
        # Opening all lincs More from Bikroy
        link_open(2, 7)
        time.sleep(3)

        # Opening all lincs Help & Support
        link_open(3, 4)
        time.sleep(3)

        # Opening all lincs Follow Bikroy
        link_open(4, 5)
        time.sleep(3)

        # Opening all lincs About Bikroy
        link_open(5, 6)

        self.driver.close()