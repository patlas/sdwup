import threading
import Queue
import struct
import numpy
import binascii


XILLIBUS_DEV = "read_from_filter.bin"


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
			if len(data_r) != 0: ###len(data_r) != 0:
				#print(format(ord(data),'02x'))
				self.queue.put(data_r)


		print("ReadThread - stopped.")
		self.fd.close()
		return
            
            
            
