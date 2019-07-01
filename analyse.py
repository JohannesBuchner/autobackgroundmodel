import astropy.io.fits as pyfits
import sys

filename = sys.argv[1]
print(('file:', filename))
f = pyfits.open(filename)
s = f['SPECTRUM']

telescope = s.header['TELESCOP']
print(('telescope: %s' % telescope))
instrument = s.header['INSTRUME']
print(('instrument: %s' % instrument))

print(('exposure time: %.1f seconds' % s.header['EXPOSURE']))
y = s.data['COUNTS']
print(('counts: %d' % y.sum()))


if y.sum() > 1000:
	import matplotlib.pyplot as plt
	#x = s.data['PI'] / 1000.
	x = s.data['CHANNEL']
	plt.plot(x, y, 'o-')
	plt.savefig('analyse.pdf', bbox_inches='tight')
	plt.close()

