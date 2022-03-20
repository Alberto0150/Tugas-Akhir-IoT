import cv2 as cv
import numpy as np
# import urllib.request
import requests
import shutil 
from selenium import webdriver

def capture_mode(IP, counter_capture_before_delete):
    #change to your ESP32-CAM ip
    # url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
    # url="http://192.168.229.156:81/stream"
    url="http://"
    url += IP
    # url +=":81/capture"
    print(url)
    # capturing = urlopen(url)
    
    # Change default saving location
    custom_options = webdriver.ChromeOptions() 
    custom_options.add_argument("download.default_directory=D:/Coding-Tugas-Akhir/Main-Image-Captured")

    # Replace with downloaded .exe chrome driver location
    driver = webdriver.Chrome("C:/Users/asus/Downloads/chromedriver/chromedriver.exe", chrome_options= custom_options)
    driver.get(url)
    
    # file_path = './Main-Image-Captured/'
    file_name = str(counter_capture_before_delete) + ".png"
    # full_path = file_path + file_name
    
    driver.get_screenshot_as_file(file_name)
    driver.quit()
    # captured_image = requests.get(url, stream = True)
    
    # if captured_image.status_code == 200:
    #     # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    #     captured_image.raw.decode_content = True
        
    #     # Open a local file with wb ( write binary ) permission.
    #     with open(full_path,'wb') as f:
    #         shutil.copyfileobj(captured_image.raw, f)
            
    #     print('Image sucessfully Downloaded')
    # else:
    #     print('Image Couldn\'t be retreived')

if __name__ == "__main__":
    capture_mode("192.168.1.5", 2)