from selenium.webdriver.common.by import By

class ItemCategoryPageLocators(object):
    SPCASE_HARD = (By.XPATH, "//div[@class='cat_list']/ul/li[1]")

class DesignPageLocators(object):
    ADD_IMAGE_BUTTON = (By.XPATH, "//div[@id='commandButtons2ListContainer']/div[@id='inputPicture_button2']")
    NEXT_IMAGE_BUTTON = (By.XPATH, "//*[@id='stepNext']")
    BUY_BUTTON = (By.XPATH, '//*[@id="buyThisItem"]')
    SAVE_BUTTON = (By.XPATH, '//*[@id="openSaveMenus"]')
    SAVE_DESIGN_BUTTON = (By.XPATH, '//*[@id="createNewSaveData"]')
    SAVE_CONFIRM_YES_BUTTON = (By.XPATH, '//*[@id="confirmYes"]')
    LATEST_DESIGN = (By.XPATH, '//*[@id="stockDesigns"]/div[@class="stockDesign bounce"]')