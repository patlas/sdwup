from WriteThread import WriteThread
from ReadThread import ReadThread
from TestSignal import TestSignal


import os
import time
import Queue
import struct


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

try:
	index = 0
	byte = n_fd.read(1)
	while byte != "":
		# if need send data as BigEndian uncomment 2 lines below
		#byte = struct.unpack(">i",byte)[0] # 1st one
		#byte = struct.pack("<i", byte) # 2nd one
		
		write_thread.write(byte)
		#write_thread.write(byte[1])
		#write_thread.write(byte[2])
		#write_thread.write(byte[3])
		byte = n_fd.read(1)
		index+=1
	print("Send to fpga: {0} bytes".format(index))
finally:
	n_fd.close()


#from WriteThread import FILTERED_DATA
RECEIVED_DATA = []
read_s = 0 #len(RECEIVED_DATA)
#print(read_s)
data = ''
index = 0
while read_s < size:
	try:
		data_r = queue_read.get(True, 0.01)
		#data = ord(data_r[1])
		#data = (data<<8)&0xFF00
		#data = data + ord(data_r[0])
		#data = data+data_r
		#index+=1
		
		#if index == 4:
		#d=struct.unpack("i",data_r)[0]
		RECEIVED_DATA.append(data_r)
			#data = ''
			#index = 0
		read_s+=4
		print("Reading data from fpga. Read {0} bytes".format(read_s))
	except:
		continue

print("Read data count: {0}".format(len(RECEIVED_DATA)))

read_thread.interrupt()

print ("-------------------------")
import numpy
#numpy.set_printoptions(formatter={'int':hex})

#print(numpy.int16(RECEIVED_DATA))
#print RECEIVED_DATA

import matplotlib.pylab as plt
plt.plot(numpy.int32(RECEIVED_DATA))
plt.show()


print("END")

