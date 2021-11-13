import unittest
from selenium import webdriver
from package import page
import time

class DesignPage(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://me-q.i-designer.com/")

    def test_auto_design_case(self):
        """画像をアプロードし，自動でデザインケース画像のidを取得するテスト関数．
        """
        design_page = page.DesignPage(self.driver)
        design_page.set_SPCASE_HARD()
        file_path = "デザイン画像の絶対パス"
        design_page.add_image(file_path)
        time.sleep(1)
        design_page.click_save_button()
        design_page.click_save_design_button()
        design_page.click_save_confirm_yes_button()
        design_id = design_page.get_latest_design_id()
        print(design_id)
        time.sleep(5)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()