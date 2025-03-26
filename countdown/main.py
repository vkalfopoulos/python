import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1) #i will use the method sleep and inside (1)-> means second
    print("DONE!")

count(0, 10)