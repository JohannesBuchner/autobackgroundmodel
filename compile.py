import astropy.io.fits as pyfits
import numpy
import sys
import h5py

data = []
instrument = None
telescope = None

for filename in sys.argv[2:]:
	#print 'reading', filename
	f = pyfits.open(filename)
	s = f['SPECTRUM']
	y = s.data['COUNTS']
	ncts = y.sum()
	#z = numpy.log10((y + 1.0)/ncts)
	#print ncts, len(y)
	instrument = s.header['INSTRUME']
	telescope = s.header['TELESCOP']
	#if y[:500].mean() > 5:
	if True or y[:200].mean() > 5:
		print(filename)
		data.append(y)
	f.close()

data = numpy.array(data)

with h5py.File(sys.argv[1], 'w') as f:
	d = f.create_dataset("spectra", data=data, compression="gzip", compression_opts=9, shuffle=True)
	d.attrs['INSTRUMENT'] = instrument
	d.attrs['TELESCOPE'] = telescope


