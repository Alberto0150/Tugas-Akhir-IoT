import time

def timer_function(x):
    start_time = time.time()
    loop_each_time_by_sec = x

    while True:
        current_time = time.time()
        elapse_time = current_time - start_time
        if elapse_time >= loop_each_time_by_sec :
            start_time = current_time
            return True
            # break
