import time

print("service to create started")
while True:
    current_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.gmtime())
    with open('/data/time_file.txt', "w") as file:
        file.write(current_time)
        file.close()
    time.sleep(10)
