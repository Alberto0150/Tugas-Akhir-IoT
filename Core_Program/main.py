import core_timer as timer
import image_capture 
import os

if __name__ == '__main__':
    time_to_loop__per_sec = 5
    IP_for_capture = "192.168.229.156" # Set IP
    counter_capture_before_delete = 0
    max_limit_capture_before_delete = 100

    while True:
        value_timer = timer.timer_function(time_to_loop__per_sec)
        # print(value_timer)

        # If pass the time_to_loop_sec
        if value_timer == True :
            # capture Image from links
            if counter_capture_before_delete == max_limit_capture_before_delete:
                # Reset counter
                counter_capture_before_delete = 0
            else:
                counter_capture_before_delete+=1

            image_capture.capture_mode(IP_for_capture,counter_capture_before_delete)