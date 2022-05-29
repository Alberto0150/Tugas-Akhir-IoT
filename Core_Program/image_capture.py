import os
from selenium import webdriver

def capture_mode(IP, counter_capture_before_delete,exec_chrome_driver_path):
    #change to your ESP32-CAM ip
    url="http://"
    url += IP


    # Change default running location
    # os.chdir(path=saving_image_path)

    # Set path for chrome driver
    exec_path = exec_chrome_driver_path
    driver = webdriver.Chrome(executable_path= exec_path)
    driver.get(url)
    
    file_name = IP + "." + str(counter_capture_before_delete) + ".png"
    
    driver.get_screenshot_as_file(file_name)
    driver.quit()

if __name__ == "__main__":
    capture_mode("youtube.com", 3, "C:/Users/asus/Downloads/chromedriver/chromedriver.exe", './Main-Image-Captured')