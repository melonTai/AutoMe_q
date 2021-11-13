from selenium import webdriver
from package import page
import time
import os
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


def get_spcase_design(image_path:"絶対パス"):
    # chromeドライバー設定
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://me-q.i-designer.com/")

    design_page = page.DesignPage(driver)
    # iphone13 ハードケース デザインページに遷移
    design_page.set_SPCASE_HARD()
    # 画像アップロード
    design_page.add_image(image_path)
    time.sleep(1)
    # デザインを保存
    design_page.click_save_button()
    design_page.click_save_design_button()
    design_page.click_save_confirm_yes_button()
    # 最新のデザインidを取得
    id = design_page.get_latest_design_id()
    # デザインダウンロード
    url = "https://me-q.i-designer.com/save/"+id[:3]+"/"+id+"/"+id+"_0.png"
    download_file(url, "case_design.png")
    time.sleep(5)
    driver.close()

def main():
    folder = os.getcwd()
    image_path = fr"{folder}\test_pig.png"
    print(image_path)
    get_spcase_design(image_path)

if __name__ == '__main__':
    main()