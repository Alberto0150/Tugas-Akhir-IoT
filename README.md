# Tugas-Akhir-IoT ~ Undergraduate Thesis IoT Project

###  Yolov5 modified repository is [Here](https://github.com/Alberto0150/yolov5)

### Version used:
- Python 3.9.10  
- Arduino IDE 1.8.16

--- 
### Must install / include : 
#### Python Library:
- All YOLOv5 requirement (requirement.txt on Yolov5 modified repository) 
- cv2
- numpy 
- urllib.request
- requests
- subprocess
- threading
- argparse
- time

#### Arduino IDE:
- Additional Boards Manager URLs (Location: Arduino IDE > File > Preferences): 
``` https://dl.espressif.com/dl/package_esp32_index.json, http://arduino.esp8266.com/stable/package_esp8266com_index.json ```

---
### Additional Reference
- ESP Cam camera setting: [Here](https://randomnerdtutorials.com/esp32-cam-ov2640-camera-settings/)

---
Mandatory working tree environment:
```bash
[Root Location]
├───Main-Image-Captured (Add Manually)
├───Tugas-Akhir-IoT (This Repository)
├───yolov5 (YOLOv5 Repository)
```

```[Root Location]``` is where you open terminal and execute python program
---
### To Execute Command
- If using ESP32-Cam :  
```python ./Tugas-Akhir-IoT/Core_Program/main.py```  
- If using ColorVu Camera :  
```python ./Tugas-Akhir-IoT/Core_Program/main.py --colorvu```