from WriteThread import WriteThread
from ReadThread import ReadThread
import time
import Queue

queue = Queue.Queue(maxsize=0)
#writeR = WriteThread(queue)
writeT = ReadThread(queue)

i = 0
writeT.start()

# while i<50:
#     print("MAIN: Sent data: {0}".format(i))
#     queue.put(i)
#     time.sleep(0.02)
#     i+=1

while i<50:
    
    try:
        data_4B = queue.get(True, 0.01)  # block until item is available 10ms
        print("WriteThread: Received data: {0}".format(data_4B))
    except:
        print("{0}\n".format(i))
        continue
    
    i+=1
    time.sleep(0.05)
 

time.sleep(1)    
writeT.interrupt()
print("Loop exited")

