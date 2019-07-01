import sys, os
import json
import h5py
import numpy

def simplify(v):
	try:
		v = int(v)
	except:
		return v

filename = sys.argv[1]
target = sys.argv[2]

f = h5py.File(filename, 'r')
with open(target.lower() + '.json', 'w') as fout:
	print("getting keys:")
	for k in list(f.keys()):
	 	print(target, k, f[k].shape)
	data = dict([(k, f[k].value.tolist()) for k in list(f.keys())])
	print("getting attributes:")
	for k, v in f.attrs.items():
		print(target, k, v)
	attrs = dict([(k, simplify(v)) for k, v in f.attrs.items()])
	data.update(attrs)
	json.dump(data, fout)
