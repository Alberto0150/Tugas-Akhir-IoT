import cv2 as cv
import numpy as np
# import urllib.request
import requests
import shutil 
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def capture_mode(IP, counter_capture_before_delete,exec_chrome_driver_path, saving_image_path):
    #change to your ESP32-CAM ip
    # url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
    url = "https://youtube.com"
    # url="http://192.168.229.156:81/stream"
    # url="http://"
    # url += IP
    # url +=":81/capture"
    
    # Change default saving location
    # custom_options = webdriver.ChromeOptions() 
    # prefs = {"download.default_directory" : "./Main-Image-Captured"}
    # options = Options()
    # options.add_experimental_option("prefs",
    #     {"download.default_directory": "./Main-Image-Captured/",
    #     "download.prompt_for_download": False,
    #     "download.directory_upgrade": True,
    #     "safebrowsing.enabled": True
    #     }
    # )

    # Change default running location
    os.chdir(path=saving_image_path)

    # custom_options.add_argument("download.default_directory=D:/Coding-Tugas-Akhir/Main-Image-Captured/")
    exec_path = exec_chrome_driver_path

    # driver = webdriver.Chrome(executable_path= exec_path, chrome_options = custom_options)
    driver = webdriver.Chrome(executable_path= exec_path)
    driver.get(url)
    
    # file_path = './Main-Image-Captured/'
    file_name = str(counter_capture_before_delete) + ".png"
    # full_path = file_path + file_name
    
    driver.get_screenshot_as_file(file_name)
    driver.quit()
    # captured_image = requests.get(url, stream = True)

if __name__ == "__main__":
    capture_mode("youtube.com", 3, "C:/Users/asus/Downloads/chromedriver/chromedriver.exe", './Main-Image-Captured')