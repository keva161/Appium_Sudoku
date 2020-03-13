from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
import os
from test_grid import print_board

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'UEEDU18424003423'
desired_caps['appPackage'] = 'com.fassor.android.sudoku'
desired_caps['appActivity'] = '.MainActivity'
desired_caps['newCommandTimeout'] = '5000'

row_items = []

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

medium = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "com.fassor.android.sudoku:id/buttonMedium")))

medium.click()

sudoku_board_tiles = driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                   "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.GridView/*")

for tile in sudoku_board_tiles:
    tile.screenshot("tile.png")
    img = Image.open('tile.png')
    tile_text = pytesseract.image_to_string(img, config='--psm 10')
    if tile_text == "|" or tile_text == '':
        tile_text = 0
    print(tile_text)
    row_items.append([tile.location, tile_text])
    os.remove("tile.png")

print_board(row_items)