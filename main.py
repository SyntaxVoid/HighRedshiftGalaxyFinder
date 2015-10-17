from __future__ import print_function
import sys
sys.dont_write_bytecode = True
# The above stops the cluttering of source folder with .pyc files

import os
from matplotlib.pyplot import show

import libs.jastro
import libs.jtools
import FitsCompile
import CatCompile
import SelectionCriteria

cwd = os.getcwd()

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

header = '''#   1 NUMBER                 Running object number                                      [count]
#   2 ALPHA_J2000            Right ascension of barycenter (J2000)                      [deg]
#   3 DELTA_J2000            Declination of barycenter (J2000)                          [deg]
#   4 F125W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#   5 F125W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#   6 F125W_MAG_AUTO         Kron-like elliptical aperture magnitude                    [mag]
#   7 F125W_MAGERR_AUTO      RMS error for AUTO magnitude                               [mag]
#   8 F160W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#   9 F160W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#  10 F160W_MAG_AUTO         Kron-like elliptical aperture magnitude                    [mag]
#  11 F160W_MAGERR_AUTO      RMS error for AUTO magnitude                               [mag]
#  12 F606W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#  13 F606W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#  14 F606W_MAG_AUTO         Kron-like elliptical aperture magnitude                    [mag]
#  15 F606W_MAGERR_AUTO      RMS error for AUTO magnitude                               [mag]
#  16 F775W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#  17 F775W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#  18 F775W_MAG_AUTO         Kron-like elliptical aperture magnitude                    [mag]
#  19 F775_MAGERR_AUTO       RMS error for AUTO magnitude                               [mag]
#  20 F850LP_FLUX_AUTO       Flux within a Kron-like elliptical aperture                [uJy]
#  21 F850LP_FLUXERR_AUTO    RMS error for AUTO flux                                    [uJy]
#  22 F850LP_MAG_AUTO        Kron-like elliptical aperture magnitude                    [mag]
#  23 F850LP_MAGERR_AUTO     RMS error for AUTO magnitude                               [mag]
'''

if __name__ == '__main__':
    FITS       = 0  # With the Counts / Seconds map, the fits images are already compiled in the
                    # FullMaps_ORIGINAL/ Directory

    CATS       = 0  # Creates catalogs using SExtractor


    ERRORS     = 0  # Plot the errors in magnitude

    SELECT     = 1  # Run through the master catalog and select high redshift galaxies via given dropouts



    FLUX_OR_MAG='flux'    # Use SExtractor's flux to calculate mag or SExtractor's mag by itself.
    COL_DICT = {'flux':4,
                'mag' :6} # My flux is column 4 of the catalog, my mag is column 6 of the catalog.

    if FITS:
        print('. . .Compiling Fits Images. . .')
        FitsCompile.run()
        print ('-'*28)


    if CATS:

        print('. . .Compiling Catalogs. . .')
        CatCompile.run()
        libs.jastro.combine_catalogs(header,
                                     ['Catalogs/'+ f for f in os.listdir('Catalogs/')],[2,3,4,5,6,7],8,
                                     "master.cat",
                                     conversion_factor = 1)
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

    if SELECT:
        b435_cat_dir = "/SelectedObjects/b435.cat"
        v606_cat_dir = "/SelectedObjects/v606.cat"
        i775_cat_dir = "/SelectedObjects/i775.cat"


        num_params = 23  # Length (in lines) of the header of the catalog
        # Flux Values and Errors:

        [v606F,i775F,z850F] = libs.jastro.param_get('master.cat',[12,16,20],24)
        [v606Ferr,i775Ferr,z850Ferr] = libs.jastro.param_get('master.cat',[13,17,21],24)

        # Mag values and Errors
        [v606M,i775M,z850M] = libs.jastro.param_get('master.cat',[14,18,22],24)
        # [v606Merr,i775Merr,z850Merr] = libs.jastro.param_get('master.cat',[15,19,23],24)


        b435_drops = []
        v606_drops = []
        i775_drops = []
        with open('master.cat') as cat_data:
            cat_lines = cat_data.readlines()
            num_lines = len(cat_lines)-num_params
            for i in range(num_lines):
                # B435 Drops (Must wait for b435 data)
                #if SelectionCriteria.b435_dropout(b435M[i],v606M[i],i775M[i],z850M[i],(v606F[i]/v606Ferr[i]),(i775F[i]/i775Ferr[i])):
                #    b435_drops.append(cat_lines[i+num_params].split())

                # V606 Drops (Must wait for b435 data)
                #if SelectionCriteria.v606_dropout(b435M[i],v606M[i],i775M[i],z850M[i],(z850F[i]/z850Ferr[i]),(b435F[i]/b435Ferr[i])):
                #    v606_drops.append(cat_lines[i+num_params].split())

                # I775 Drops
                if SelectionCriteria.i775_dropout(v606M[i],i775M[i],z850M[i],(z850F[i]/z850Ferr[i]),(v606F[i]/v606Ferr[i])):
                    i775_drops.append(cat_lines[num_params+i].split())
        print("Selected {} objects with 4 <= z <= 6 using b435 dropout criteria".format(len(b435_drops)))
        libs.jtools.write_table(b435_drops,header,cwd + b435_cat_dir)
        print("\tCatalog written to {}".format(cwd + b435_cat_dir))
        print("-"*28)

        print("Selected {} objects with 4 <= z <= 6 using v606 dropout criteria".format(len(v606_drops)))
        print("\tCatalog written to {}".format(cwd + v606_cat_dir))
        libs.jtools.write_table(v606_drops,header,cwd + v606_cat_dir)
        print("-"*28)

        print("Selected {} objects with 4 <= z <= 6 using i775 dropout criteria".format(len(i775_drops)))
        print("\tCatalog written to {}".format(cwd + i775_cat_dir))
        libs.jtools.write_table(i775_drops,header,cwd + i775_cat_dir)
        print("-"*28)
