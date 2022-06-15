import cv2   #include opencv library functions in python
import urllib.request
import numpy as np

def capture_mode(IP, counter_capture_before_delete,exec_chrome_driver_path,saving_image_path,ColorVu_Flag,ColorVu_username,ColorVu_password):
    
    if ColorVu_Flag == 0:
        #Change to your ESP32-CAM ip
        url = "http://" + IP + "/capture"
    elif ColorVu_Flag == 1:
        #Change to your ColorVu Cam ip
        url = "http://" + ColorVu_username+ ':'+ ColorVu_password + '@' + IP + ":80/Streaming/Channels/1/picture"
    
    file_name = saving_image_path + IP + "." + str(counter_capture_before_delete) + ".png"
    
    #Saving image
    try:
        urllib.request.urlretrieve(url, file_name)
    except urllib.ContentTooShortError:
        print("Error when downloading "+ url+ ", Retrying...")
        urllib.request.urlretrieve(url, file_name)


if __name__ == "__main__":
    capture_mode("youtube.com", 3, "C:/Users/asus/Downloads/chromedriver/chromedriver.exe", './Main-Image-Captured')