Machine-learned Background Spectral Model
--------------------------------------------

Builds a paramtric spectral model for the background of any instrument
from a large number of example background spectra.


Uses PCA to learn average spectral shape and features and their correlations.

Works on the detector-level, completely empirical (does not go through the response).
See Simmonds, Buchner et al. 2018.


Usage
--------

* `analyse.py bkg1.fits`: plot spectrum

* `compile.py pack.hdf5 bkg1.fits bkg2.fits bkg3.fits`: Combine number of counts from many background spectra into a HDF5 file

* `(concat/combine).py outfile.hdf5 infile1.hdf5 infile2.hdf5 etc ` # take several hdf5 packs and combine them.


* `compress.py <cmd> infile.hdf5`

  * create: make infile.hdf5pca.hdf5 -- find 20 most important pca components
  * components: read file above and plot components
  * showcomp: for each component show interactive plot 
  * check: for a few spectra, show its approximate pca reconstruction based on pca components

* `repack.py pack.h5` # stacks spectra so they each have at least 10000 counts
  The output is pack.h5repacked.hdf5
* `export.py targetdir` 
  make json files



