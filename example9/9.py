from time import sleep


obj = zip([1, 2], ["a", "b"])

for key, value in obj:
    print(key, value)
    sleep(1)
