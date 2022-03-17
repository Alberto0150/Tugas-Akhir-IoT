import cv2 as cv
import numpy as np
# import urllib.request
import requests
import shutil 

def capture_mode(IP, counter_capture_before_delete):
    #change to your ESP32-CAM ip
    url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
    # url="http://192.168.229.156:81/stream"
    # url="http://"
    # url += IP
    # url +=":81/capture"
    # capturing = urlopen(url)

    
    file_path = './Main-Image-Captured/'
    file_name = str(counter_capture_before_delete) + ".jpg"
    full_path = file_path + file_name
    
    captured_image = requests.get(url, stream = True)
    
    if captured_image.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        captured_image.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(full_path,'wb') as f:
            shutil.copyfileobj(captured_image.raw, f)
            
        print('Image sucessfully Downloaded')
    else:
        print('Image Couldn\'t be retreived')

if __name__ == "__main__":
    capture_mode(1, 2)