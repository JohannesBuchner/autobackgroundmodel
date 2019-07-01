import sys, os
import json
import h5py
import astropy.io.fits as pyfits

targetdir = sys.argv[1]

for filename, target in [line.split() for line in """
chandra-all.hdf5repacked.hdf5pca.hdf5 chandra
hexa.hdf5pca.hdf5 xrte_hexa
hexb.hdf5pca.hdf5 xrte_hexb
pca.hdf5pca.hdf5 xrte_pca
nustar.hdf5repacked.hdf5pca.hdf5 nustar
suzaku.hdf5repacked.hdf5pca.hdf5 suzaku
swift-xrt.hdf5repacked.hdf5pca.hdf5 swift_xrt
xmm-pn.hdf5repacked.hdf5pca.hdf5 xmm_pn
xmm-mos.hdf5repacked.hdf5pca.hdf5 xmm
""".strip().split('\n')]:
	f = h5py.File(filename, 'r')
	with open(os.path.join(targetdir, target + '.json'), 'w') as fout:
		for k in f.keys():
		 	print target, k, f[k].shape
		data = dict([(k, f[k].value.tolist()) for k in f.keys()])
		for k, v in f.attrs.iteritems():
		 	print target, k, v
		data.update(f.attrs)
		json.dump(data, fout)
		print
	

