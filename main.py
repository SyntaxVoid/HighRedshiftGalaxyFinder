from __future__ import print_function
import sys
sys.dont_write_bytecode = True
# The above stops the cluttering of source folder with .pyc files

import functions
import numpy
import os
from matplotlib.pyplot import show


'''
Run Sextractor in dual mode and run with detection image as f160w
Example command:

sex -c CONFIG.SEX gs_f160w_cropcal.fits gs_f850l_cropcal.fits

f125 -- J --
f160 -- H --
f606 -- V --
f775 -- I --
f850 -- z --
'''

if __name__ == '__main__':
    FITS       = 0
    CATS       = 0
    ERRORS     = 1

    if FITS:
        print('. . .Compiling Fits Images. . .')
        import FitsCompile
        FitsCompile.run()
        print ('-'*28)


    if CATS:
        print('. . .Compiling Catalogs. . .')
        import CatCompile
        CatCompile.run()
        functions.cat_add(['Catalogs/'+ f for f in os.listdir('Catalogs/')],'MASTER.cat')
        print('-'*28)


    if ERRORS:
        print('. . .Compiling Magnitudes and Errors. . .')

        # -- f125w is in the J band
        print("\n"+"="*10+"F125W Magnitude Errors"+"="*10)
        [f125_my_mag,f125_public_mag,f125_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f125w.cat',4,40,2,['stats','plot'])

        # -- f160w is in the H band
        print("\n"+"="*10+"F160W Magnitude Errors"+"="*10)
        [f160_my_mag,f160_public_mag,f160_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f160w.cat',4,43,2,['stats','plot'])

        # -- f606w is in the V band
        print("\n"+"="*10+"F606W Magnitude Errors"+"="*10)
        [f606_my_mag,f606_public_mag,f606_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f606w.cat',4,22,2,['stats','plot'])

        # -- f775w is in the I band
        print("\n"+"="*10+"F775W Magnitude Errors"+"="*10)
        [f775_my_mag,f775_public_mag,f775_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f775w.cat',4,25,2,['stats','plot'])

        # -- f850l is in the z band
        print("\n"+"="*10+"F850L Magnitude Errors"+"="*10)
        [f850_my_mag,f850_public_mag,f850_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f850l.cat',4,31,2,['stats','plot'])

        show() # To stop the windows from immediately being closed at end of script        show() # To stop the windows from immediately being closed at end of script