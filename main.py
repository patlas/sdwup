from WriteThread import WriteThread
from ReadThread import ReadThread
from TestSignal import TestSignal
from FIR_COEF import FIR_COEF as fir_coef


import os
import time
import Queue
import struct
import numpy as np


queue_read = Queue.Queue(maxsize=1000)
queue_write = Queue.Queue(maxsize=1000)
write_thread = WriteThread(queue_write)
read_thread = ReadThread(queue_read)

# generate sinus signal 20Hz with noise and sample it with 1000Hz
signal = TestSignal(1000.0, 20.0)
# save generated noised signal to file
signal.generate_white("noised_signal.bin")

# start waiting for data upcoming from fpga
read_thread.start()

# get file size and open (contains noised signal) and send it to fpga
size = (os.stat("noised_signal.bin")).st_size;
print("FILE SIZE:"+str(size))
n_fd = open("noised_signal.bin", "rb")
noised_signal = np.fromfile(n_fd, dtype=np.uint16)
n_fd.close()

for data_16b in noised_signal:
	# if need send data as BigEndian uncomment 2 lines below
	#byte = struct.unpack(">i",byte)[0] # 1st one
	#byte = struct.pack("<i", byte) # 2nd one
	
	####print(format(data_16b,'02x'))
	write_thread.write(data_16b)

print("Send to fpga: {0} bytes".format(size))


RECEIVED_DATA = []
read_s = 0 #len(RECEIVED_DATA)

while read_s < size:
	try:
		data_r = queue_read.get(True, 0.01)

		p_data=struct.unpack("=H",data_r)[0]
		RECEIVED_DATA.append(p_data)
		
		read_s+=2
		print("Reading data from fpga. Read {0} bytes".format(read_s))
	except:
		continue

print("Read data count: {0}".format(len(RECEIVED_DATA)))

read_thread.interrupt()

print ("-------------------------")

#numpy.set_printoptions(formatter={'int':hex})
#print(numpy.int16(RECEIVED_DATA))
#print RECEIVED_DATA

import matplotlib.pylab as plt
f_delay = (len(fir_coef)-1)/2
plot_array = np.concatenate((np.zeros(f_delay,dtype=np.uint16), np.uint16(RECEIVED_DATA)[f_delay:]))
plt.plot(plot_array)
plt.show()


print("END")

