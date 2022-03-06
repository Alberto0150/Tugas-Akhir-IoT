import cv2 as cv
import numpy as np
from urllib.request import urlopen
import os

def capture_mode(IP, counter_capture_before_delete):
    #change to your ESP32-CAM ip
    # url="http://192.168.229.156:81/stream"
    url="http://"
    url += IP
    url +=":81/capture"

    dir=os.path.abspath('./Image-file')
    image_file_name = str(counter_capture_before_delete) + ".jpg"
    work_path=os.path.join(dir, image_file_name)

    urlopen.urlretrieve(url,work_path)
    # TODO cari cara connect ke yolo
    # 1. opencv manual dnn, atau
    # 2. call exec SC yolo    