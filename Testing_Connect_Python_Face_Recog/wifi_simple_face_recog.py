import cv2 as cv
import numpy as np
from urllib.request import urlopen
import os
import datetime
import time
import sys

#change to your ESP32-CAM ip
url="http://192.168.1.149:9601/stream"
CAMERA_BUFFRER_SIZE=4096
stream=urlopen(url)
bts=b''
i=0
while True:    
    try:
        bts+=stream.read(CAMERA_BUFFRER_SIZE)
        jpghead=bts.find(b'\xff\xd8')
        jpgend=bts.find(b'\xff\xd9')
        if jpghead>-1 and jpgend>-1:
            jpg=bts[jpghead:jpgend+2]
            bts=bts[jpgend+2:]
            img=cv.imdecode(np.frombuffer(jpg,dtype=np.uint8),cv.IMREAD_UNCHANGED)
            img=cv.resize(img,(640,480))
            cv.imshow("a",img)
        k=cv.waitKey(1)
    except Exception as e:
        print("Error:" + str(e))
        bts=b''
        stream=urlopen(url)
        continue
    
    k=cv.waitKey(1)
    # Press A to capture
    if k & 0xFF == ord('a'):
        cv.imwrite(str(i) + ".jpg", img)
        i=i+1
    # Press Q to quit
    if k & 0xFF == ord('q'):
        break
cv.destroyAllWindows()