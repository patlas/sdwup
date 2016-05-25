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
        

        
    def generate_harm(self, harmonic_nr, harmonic_step, sample_count):
            pass
        
    def generate_white(self, file_name):
        # noise = numpy.random.standard_normal(size = )
        # self.__t_sample = numpy.arange(self.__T * self.__f_sampling/self.__F) / self.__f_sampling
        # #print(self.__t_sample)
        # self.__test_sig = numpy.sin(2*3.14*self.__F*self.__t_sample)# + noise
        
        # import matplotlib.pylab as plt
        # plt.plot(self.__test_sig)
        # plt.show()
        
	
        self.__t_sample = numpy.arange(self.__pc*self.__spp)/(self.__f_sampling)#self.__F)
        #noise = numpy.random.standard_normal(size = len(self.__t_sample))
        #n_scale = max(abs(noise))
        #self.__noise =  (noise / n_scale)*3
        #self.__test_sig = signal.square(2*3.14*self.__F*self.__t_sample)
	self.__test_sig = numpy.sin(2*3.14*self.__F*self.__t_sample)
	
        #plt.plot(self.__test_sig+self.__noise)
        #plt.show()

	noise = numpy.sin(2*3.14*527*self.__t_sample)+numpy.sin(2*3.14*431*self.__t_sample)   
        noised_signal = self.__test_sig+noise#self.__noise

	self._sig_to_filter = np.int16(noised_signal*1000)	


	fd = open(file_name, 'wb')
	fd.write(self._sig_to_filter)
	#numpy.set_printoptions(formatter={'int':hex})
	#print(self._sig_to_filter)

	self.show()
        
        
        
           
        
    def show(self):
        # t = numpy.arange(self.__T*1000) / (1000*self.__F)
        # sig = numpy.sin(2*3.14*self.__F*t)# + noise
        # 
        # import matplotlib.pylab as plt
        # plt.plot(t,sig)
        # plt.plot(self.__t_sample, self.__test_sig, 'r*')
        # plt.show()

	_,(p1,p2, p3) = plt.subplots(3,1,sharex=True)
        #plt.plot(self.__t_sample,self.__test_sig+self.__noise)
        #plt.plot(self.__t_sample,self.__test_sig,'r')
        #plt.show()
     	'''
	noise = numpy.sin(2*3.14*527*self.__t_sample)+numpy.sin(2*3.14*431*self.__t_sample)   
        noised_signal = self.__test_sig+noise#self.__noise

	self._sig_to_filter = np.int16(noised_signal*1000)	
'''
	p1.plot(self._sig_to_filter)        
	
        y_filtered = signal.lfilter(fir_coef,[1.0],self._sig_to_filter)
#######################        
	#fd = open("read_from_filter.bin", 'wb')
###############3	

	delay = (len(fir_coef)-1)/2
        p2.plot(y_filtered[delay:])
###################3
	#fd.write(np.int16(y_filtered))
	#numpy.set_printoptions(formatter={'int':hex})
	#print("----------------------")
	#print(np.uint16(y_filtered))
	#print("----------------------")
	#print(np.int16(y_filtered))
	#print("----------------------")
##################3
	

        #plt.show()

	'''
	w,h=signal.freqz(fir_coef)

	plot(20*numpy.log10(abs(h)))
	show()
	plt.plot(abs(fft(y_filtered[delay:])))
	plt.show()
        '''
        pass
        
        
        
#a = TestSignal(1000.0, 20.0)
#a.generate_white("noised_signal.bin")
#a.show()

        
        
