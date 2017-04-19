import time, threading

def loop():
    print("%s is running" % threading.current_thread().name)
    n = 0
    while n< 5:
        n = n+1
        print("%s is running >>> %s" % (threading.current_thread().name,n))
        time.sleep(1)

    print("%s is ended" % threading.current_thread().name)

print("%s is running" % threading.current_thread().name)
t = threading.Thread(target=loop,name='YY')
t.start()
t.join()
print("%s is END" % threading.current_thread().name)
        
