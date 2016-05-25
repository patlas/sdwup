import threading
import Queue
import os
import numpy

__size = 50 # os.path.getsize('data.bin') #binary file with data to be filtered

FILTERED_DATA = [] #numpy.arange(__size)

XILLIBUS_DEV = "send_to_filter.bin" #/dev/xillibus"  # to be changed

class WriteThread(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.isStarted = False
        self.fd = open(XILLIBUS_DEV, 'wb')
        self.isInterrupted = False
        
    def interrupt(self):
        self.isInterrupted = True
    
    def __write(self, data):
        self.fd.write(data)#bytearray([data]))

    def write(self, data):
	self.__write(data)
        
    def run(self):
        data_4B = None

        while not self.isInterrupted:
            try:
                data_4B = self.queue.get(True, 0.01)  # block until item is available 10ms
                #print("WriteThread: Received data: {0}".format(data_4B))
            except:
                #print("No data in queue")
                continue
            
            self.__write(data_4B)
        
        print("WriteThread - stopped.")
        return
            
