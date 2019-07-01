import h5py
import numpy
import sys
import os

outfile = sys.argv[1]
filenames = sys.argv[2:]
alldata = None
for filename in filenames:
	f = h5py.File(filename, 'r')
	attrs = f['spectra'].attrs
	data = f['spectra'].value
	print data.shape
	if alldata is None:
		alldata = data
	else:
		alldata = numpy.concatenate((data, alldata))
print alldata.shape

with h5py.File(outfile, 'w') as f:
	d = f.create_dataset("spectra", data=alldata, compression="gzip", compression_opts=9, shuffle=True)
	for k, v in attrs.iteritems():
		d.attrs[k] = os.environ.get(k, v)
		print k, d.attrs[k]
	
