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

        while not self.isInterrupted:
            data = self.__read()
            #print(binascii.b2a_hex(a))
            #print(ord(data))
            if len(data) != 0:
                self.queue.put(ord(data))
                #FILTERED_DATA = numpy.append(FILTERED_DATA,ord(data))
                FILTERED_DATA.append(ord(data))
                #print(ord(data))
            #self.fd2.write(a)
            
        
        print("ReadThread - stopped.")
        return
            
            
            
