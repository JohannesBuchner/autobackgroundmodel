import h5py
import numpy
import sys
import tqdm

f = h5py.File(sys.argv[1], 'r')
attrs = f['spectra'].attrs
data = f['spectra'].value
mincts = 1 * data.shape[1] # number of counts per bin

print('original shape: %s' % str(data.shape))
ncts = data.sum(axis=1)
selected = ncts>mincts
print('high-count:    %d have >%d counts' % (selected.sum(), mincts))
print('count distribution:  %d %d %d %d %d' % tuple(numpy.percentile(ncts, [1, 10, 50, 90, 99])))

# order by number of counts in the hope we can get spectra in faint and bright background regions together
indices = numpy.argsort(ncts)
indices2 = indices[::-1]
indices3 = numpy.random.randint(0, len(data), 40 * len(data))
indices = numpy.hstack((indices3, indices2, indices))

# start with individuals already above threshold
newdata = []
initdata = data[selected,:]

# group together those below threshold, in order of indices, reverse
pack = 0
packlen = 0

for i in tqdm.tqdm(indices[::-1]):
	if ncts[i] > mincts:
		continue
	pack += data[i,:]
	packlen += 1
	if pack.sum() > mincts:
		newdata.append(pack)
		pack = 0
		packlen = 0

newdata = numpy.vstack(tuple(newdata))
newdata = numpy.concatenate((initdata, newdata))
print('repacked shape:', newdata.shape)
print('dropped:       ', packlen)

with h5py.File(sys.argv[1] + 'repacked.hdf5', 'w') as f:
	d = f.create_dataset("spectra", data=newdata, compression="gzip", compression_opts=9, shuffle=True)
	for k, v in attrs.items():
		print('   storing attribute %s = %s' % (k, v))
		d.attrs[k] = v

