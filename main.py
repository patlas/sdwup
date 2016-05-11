from WriteThread import WriteThread
from ReadThread import ReadThread
import time
import Queue

queue_read = Queue.Queue(maxsize=1000)
queue_write = Queue.Queue(maxsize=1000)
write_thread = WriteThread(queue_write)
read_thread = ReadThread(queue_read)


read_thread.start()
write_thread.start()

while True:
    
    try:
        data_4B = queue.get(True, 0.01)  # block until item is available 10ms
        print("WriteThread: Received data: {0}".format(data_4B))
    except:
        print("{0}\n".format(i))
        continue
    
    i+=1
    time.sleep(0.05)
 

time.sleep(1)

read_thread.interrupt()
write_thread.interrupt()
print("END")

