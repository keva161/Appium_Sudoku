from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
import numpy as np
import os
from helper_functions import possible, solve

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'UEEDU18424003423'
desired_caps['appPackage'] = 'com.fassor.android.sudoku'
desired_caps['appActivity'] = '.MainActivity'
desired_caps['newCommandTimeout'] = '5000'

grid = []

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
        if type(tile_text) != int:
            tile_text = int(tile_text)
        os.remove("tile.png")
        print(tile_text)
        grid.append(tile_text)

board = np.asarray(grid).reshape(9, 9)

print(board)
print('-')
solve(board)