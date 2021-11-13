import unittest
from selenium import webdriver
from package import page
import time

class ItemCategoryPage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.me-q.jp/item-category")

    def test_select_category(self):
        #Load the main page. In this case the home page of Python.org.
        itemcategory_page = page.ItemCategoryPage(self.driver)
        itemcategory_page.click_SPCASE_HRAD()
        time.sleep(5)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()