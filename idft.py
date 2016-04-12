from scipy.fftpack import fft, ifft
from pylab import *
from math import fabs
import numpy
from scipy import signal

a = 200 # must be even
x = [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]
x = numpy.concatenate([numpy.zeros(a),numpy.ones(a),numpy.zeros(a)])

#print(x)

h = fft(x)

#print(h)
 
ww= range(len(x))

#print(numpy.absolute(h))
#print(a)

#plot(ww,h)
#show()

#y = ifft(h)

fir_coef = ifft(x) # real()

tab1 = []
tab2 = []

s = len(fir_coef)
for i in range(s/2 ):
	tab1.append( fir_coef[i])
	tab2.append(fir_coef[i+s/2])

rotate_coef = numpy.concatenate([tab2, tab1])

#print(len(rotate_coef), len(ww))

#plot(ww, rotate_coef) # fir coefitient

data = numpy.random.rand(1,s)
data = data[0]

data = numpy.ones(600)

print(len(data))
#plot(ww,data)

rotate_coef.real

filtered = signal.convolve(rotate_coef, data)

plot(ww[:600], data )
show()

plot(ww[:600], filtered[:600] )
show()



