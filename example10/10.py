import time

while True:
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print(now)
    time.sleep(1)
