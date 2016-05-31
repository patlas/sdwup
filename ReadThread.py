import threading
import Queue
import struct
import numpy
import binascii

from WriteThread import FILTERED_DATA


XILLIBUS_DEV = "read_from_filter.bin"#"/home/patlas/Pulpit/a.bin" #/dev/xillibus"  # to be changed


#FILTERED_ARRAY = []# numpy.arange()

class ReadThread(threading.Thread):

	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.isStarted = False
		self.fd = open(XILLIBUS_DEV, 'rb')
		self.isInterrupted = False
		self.data = []

	def interrupt(self):
		self.isInterrupted = True

	def __read(self):
		return self.fd.read(2)

	def run(self):
		while not self.isInterrupted:
			data_r = self.__read()
			#print(binascii.b2a_hex(a))
			#print(ord(data))
			if len(data_r) != 0:
				data = ord(data_r[1])
				data = (data<<8)&0xFF00
				data = data + ord(data_r[0])
				print(format(data,'02x'))

				FILTERED_DATA.append(data)
				self.queue.put(data)


		print("ReadThread - stopped.")
		return
            
            
            
