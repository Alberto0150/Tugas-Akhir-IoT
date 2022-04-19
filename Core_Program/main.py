import time
import image_capture 
import remove_image
import get_request
import os
import subprocess
import threading

time_to_loop_per_sec = 5
IP_ESP_Cam_Array = ["192.168.29.156",
                    "192.168.29.156",
                    ] # Set IP
counter_capture_before_delete = 1
max_limit_capture_before_delete = 100

# Get Current location
current_location = os.getcwd()
# Set chromedriver.exe location
exec_chrome_driver_path = "C:/Users/asus/Downloads/chromedriver/chromedriver.exe"
# Set saving image location
saving_image_path = './Main-Image-Captured'

def thread_task(current_IP):
    time.sleep(time_to_loop_per_sec)

    # Execute Capture Image
    image_capture.capture_mode(current_IP,counter_capture_before_delete, exec_chrome_driver_path, saving_image_path)

    # Current exec location : @saving_image_path → check before running
    # Change back location
    os.chdir(path=current_location)

    # Execute Yolo Program
    # TODO edit di yolov5 biar bisa multi saving,(1: by additional param, 2: idk yet 😣 )
    yolo_exec_command = 'python ./yolov5/detect.py --source ./Main-Image-Captured/' + current_IP + '.' + str(counter_capture_before_delete) + '.png'
    running_program = subprocess.Popen(yolo_exec_command)
    stdoutdata, stderrdata = running_program.communicate()

    # Check if "person"
    result_path = saving_image_path + "/" + current_IP + "result.txt"
    result_file = open(result_path, "r")
    if  'person' in result_file.read():
        get_request.sending_get_request(current_IP,0)
    else:
        get_request.sending_get_request(current_IP,1)
    
    # Set counter for naming file
    if counter_capture_before_delete >= max_limit_capture_before_delete:
        # Reset counter
        counter_capture_before_delete = 0
        # Removing old file
        remove_image.remove_mode()
    else:
        counter_capture_before_delete+=1


if __name__ == '__main__':
    
    # TODO buat loop 'threading'
    # TODO buat pakai apa gitu, biar misal thread1 kelar dan diatas 5 detik, baru distart lagi htread1. begitu juga thread2 sampai thread-N
    # while True:
    for current_IP in IP_ESP_Cam_Array:
        # Get array index for threadID
        IP_index = IP_ESP_Cam_Array.index(current_IP)
        thread_name = "thread"+str(IP_index)
        new_thread = threading.Thread(target=thread_task,args=(current_IP,),name=thread_name)
        # Dari siniiiiii!!!
        if not new_thread.is_alive():
            new_thread.start()

        