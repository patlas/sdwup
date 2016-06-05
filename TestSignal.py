from scipy.fftpack import fft, ifft
from pylab import *
from math import fabs
import numpy
from scipy import signal
import matplotlib.pylab as plt
from FIR_COEF import FIR_COEF as fir_coef

import time


class TestSignal:
    
	filtering_time = None
    
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
        

	def generate_white(self, file_name, sig_type='sin', noise_type='harmonic'):

		self.__t_sample = numpy.arange(self.__pc*self.__spp)/(self.__f_sampling)#self.__F)

		if sig_type == 'combined':
			self.__test_sig = numpy.sin(2*3.14*self.__F*self.__t_sample) + numpy.cos(2*3.14*self.__F/4*self.__t_sample)
		elif sig_type == 'square':
			self.__test_sig = signal.square(2*3.14*self.__F/6*self.__t_sample)
		else: #sig_type is 'sin':
			self.__test_sig = numpy.sin(2*3.14*self.__F*self.__t_sample)# + numpy.cos(2*3.14*self.__F/4*self.__t_sample)
 
		if noise_type == 'white':
			_n = numpy.random.standard_normal(size = len(self.__t_sample))
			_n_scale = max(abs(_n))
			noise = (_n/_n_scale)*3
		else: #noise_type is 'harmonic':
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
		
		#fig1 = plt.figure("Signals")
		fig1,(p1,p2, p3) = plt.subplots(3,1,sharex=True)
		#fig1.add_axes(p1)
		
		T = 1/self.__f_sampling
		x_axis = numpy.arange(0,len(self.__t_sample))
		
		x = [a for a in x_axis if not (a%45)]
		x_new = [round(a*T,3) for a in x]

		plt.xticks(x, x_new)

		p1.plot(self._sig_to_filter)        

		filter_start = time.time()
		y_filtered = signal.lfilter(fir_coef,[1.0],self._sig_to_filter)
		self.filtering_time = time.time() - filter_start;
		
		
		fd = open("read_from_filter.bin", 'wb')
		delay = (len(fir_coef)-1)/2
		p2.plot(y_filtered[delay:], 'r')

		fd.write(np.uint16(y_filtered))
		fd.close()
		#numpy.set_printoptions(formatter={'int':hex})
		#print("----------------------")
		#print(np.uint16(y_filtered))
		#print("----------------------")
		#print(np.int16(y_filtered))
		#print("----------------------")
		##################3     
		
		p1.set_title("Input noised signal")
		p2.set_title("Signal filtered by cortex FIR filter(python)")
		p3.set_title("Signal filtered by FPGA FIR filter")
		
		plt.xlabel("Time [s]")
		plt.figtext(0.02,0.5,"Digitized signal aplitude", va='center', rotation='vertical')
		
		fig2,(p4,p5, p6) = plt.subplots(3,1,sharex=True)
		p4.plot(abs(fft(self._sig_to_filter))[2:])
		p5.plot(abs(fft(y_filtered))[2:], 'r')
		
		p4.set_title("[FFT] Input signal")
		p5.set_title("[FFT] Cortex filtered signal")
		p6.set_title("[FFT] FPGA filtered signal")
		
		plt.xlabel("Normalized frequency")
		plt.figtext(0.02,0.5,"Digitized signal aplitude", va='center', rotation='vertical')
 
	def show_firz(self):	
		w,h=signal.freqz(fir_coef)
		plt.figure(3)
		plt.plot(20*numpy.log10(abs(h)))
		#plt.show()

        
#a = TestSignal(1000.0, 20.0)
#a.generate_white("noised_signal.bin")
#a.show()

    
        
