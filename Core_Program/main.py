import core_timer as timer
import image_capture 
import remove_image
import get_request
import os
import subprocess

if __name__ == '__main__':
    time_to_loop_per_sec = 5
    # TODO Buat Ip jadi Array
    IP_ESP_Cam = "192.168.29.156" # Set IP
    counter_capture_before_delete = 1
    max_limit_capture_before_delete = 100
    # print(IP_ESP_Cam)

    # Get Current location
    current_location = os.getcwd()
    # Set chromedriver.exe location
    exec_chrome_driver_path = "C:/Users/asus/Downloads/chromedriver/chromedriver.exe"
    # Set saving image location
    saving_image_path = './Main-Image-Captured'
    
    # TODO buat loop 'threading'
    # while True:
    value_timer = timer.timer_function(time_to_loop_per_sec)

    # If pass the time_to_loop_sec
    if value_timer == True :
        # Execute Capture Image
        # TODO buat parameter pembeda saving foto
        image_capture.capture_mode(IP_ESP_Cam,counter_capture_before_delete, exec_chrome_driver_path, saving_image_path)

        # Current exec location : @saving_image_path → check before running
        # Change back location
        os.chdir(path=current_location)

        # Execute Yolo Program
        # TODO buat counter_capture_before_delete biar bisa nerima param beda
        yolo_exec_command = 'python ./yolov5/detect.py --source ./Main-Image-Captured/'+str(counter_capture_before_delete)+'.png'
        running_program = subprocess.Popen(yolo_exec_command)
        stdoutdata, stderrdata = running_program.communicate()

        # Check if "person"
        # TODO buat counter_capture_before_delete biar bisa ngehasilin parameter yg beda
        result_path = saving_image_path + "/result.txt"
        result_file = open(result_path, "r")
        if  'person' in result_file.read():
            get_request.sending_get_request(IP_ESP_Cam,0)
        else:
            get_request.sending_get_request(IP_ESP_Cam,1)
        
        # Set counter for naming file
        if counter_capture_before_delete >= max_limit_capture_before_delete:
            # Reset counter
            counter_capture_before_delete = 0
            # Removing old file
            # TODO buat parameter pembeda penghapus
            remove_image.remove_mode()
        else:
            counter_capture_before_delete+=1