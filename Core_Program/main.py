import core_timer as timer
import image_capture 
import os

if __name__ == '__main__':
    time_to_loop_per_sec = 5
    IP_for_capture = "192.168.229.156" # Set IP
    counter_capture_before_delete = 0
    max_limit_capture_before_delete = 100

    while True:
        value_timer = timer.timer_function(time_to_loop_per_sec)
        # print(value_timer)

        # If pass the time_to_loop_sec
        if value_timer == True :
            # Set counter for naming file
            if counter_capture_before_delete == max_limit_capture_before_delete:
                # Reset counter
                counter_capture_before_delete = 0
            else:
                counter_capture_before_delete+=1

            # Execute Capture Image
            image_capture.capture_mode(IP_for_capture,counter_capture_before_delete)

            # Execute Yolo Program
            yolo_exec_command = 'python ../../yolov5/detect.py --source ../Main-Image-Captured/'+str(counter_capture_before_delete)+'.jpg'
            os.system(yolo_exec_command)

    # TODO return value saja buat kirim perintah ke esp32    