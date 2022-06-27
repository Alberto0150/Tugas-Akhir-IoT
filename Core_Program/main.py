import image_capture 
import remove_image
import get_request

import time
import os
import subprocess
import threading
import argparse

# Accepting optional argument
parser = argparse.ArgumentParser()
parser.add_argument("-CV", "--colorvu", 
                    help="Change mode into ColorVu HIKVISION Camera",
                    action="store_true")
args = parser.parse_args()

# If using ColorVu camera
if args.colorvu:
    ColorVu_Flag = 1
    ColorVu_username = 'admin' # Set username ColorVu
    ColorVu_password = 'cctv1234' # Set password ColorVu
    ColorVu_cam_IP_array=['192.168.1.103'] # Set ColorVu IP
    ColorVu_ESP_IP_list={} 
else:
    ColorVu_Flag = 0
    ColorVu_username = '' # Set no username ColorVu
    ColorVu_password = '' # Set no password ColorVu


thread_list = {}
each_IP_counter_list = {}
flag = 0

time_to_loop_per_sec = 5

IP_Cam_Relay_Array = ["192.168.1.104",
                    ] # Set ESP-Cam Relay IP
total_ESP = len(IP_Cam_Relay_Array) + 1

counter_capture_before_delete = 1
max_limit_capture_before_delete = 30


# Get default location
default_location = os.getcwd()
# Set saving image location
saving_image_path = './Main-Image-Captured/'

def thread_task(current_IP):
    global counter_capture_before_delete

    time.sleep(time_to_loop_per_sec)
    # Set default result_path & Default value
    result_path = saving_image_path + current_IP + "-result.txt"
    result_file = open(result_path,"w")
    result_file.write("Empty_Room")
    result_file.close()
    
    # Execute capture image
    get_current_ip_counter = each_IP_counter_list[current_IP]
    temp_value = str(get_current_ip_counter)
    each_IP_counter_list[current_IP] = get_current_ip_counter + 1

    if ColorVu_Flag == 0:
        image_capture.capture_mode_urlretrieve(current_IP, temp_value, saving_image_path)
    elif ColorVu_Flag == 1: 
        temp_IP = ColorVu_ESP_IP_list[current_IP]
        custom_saving_image_path = 'D:/Coding-Tugas-Akhir/Main-Image-Captured/'
        image_capture.capture_mode_colorvu(temp_IP,current_IP, temp_value, custom_saving_image_path,ColorVu_username,ColorVu_password)

    # Change back location
    current_location = os.getcwd()
    if current_location not in default_location:
        os.chdir(path=default_location)
        
    # Execute YOLO program
    yolo_exec_command = 'python ./yolov5/detect.py --source ./Main-Image-Captured/' + current_IP + '.' + temp_value + '.png' + ' --custom-report-destination ' + current_IP
    running_program = subprocess.Popen(yolo_exec_command)
    stdoutdata, stderrdata = running_program.communicate()

    # Check if "person"
    result_file = open(result_path, "r")
    if  'person' in result_file.read():
        get_request.sending_get_request(current_IP,0)
    else:
        get_request.sending_get_request(current_IP,1)
    
    # Set counter for naming file
    get_current_ip_counter = each_IP_counter_list[current_IP]
    if get_current_ip_counter > (max_limit_capture_before_delete/len(IP_Cam_Relay_Array)):
        # Reset counter
        counter_capture_before_delete = counter_capture_before_delete - get_current_ip_counter
        each_IP_counter_list[current_IP] = 1
        # Removing old file
        remove_image.remove_mode(current_IP)
    else:
        counter_capture_before_delete+=1
    thread_list[current_IP]= 'DONE'

def create_thread():
    if len(threading.enumerate()) < total_ESP :
        new_thread = threading.Thread(target=thread_task,args=(current_IP,))
        new_thread.start()
        thread_list[current_IP]=new_thread.name
        time.sleep(1)
        print(threading.enumerate())
        
if __name__ == '__main__':
    if ColorVu_Flag == 1:
        for x in range(len(IP_Cam_Relay_Array)):
            # Fill ESP - ColorVu IP list
            ColorVu_ESP_IP_list[IP_Cam_Relay_Array[x]]=ColorVu_cam_IP_array[x]

    print(ColorVu_ESP_IP_list)

    
    for current_IP in IP_Cam_Relay_Array:
        saving_txt_detection_location = 'D:\\Coding-Tugas-Akhir\\Main-Image-Captured\\'+current_IP+'-result.txt'
        
        result_file = open(saving_txt_detection_location,"w")
        result_file.write("Initiating...")
        result_file.close()

        # Set default start to be OFF
        get_request.sending_get_request(current_IP,1)

        # Initiate numbering for each image per IP
        each_IP_counter_list[current_IP] = 1

    while True:
        for current_IP in IP_Cam_Relay_Array:
            # Creating thread
            if flag == 1:
                if thread_list[current_IP] == 'DONE':
                    create_thread()
            else:
                create_thread()
        flag = 1