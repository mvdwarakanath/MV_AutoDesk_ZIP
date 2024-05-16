import unittest
import page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# The code below is a test case using Page Object Model.
# The test case is written in the form of a class.
# The class inherits from unittest.TestCase.
# The setUp method is used to open the browser and navigate to the URL. 
# The test_button method is used to test the buttons on the calculator.
# The tearDown method is used to close the browser.
# The if __name__ == "__main__": block is used to run the test case.

class GoogleSearch(unittest.TestCase):
## Test Case using Page Object Model
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url="http://www.google.com") 
        print("Printing Title: " + self.driver.title) 
        if self.driver.page_source.__contains__('Google'):
            print('user logged in')

            self.driver.find_element(By.XPATH,("//textarea[@id='APjFqb']")).send_keys('calculator')
            self.driver.find_element(By.XPATH,("//textarea[@id='APjFqb']")).send_keys(Keys.RETURN)
            self.driver.save_screenshot ('Screenshot1_google.png')
            print('Invoking Calculator UI is DONE')
        self.driver.implicitly_wait(10)
        
    def test_button(self):
        
        # Test the AC button
        page.AC_button(self)

        # Test the numeric button 8
        page.numeric_button(self, button = 8)

        # Test the Plus math button
        page.math_button(self)

        # Test the CE button
        page.CE_button(self)
   
    def tearDown(self):
        self.driver.save_screenshot ('Screenshot_google.png')
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



