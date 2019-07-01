import h5py
import numpy
import sys

f = h5py.File(sys.argv[1], 'r')
attrs = f['spectra'].attrs
data = f['spectra'].value
mincts = 10000

print 'original shape:', data.shape
ncts = data.sum(axis=1)
selected = ncts>mincts
print 'high-count:    ', selected.sum()

indices = numpy.argsort(ncts)
newdata = data[selected,:]
pack = 0
packlen = 0

for i in indices[::-1]:
	if ncts[i] > mincts:
		continue
	pack += data[i,:]
	packlen += 1
	if pack.sum() > mincts:
		newdata = numpy.concatenate((newdata, [pack]))
		pack = 0
		packlen = 0

print 'repacked shape:', newdata.shape
print 'dropped:       ', packlen

with h5py.File(sys.argv[1] + 'repacked.hdf5', 'w') as f:
	d = f.create_dataset("spectra", data=newdata, compression="gzip", compression_opts=9, shuffle=True)
	for k, v in attrs.iteritems():
		print '   storing attribute %s = %s' % (k, v)
		d.attrs[k] = v

