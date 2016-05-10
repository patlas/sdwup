from WriteThread import WriteThread
import time
import Queue

queue = Queue.Queue(maxsize=0)
writeT = WriteThread(queue)
i = 0
writeT.start()

while i<5:
    print("MAIN: Sent data: {0}".format(i))
    queue.put(i)
    time.sleep(0.2)
    i+=1
    
writeT.interrupt()
print("Loop exited")

