import cv2   #include opencv library functions in python
import urllib.request
import numpy as np

def capture_mode(IP, counter_capture_before_delete,exec_chrome_driver_path,saving_image_path):
    #Change to your ESP32-CAM ip
    url = "http://" + IP + "/capture"
    
    file_name = saving_image_path + IP + "." + str(counter_capture_before_delete) + ".png"
    
    #Saving image
    urllib.request.urlretrieve(url, file_name)

if __name__ == "__main__":
    capture_mode("youtube.com", 3, "C:/Users/asus/Downloads/chromedriver/chromedriver.exe", './Main-Image-Captured')