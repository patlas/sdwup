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


fs = 10000.0
fnyq = fs/2
t = numpy.arange(fs) / fs

fcut = 1000

PI = numpy.pi



y1 = numpy.sin(2*3.14*100*t)
y2 = numpy.sin(2*PI*3000*t)
y3 = numpy.sin(2*PI*5000*t)

y_out = y1+y2+y3;
#plot(y_out[:100])
#show()


fir_coef = signal.firwin(100, fcut/fnyq) #fc
#print(fir_coef)


# w,h=signal.freqz(fir_coef)
# 
# plot(20*numpy.log10(abs(h)))
# show()
#plot(abs(fft(y_out)))


y_filtered = signal.lfilter(fir_coef,[1.0],y_out)
plot(y_out[:100])
#plot(y_filtered[(len(fir_coef)-1):100+len(fir_coef)], 'r')
delay = (len(fir_coef)-1)/2
plot(y_filtered[delay:delay+150])
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




# 
# 
# 
# from numpy import cos, sin, pi, absolute, arange
# from scipy.signal import kaiserord, lfilter, firwin, freqz
# from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show
# 
# 
# #------------------------------------------------
# # Create a signal for demonstration.
# #------------------------------------------------
# 
# sample_rate = 100.0
# nsamples = 400
# t = arange(nsamples) / sample_rate
# x = cos(2*pi*0.5*t) + 0.2*sin(2*pi*2.5*t+0.1) + \
#         0.2*sin(2*pi*15.3*t) + 0.1*sin(2*pi*16.7*t + 0.1) + \
#             0.1*sin(2*pi*23.45*t+.8)
# 
# 
# #------------------------------------------------
# # Create a FIR filter and apply it to x.
# #------------------------------------------------
# 
# # The Nyquist rate of the signal.
# nyq_rate = sample_rate / 2.0
# 
# # The desired width of the transition from pass to stop,
# # relative to the Nyquist rate.  We'll design the filter
# # with a 5 Hz transition width.
# width = 5.0/nyq_rate
# 
# # The desired attenuation in the stop band, in dB.
# ripple_db = 60.0
# 
# # Compute the order and Kaiser parameter for the FIR filter.
# N, beta = kaiserord(ripple_db, width)
# 
# # The cutoff frequency of the filter.
# cutoff_hz = 10.0
# 
# # Use firwin with a Kaiser window to create a lowpass FIR filter.
# taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
# 
# # Use lfilter to filter x with the FIR filter.
# filtered_x = lfilter(taps, 1.0, x)
# 
# #------------------------------------------------
# # Plot the FIR filter coefficients.
# #------------------------------------------------
# 
# figure(1)
# plot(taps, 'bo-', linewidth=2)
# title('Filter Coefficients (%d taps)' % N)
# grid(True)
# 
# #------------------------------------------------
# # Plot the magnitude response of the filter.
# #------------------------------------------------
# 
# figure(2)
# clf()
# w, h = freqz(taps, worN=8000)
# plot((w/pi)*nyq_rate, absolute(h), linewidth=2)
# xlabel('Frequency (Hz)')
# ylabel('Gain')
# title('Frequency Response')
# ylim(-0.05, 1.05)
# grid(True)
# 
# # Upper inset plot.
# ax1 = axes([0.42, 0.6, .45, .25])
# plot((w/pi)*nyq_rate, absolute(h), linewidth=2)
# xlim(0,8.0)
# ylim(0.9985, 1.001)
# grid(True)
# 
# # Lower inset plot
# ax2 = axes([0.42, 0.25, .45, .25])
# plot((w/pi)*nyq_rate, absolute(h), linewidth=2)
# xlim(12.0, 20.0)
# ylim(0.0, 0.0025)
# grid(True)
# 
# #------------------------------------------------
# # Plot the original and filtered signals.
# #------------------------------------------------
# 
# # The phase delay of the filtered signal.
# delay = 0.5 * (N-1) / sample_rate
# 
# figure(3)
# # Plot the original signal.
# plot(t, x)
# # Plot the filtered signal, shifted to compensate for the phase delay.
# plot(t-delay, filtered_x, 'r-')
# # Plot just the "good" part of the filtered signal.  The first N-1
# # samples are "corrupted" by the initial conditions.
# plot(t[N-1:]-delay, filtered_x[N-1:], 'g', linewidth=4)
# 
# xlabel('t')
# grid(True)
# 
# show()
# 
