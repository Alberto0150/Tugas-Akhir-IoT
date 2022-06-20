import cv2   #include opencv library functions in python
import urllib.request
import numpy as np

def capture_mode_urlretrieve(current_IP, temp_value, saving_image_path):
    
    #Change url to view ESP32-CAM 
    url = "http://" + current_IP + "/capture"
    
    file_name = saving_image_path + current_IP + "." + str(temp_value) + ".png"
    
    #Saving image
    try:
        urllib.request.urlretrieve(url, file_name)
    except urllib.ContentTooShortError:
        print("Error when downloading "+ url+ ", Retrying...")
        urllib.request.urlretrieve(url, file_name)

def capture_mode_colorvu(temp_IP,current_IP, temp_value, saving_image_path,ColorVu_username,ColorVu_password):
    
    #Change url to view ColorVu Cam 
    url = "rtsp://" + ColorVu_username + ':' + ColorVu_password + '@' + temp_IP + ":554/h264Preview_01_main"
    # rstp://admin:cctv1234@192.168.1.103:554/h264Preview_01_main
    file_name = saving_image_path + current_IP + "." + str(temp_value) + ".png"
    #Saving image
    cv_image_capture = cv2.VideoCapture(url)
    if cv_image_capture.isOpened():
        ret, frame = cv_image_capture.read()
        cv2.imwrite(file_name, frame)   
        cv2.waitKey(1)
        cv_image_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_mode("youtube.com", 3, "C:/Users/asus/Downloads/chromedriver/chromedriver.exe", './Main-Image-Captured')