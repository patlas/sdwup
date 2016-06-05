from scipy.fftpack import fft, ifft
from pylab import *
from math import fabs
import numpy
from scipy import signal
import matplotlib.pylab as plt
from FIR_COEF import FIR_COEF as fir_coef


class TestSignal:
    
    
    # F -> base frequency
	def __init__(self, f_sampling, F):
		#self.__T = T
		self.__F = F
		self.__white = False
		self.__f_sampling = f_sampling
		self.__test_sig = None
		self.__t_sample = None
		self.__pc = 12
		self.__noise = None
		self.__spp = f_sampling/F #sample per period
		self._sig_to_filter = None
        

	def generate_white(self, file_name):

		self.__t_sample = numpy.arange(self.__pc*self.__spp)/(self.__f_sampling)#self.__F)

		self.__test_sig = numpy.sin(2*3.14*self.__F*self.__t_sample)

		noise = numpy.sin(2*3.14*527*self.__t_sample)+numpy.sin(2*3.14*431*self.__t_sample)   
		noised_signal = self.__test_sig+noise#self.__noise


		self._sig_to_filter = np.uint16((noised_signal+abs(min(noised_signal)))*1000)	

		fd = open(file_name, 'wb')
		fd.write(self._sig_to_filter)
		fd.close()
		#numpy.set_printoptions(formatter={'int':hex})
		#print(self._sig_to_filter)

		self.show()
        

	def show(self):
		
		_,(p1,p2, p3) = plt.subplots(3,1,sharex=True)
		p1.plot(self._sig_to_filter)        

		y_filtered = signal.lfilter(fir_coef,[1.0],self._sig_to_filter)
    
		fd = open("read_from_filter.bin", 'wb')
		delay = (len(fir_coef)-1)/2
		p2.plot(y_filtered[delay:])

		fd.write(np.uint16(y_filtered))
		fd.close()
		#numpy.set_printoptions(formatter={'int':hex})
		#print("----------------------")
		#print(np.uint16(y_filtered))
		#print("----------------------")
		#print(np.int16(y_filtered))
		#print("----------------------")
		##################3     
 
	def show_firz(self):	
		w,h=signal.freqz(fir_coef)
		plt.figure(2)
		plt.plot(20*numpy.log10(abs(h)))
		plt.show()

        
#a = TestSignal(1000.0, 20.0)
#a.generate_white("noised_signal.bin")
#a.show()

    
        
