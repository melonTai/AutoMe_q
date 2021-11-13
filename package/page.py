from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from .locators import ItemCategoryPageLocators, DesignPageLocators
from .url_parameters import DesignPageUrlParameters
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import pyperclip

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver:WebDriver):
        self.driver = driver

class ItemCategoryPage(BasePage):
    def is_url_matches(self):
        return "item-category" in self.driver.url

    def click_category(self, locator):
        actions = ActionChains(self.driver)
        category_card = self.driver.find_element(*locator)
        actions.move_to_element(category_card).perform()
        btn_locator = (locator[0], locator[1]+"/div[@class='hover']/div[@class='table']/div[@class='table-cell']/p[@class='btn_make btn']")
        category_btn = self.driver.find_element(*btn_locator)
        category_btn.click()
    
    def click_SPCASE_HRAD(self):
        self.click_category(ItemCategoryPageLocators.SPCASE_HARD)

class DesignPage(BasePage):
    def set_url_parameters(self, parameters:str):
        self.driver.get(f"https://me-q.i-designer.com/?{parameters}")
    
    def set_SPCASE_HARD(self):
        self.set_url_parameters(DesignPageUrlParameters.SPCASE_HARD)
    
    def add_image(self, file_path):
        add_image_btn = self.driver.find_element(*DesignPageLocators.ADD_IMAGE_BUTTON)
        add_image_btn.click()
        time.sleep(1)
        pyperclip.copy(file_path)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('return')
        next_image_btn  = self.driver.find_element(*DesignPageLocators.NEXT_IMAGE_BUTTON)
        next_image_btn.click()
    
    def click_buy_button(self):
        btn = self.driver.find_element(*DesignPageLocators.BUY_BUTTON)
        btn.click()

    def click_save_button(self):
        btn = self.driver.find_element(*DesignPageLocators.SAVE_BUTTON)
        btn.click()
    
    def click_save_design_button(self):
        btn = self.driver.find_element(*DesignPageLocators.SAVE_DESIGN_BUTTON)
        btn.click()

    def click_save_confirm_yes_button(self):
        btn = self.driver.find_element(*DesignPageLocators.SAVE_CONFIRM_YES_BUTTON)
        btn.click()

    def get_latest_design_id(self):
        latest_design = self.driver.find_element(*DesignPageLocators.LATEST_DESIGN)
        design_id = latest_design.get_attribute("data-designid")
        return design_id