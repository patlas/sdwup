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


a = 300 # must be even
x = numpy.concatenate([numpy.zeros(a),numpy.ones(a)])

 
ww= range(len(x))


fir_coef = ifft(x) # real()

s = len(fir_coef)


rotate_coef = fft_mirror(fir_coef)

x_sinc = numpy.linspace(-15,15,s)
y_sinc = numpy.sinc(x_sinc)


data = y_sinc
#####rotate_coef = numpy.absolute(rotate_coef)
rotate_coef = numpy.real(rotate_coef)

filtered = signal.convolve(rotate_coef, data)

#plot(ww[:600], numpy.absolute(fft(data)) )

plot(fft_mirror(numpy.absolute(fft(data))))
plot(x)
show()

#plot( numpy.absolute(fft(filtered))[:600] )
#show()

#same effect like above
plot(fft_mirror((signal.lfilter(rotate_coef,1,data))))
show()



