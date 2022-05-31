import time
import image_capture 
import remove_image
import get_request
import os
import subprocess
import threading

thread_list = {}
flag = 0

time_to_loop_per_sec = 5
IP_ESP_Cam_Array = ["192.168.158.172",
                    "192.168.158.156",
                    ] # Set IP
total_ESP = len(IP_ESP_Cam_Array) + 1

counter_capture_before_delete = 1
max_limit_capture_before_delete = 100


# Get Defaultlocation
default_location = os.getcwd()
# Set chromedriver.exe location
exec_chrome_driver_path = "C:/Users/asus/Downloads/chromedriver/chromedriver.exe"
# Set saving image location
saving_image_path = './Main-Image-Captured/'

def thread_task(current_IP):
    global counter_capture_before_delete

    time.sleep(time_to_loop_per_sec)

    # Execute Capture Image
    # try:
    #     os.chdir(path=saving_image_path)
    # except:
    #     pass
    # current_location = os.getcwd()
    # if saving_image_path not in current_location:
        # os.chdir(path=saving_image_path)
        # print('Change to image location')
    image_capture.capture_mode(current_IP,'1', exec_chrome_driver_path,saving_image_path)

    # Current exec location : @saving_image_path → check before running
    # Change back location
    current_location = os.getcwd()
    if current_location not in default_location:
        os.chdir(path=default_location)
        print('Change to default location')
        

    # Execute Yolo Program
    # TODO modify penamaan nama file yang berformat angka statis( disini masih '1')
    yolo_exec_command = 'python ./yolov5/detect.py --source ./Main-Image-Captured/' + current_IP + '.' + '1' + '.png' + ' --custom-report-destination ' + current_IP
    running_program = subprocess.Popen(yolo_exec_command)
    stdoutdata, stderrdata = running_program.communicate()

    # Check if "person"
    #result_path = saving_image_path + "/" + current_IP + "-result.txt"
    result_path = saving_image_path + current_IP + "-result.txt"
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
    thread_list[current_IP]= 'DONE'

def create_thread():
    if len(threading.enumerate()) < total_ESP :
        print(current_IP)
        new_thread = threading.Thread(target=thread_task,args=(current_IP,))
        print("Creating thread...")
        new_thread.start()
        print("Appending...")
        thread_list[current_IP]=new_thread.name
        print(new_thread.name)
        time.sleep(1)
        print(threading.enumerate())
        
if __name__ == '__main__':
    
    for current_IP in IP_ESP_Cam_Array:
        saving_txt_detection_location = 'D:\\Coding-Tugas-Akhir\\Main-Image-Captured\\'+current_IP+'-result.txt'
        result_file = open(saving_txt_detection_location,"w")
        result_file.close()
    # while True:
    for current_IP in IP_ESP_Cam_Array:
        # Creating thread
        if flag == 1:
            if thread_list[current_IP] == 'DONE':
                create_thread()
        else:
            create_thread()
    flag = 1
        
