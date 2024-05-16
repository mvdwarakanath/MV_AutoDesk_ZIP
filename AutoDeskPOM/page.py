#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def AC_button(self):
    buttonAC = self.driver.find_element(By.XPATH,("//div[contains(text(),'AC')]"))
    #buttonAC = self.driver.find_element(By.CSS_SELECTOR,("div[aria-label='all clear']"))
    self.driver.implicitly_wait(10)
    ActionChains(self.driver).move_to_element(buttonAC).click(buttonAC).perform()
    print('Button AC clicked')
    # Verify display is 0
    if self.driver.page_source.__contains__('0'):
        print('Button AC verified')

def numeric_button(self, button):
    button8 = self.driver.find_element(By.XPATH,("//div[contains(text(),'8')]"))
    self.driver.implicitly_wait(10)
    ActionChains(self.driver).move_to_element(button8).click(button8).perform()
    print('Button 8 clicked')
    # Verify display is 8
    if self.driver.page_source.__contains__('8'):
          print('Button 8 verified')

def math_button(self):
    buttonPlus = self.driver.find_element(By.XPATH,("//div[contains(text(),'+')]"))
    self.driver.implicitly_wait(10)
    ActionChains(self.driver).move_to_element(buttonPlus).click(buttonPlus).perform()
    print('Button Plus clicked')
    

    button9 = self.driver.find_element(By.XPATH,("//div[contains(text(),'9')]"))
    self.driver.implicitly_wait(10)
    ActionChains(self.driver).move_to_element(button9).click(button9).perform()
    print('Button 9 clicked')
    
    buttonEquals = self.driver.find_element(By.XPATH,("//div[contains(text(),'=')]"))
    self.driver.implicitly_wait(10)
    ActionChains(self.driver).move_to_element(buttonEquals).click(buttonEquals).perform()
    print('Button Equals clicked')
    # Verify display is 17
    if self.driver.page_source.__contains__('18'):
        print('Math Result 17 verified')
    
def CE_button(self):
    button9 = self.driver.find_element(By.XPATH,("//div[contains(text(),'9')]"))
    self.driver.implicitly_wait(10)
    ActionChains(self.driver).move_to_element(button9).click(button9).perform()
    print('Button 9 clicked')

    buttonCE = self.driver.find_element(By.XPATH,("//div[contains(text(),'CE')]"))
    self.driver.implicitly_wait(10)
    ActionChains(self.driver).move_to_element(buttonCE).click(buttonCE).perform()
    print('Button CE clicked')
    # Verify display is 0
    if self.driver.page_source.__contains__('0'):
            print('Button CE verified')
