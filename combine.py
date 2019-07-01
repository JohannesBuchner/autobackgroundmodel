import h5py
import numpy
import sys

data = []

for filename in sys.argv[2:]:
	f = h5py.File(filename, 'r')
	attrs = f['spectra'].attrs
	print(filename, f['spectra'].shape)
	data.append(f['spectra'].value)

newdata = numpy.concatenate(tuple(data))
print 'repacked shape:', newdata.shape

with h5py.File(sys.argv[1], 'w') as f:
	d = f.create_dataset("spectra", data=newdata, compression="gzip", compression_opts=9, shuffle=True)
	for k, v in attrs.iteritems():
		print('   storing attribute %s = %s' % (k, v))
		d.attrs[k] = v

