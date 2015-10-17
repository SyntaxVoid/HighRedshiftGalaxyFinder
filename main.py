from __future__ import print_function
import sys
sys.dont_write_bytecode = True
# The above stops the cluttering of source folder with .pyc files

import os
from matplotlib.pyplot import show

import libs.jastro


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

# ADJUSTED ZERO POINTS (ZP for uJy is 23.9)
ZP_f125w = 23.9#+0.0
ZP_f160w = 23.9#+0.0
ZP_f606w = 23.9#+1.8
ZP_f775w = 23.9#+1.9
ZP_f850l = 23.9#+1.7

if __name__ == '__main__':
    FITS       = 0  # With the Counts / Seconds map, the fits images are already compiled in the
                    # FullMaps_ORIGINAL/ Directory

    CATS       = 1  # Creates catalogs using SExtractor


    ERRORS     = 0  # Plot the errors in magnitude


    FLUX_OR_MAG='flux'    # Use SExtractor's flux to calculate mag or SExtractor's mag by itself.
    COL_DICT = {'flux':4,
                'mag' :6} # My flux is column 4 of the catalog, my mag is column 6 of the catalog.

    if FITS:
        print('. . .Compiling Fits Images. . .')
        import FitsCompile
        FitsCompile.run()
        print ('-'*28)


    if CATS:
        header = '''#   1 NUMBER                 Running object number                                      [count]
#   2 ALPHA_J2000            Right ascension of barycenter (J2000)                      [deg]
#   3 DELTA_J2000            Declination of barycenter (J2000)                          [deg]
#   4 F125W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#   5 F125W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#   6 F160W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#   7 F160W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#   8 F606W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#   9 F606W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#  10 F775W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#  11 F775W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#  12 F850LP_FLUX_AUTO       Flux within a Kron-like elliptical aperture                [uJy]
#  13 F125LP_FLUXERR_AUTO    RMS error for AUTO flux                                    [uJy]
'''
        print('. . .Compiling Catalogs. . .')
        import CatCompile
        CatCompile.run()
        libs.jastro.combine_catalogs(header,
                                     ['Catalogs/'+ f for f in os.listdir('Catalogs/')],[2,3,4,5],8,
                                     "master.cat",
                                     conversion_factor = pow(10,6))
        print('-'*28)


    if ERRORS:
        print('. . .Compiling Magnitudes and Errors. . .')

        # -- f125w is in the J band
        print("\n"+"="*10+"F125W Magnitude Errors"+"="*10)
        [f125_my_mag,f125_public_mag,f125_deltas] = \
            libs.jastro.mag_errors('Matches/Cats/Matched_f125w.cat',FLUX_OR_MAG,COL_DICT[FLUX_OR_MAG],42,2,ZP_f125w,['stats','plot'])

        # -- f160w is in the H band
        print("\n"+"="*10+"F160W Magnitude Errors"+"="*10)
        [f160_my_mag,f160_public_mag,f160_deltas] = \
            libs.jastro.mag_errors('Matches/Cats/Matched_f160w.cat',FLUX_OR_MAG,COL_DICT[FLUX_OR_MAG],45,2,ZP_f160w,['stats','plot'])

        # -- f606w is in the V band
        print("\n"+"="*10+"F606W Magnitude Errors"+"="*10)
        [f606_my_mag,f606_public_mag,f606_deltas] = \
            libs.jastro.mag_errors('Matches/Cats/Matched_f606w.cat',FLUX_OR_MAG,COL_DICT[FLUX_OR_MAG],24,2,ZP_f606w,['stats','plot'])

        # -- f775w is in the I band
        print("\n"+"="*10+"F775W Magnitude Errors"+"="*10)
        [f775_my_mag,f775_public_mag,f775_deltas] = \
            libs.jastro.mag_errors('Matches/Cats/Matched_f775w.cat',FLUX_OR_MAG,COL_DICT[FLUX_OR_MAG],27,2,ZP_f775w,['stats','plot'])

        # -- f850l is in the z band
        print("\n"+"="*10+"F850L Magnitude Errors"+"="*10)
        [f850_my_mag,f850_public_mag,f850_deltas] = \
            libs.jastro.mag_errors('Matches/Cats/Matched_f850l.cat',FLUX_OR_MAG,COL_DICT[FLUX_OR_MAG],33,2,ZP_f850l,['stats','plot'])

        show() # To stop the windows from immediately being closed at end of script        show() # To stop the windows from immediately being closed at end of script
