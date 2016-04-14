from scipy.fftpack import fft, ifft
from pylab import *
from math import fabs
import numpy
from scipy import signal

def fft_mirror(d):
	t1 = []
	t2 = []
	s = len(d)
	for i in range(s/2 ):
		t1.append( d[i])
		t2.append(d[i+s/2])
	
	return numpy.concatenate([t2, t1])


# a = 10 # must be even
# x = numpy.concatenate([numpy.zeros(a),numpy.ones(a)])
# 
#  
# ww= range(len(x))
# 
# 
# fir_coef = ifft(x) # real()
# 
# s = len(fir_coef)
# 
# 
# rotate_coef = fft_mirror(fir_coef)
# 
# x_sinc = numpy.linspace(-15,15,s)
# y_sinc = numpy.sinc(x_sinc)

fnyq = 5000.0
fsample = 2*fnyq
top = 1.0/fnyq
print(top)
xx = numpy.linspace(0,top*2,fsample) # 10k sample freq
y1 = numpy.sin((2*3.14*fnyq/2)*xx)
y2 = numpy.sin((2*3.14*fnyq*5)*xx)
y3 = numpy.sin((2*3.14*fnyq*10)*xx)

y_out = y1#+y2+y3;
#fft_out = numpy.fft.fft(y_out)
#plot(2.0/fsample*numpy.abs(fft_out))
plot(y_out)
show()

cutoff_freq = fnyq/5.0
fc = cutoff_freq/fnyq

fir_coef = signal.firwin(1001, fc)
print(fir_coef)


# w,h=signal.freqz(fir_coef)
# 
# plot(20*numpy.log10(abs(h)))
# show()
#plot(abs(fft(y_out)))


plot(signal.lfilter(fir_coef,[1.0],y_out))
#plot(signal.convolve(fir_coef, y_out))
show()
'''
#data = y_sinc
data = y_out
#####rotate_coef = numpy.absolute(rotate_coef)
rotate_coef = numpy.real(rotate_coef)
print(rotate_coef)

filtered = signal.convolve(rotate_coef, data)

#plot(ww[:600], numpy.absolute(fft(data)) )

plot(fft_mirror(numpy.absolute(fft(data))))
show()

#plot( numpy.absolute(fft(filtered))[:600] )
#show()

#same effect like above
plot(fft_mirror((signal.lfilter(rotate_coef,1,data))))
show()



'''