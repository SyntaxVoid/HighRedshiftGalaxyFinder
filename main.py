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

Column numbers correspond to columns of MUSYC Data/ipac_ascii_ECDFS_BVRdet_Subaru_v1.tbl
f125 -- J -- Column 29
f160 -- H -- Column 31
f606 -- V -- Column 21
f775 -- I -- Column 25
f850 -- z -- Column 27
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

        # -- f125w is in the J band which is column 29 of the public catalog. (column 34 of matched)
        print("\n"+"="*10+"F125W Magnitude Errors"+"="*10)
        [f125_my_mag,f125_public_mag,f125_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f125w.cat',4,34,2,['stats','plot'])

        # -- f160w is in the H band which is column 31 of the public catalog. (column 36 of matched)
        print("\n"+"="*10+"F160W Magnitude Errors"+"="*10)
        [f160_my_mag,f160_public_mag,f160_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f160w.cat',4,36,2,['stats','plot'])

        # -- f606w is in the V band which is column 21 of the public catalog. (column 26 of matched)
        print("\n"+"="*10+"F606W Magnitude Errors"+"="*10)
        [f606_my_mag,f606_public_mag,f606_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f606w.cat',4,26,2,['stats','plot'])

        # -- f775w is in the I band which is column 25 of the public catalog. (column 30 of matched)
        print("\n"+"="*10+"F775W Magnitude Errors"+"="*10)
        [f775_my_mag,f775_public_mag,f775_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f775w.cat',4,30,2,['stats','plot'])

        # -- f850l is in the z band which is column 27 of the public catalog. (column 32 of matched)
        print("\n"+"="*10+"F850L Magnitude Errors"+"="*10)
        [f850_my_mag,f850_public_mag,f850_deltas] = \
            functions.mag_errors('Matches/Cats/Matched_f850l.cat',4,32,2,['stats','plot'])

        show() # To stop the windows from immediately being closed at end of script