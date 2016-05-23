from WriteThread import WriteThread
from ReadThread import ReadThread
import time
import Queue


queue_read = Queue.Queue(maxsize=1000)
queue_write = Queue.Queue(maxsize=1000)
write_thread = WriteThread(queue_write)
read_thread = ReadThread(queue_read)

#########################
'''
import numpy as np
x = np.linspace(-np.pi, np.pi, 201)

y = np.int16((np.sin(x)+np.cos(x))*1000)
y1 = np.uint16(y+32768)
print(len(x))
fd = open("sin.bin", 'wb')
fd.write(y)
print(y[5])
#fd.write(y.tolist())
import matplotlib.pylab as plt
plt.plot(y)
plt.show()
#time.sleep(4)
exit()
'''
#######################

read_thread.start()

print("SLEEPING")
time.sleep(5)
print("PLOTTING\n")
from WriteThread import FILTERED_DATA
import matplotlib.pylab as plt
print(FILTERED_DATA[5])
read_thread.interrupt()
plt.plot(FILTERED_DATA)
print("FILTERED LEN: "+ str(len(FILTERED_DATA)))
plt.show()

exit()
#write_thread.start()

i = 0
data_4B = None
while True:
    
    try:
        data_4B = queue_read.get(True, 0.01)  # block until item is available 10ms
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

