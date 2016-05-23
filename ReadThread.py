import threading
import Queue
import struct
import numpy
import binascii

from WriteThread import FILTERED_DATA


XILLIBUS_DEV = "sin.bin"#"/home/patlas/Pulpit/a.bin" #/dev/xillibus"  # to be changed


#FILTERED_ARRAY = []# numpy.arange()

class ReadThread(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.isStarted = False
        self.fd = open(XILLIBUS_DEV, 'rb')
        self.isInterrupted = False
        #self.fd2 = open("/home/patlas/Pulpit/aa.bin", 'wb')
        self.data = []
        
    def interrupt(self):
        self.isInterrupted = True
    
    def __read(self):
        return self.fd.read(1)
        
    def run(self):
	i = 0
	_data = 0
        while not self.isInterrupted:
            data = self.__read()
            #print(binascii.b2a_hex(a))
            #print(ord(data))
            if len(data) != 0:
                data = ord(data)
		#print(format(data,'02x'))
		if i == 2:
                #FILTERED_DATA = numpy.append(FILTERED_DATA,ord(data))
			data = (data<<8)&0xFF00
			data = data+_data
			print(format(data,'02x'))
			#if data & 0x8000:
			#	data=data*(-1)
                	FILTERED_DATA.append(data)
			self.queue.put(data)
			i = 1
			###print(data)
		else:
			_data = data
			i=2
                	#print(data)
            #self.fd2.write(a)
            
        
        print("ReadThread - stopped.")
        return
            
            
            
