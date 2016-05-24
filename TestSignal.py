from scipy.fftpack import fft, ifft
from pylab import *
from math import fabs
import numpy
from scipy import signal


# fs = 10000.0
# fnyq = fs/2
# t = numpy.arange(fs) / fs
# 
# fcut = 1000
# 
# PI = numpy.pi
# 
# 
# 
# y1 = numpy.sin(2*3.14*100*t)
# y2 = numpy.sin(2*PI*3000*t)
# y3 = numpy.sin(2*PI*5000*t)
# 
# y_out = y1+y2+y3;
# 
# plot(abs(fft(y_out)))

class TestSignal:
    
    
    # F -> base frequency
    def __init__(self, f_sampling, F):
        #self.__T = T
        self.__F = F
        self.__white = False
        self.__f_sampling = f_sampling
        self.__test_sig = None
        self.__t_sample = None
        self.__T = 5
        self.__noise = None
        

        
    def generate_harm(self, harmonic_nr, harmonic_step, sample_count):
            pass
        
    def generate_white(self):
        # noise = numpy.random.standard_normal(size = )
        # self.__t_sample = numpy.arange(self.__T * self.__f_sampling/self.__F) / self.__f_sampling
        # #print(self.__t_sample)
        # self.__test_sig = numpy.sin(2*3.14*self.__F*self.__t_sample)# + noise
        
        # import matplotlib.pylab as plt
        # plt.plot(self.__test_sig)
        # plt.show()
        
        self.__t_sample = numpy.arange(self.__T*1000) / (1000*self.__F)
        noise = numpy.random.standard_normal(size = len(self.__t_sample))
        n_scale = max(abs(noise))
        self.__noise =  (noise / n_scale)*3
        self.__test_sig  = numpy.sin(2*3.14*self.__F*self.__t_sample)
        
        
        
           
        
    def show(self):
        # t = numpy.arange(self.__T*1000) / (1000*self.__F)
        # sig = numpy.sin(2*3.14*self.__F*t)# + noise
        # 
        # import matplotlib.pylab as plt
        # plt.plot(t,sig)
        # plt.plot(self.__t_sample, self.__test_sig, 'r*')
        # plt.show()
        
        import matplotlib.pylab as plt
        #plt.plot(self.__t_sample,self.__test_sig+self.__noise)
        #plt.plot(self.__t_sample,self.__test_sig,'r')
        #plt.show()
        
        noised_signal = self.__t_sample,self.__test_sig+self.__noise
        from FIR_COEF import FIR_COEF as fir_coef
        y_filtered = signal.lfilter(fir_coef,[1.0],noised_signal)
        
        plt.plot(y_filtered)
        plt.show()
        
        pass
        
        
        
a = TestSignal(400.0, 50.0)
a.generate_white()
a.show()

        
        