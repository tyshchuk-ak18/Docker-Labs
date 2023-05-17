import os
import time

time.sleep(1)
print("service to read started")
while True:
    files = os.listdir("/data")
    for file in files:
        if file.endswith(".txt"):
            fileDir = "/data/" + str(file)
            with open(fileDir, "r") as file_content:
                content = file_content.read()
            print("Filename: " + str(file) + ", Content: " + str(content))
        else:
            print("no file found")
    time.sleep(5)
