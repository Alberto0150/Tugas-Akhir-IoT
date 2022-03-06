import cv2 as cv
import numpy as np
from urllib.request import urlopen
import sys

#change to your ESP32-CAM ip
url="http://192.168.229.156:81/stream"
# url="http://192.168.229.156:81/capture"
# url="http://"
# url+= sys.argv[1]
# # Stream port 
# url+=":81/stream"
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
            img=cv.flip(img,0)           
            h,w=img.shape[:2]
            img=cv.resize(img,(640,480))
            cv.imshow("Img-Capturing",img)
        k=cv.waitKey(1)
    except Exception as e:
        print("Error:" + str(e))
        bts=b''
        stream=urlopen(url)
        continue
    
    k=cv.waitKey(1)
    if k & 0xFF == ord('q'):
        break
cv.destroyAllWindows()