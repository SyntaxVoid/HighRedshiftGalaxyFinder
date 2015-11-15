## The filters [str] which we are looking at in this project
FILTERS = ['f125w','f160w','f435w','f606w','f775w','f850l']

## The name of each selection criteria we will apply
SELECTION_CATS   = ["b435","v606","i775","z7","z6","z5","z4"]
SELECTION_FUNCTS = ["SelectionCriteria.b435","SelectionCriteria.v606",
                    "SelectionCriteria.i775","SelectionCriteria.z7",
                    "SelectionCriteria.z6"  ,"SelectionCriteria.z5",
                    "SelectionCriteria.z4"]

MASTER_COL_DICT = {"Number": 1, "RA": 2, "ALPHA_J2000": 2, "DEC": 3,"DELTA_J2000": 3,
               "F125W_FLUX": 4 , "F125W_FLUXERR": 5 , "F125W_MAG": 6 , "F125W_MAGERR": 7 ,
               "F160W_FLUX": 8 , "F160W_FLUXERR": 9 , "F160W_MAG": 10, "F160W_MAGERR": 11,
               "F435W_FLUX": 12, "F435W_FLUXERR": 13, "F435W_MAG": 14, "F435W_MAGERR": 15,
               "F606W_FLUX": 16, "F606W_FLUXERR": 17, "F606W_MAG": 18, "F606W_MAGERR": 19,
               "F775W_FLUX": 20, "F775W_FLUXERR": 21, "F775W_MAG": 22, "F775W_MAGERR": 23,
               "F850L_FLUX": 24, "F850L_FLUXERR": 25, "F850L_MAG": 26, "F850L_MAGERR": 27}

## The column [int] corresponding to the filter [str] in the Candels column
PUB_COL_DICT = {"f125w":42,"f160w":45,"f435w":21,"f606w":24,"f775w":27,"f850l":33}


## Zerp points [float] of each filter we are analyzing corresponding
## to the units that our map is in. All maps except f435 are in units
## of uJy, which has a corresponding zero point of 23.9.
ZP_f125w = 23.9
ZP_f160w = 23.9
ZP_f435w = 25.665
ZP_f606w = 23.9
ZP_f775w = 23.9
ZP_f850l = 23.9

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
#  12 F435W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#  13 F435W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#  14 F435W_MAG_AUTO         Kron-like elliptical aperture magnitude                    [mag]
#  15 F435W_MAGERR_AUTO      RMS error for AUTO magnitude                               [mag]
#  16 F606W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#  17 F606W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#  18 F606W_MAG_AUTO         Kron-like elliptical aperture magnitude                    [mag]
#  19 F606W_MAGERR_AUTO      RMS error for AUTO magnitude                               [mag]
#  20 F775W_FLUX_AUTO        Flux within a Kron-like elliptical aperture                [uJy]
#  21 F775W_FLUXERR_AUTO     RMS error for AUTO flux                                    [uJy]
#  22 F775W_MAG_AUTO         Kron-like elliptical aperture magnitude                    [mag]
#  23 F775_MAGERR_AUTO       RMS error for AUTO magnitude                               [mag]
#  24 F850LP_FLUX_AUTO       Flux within a Kron-like elliptical aperture                [uJy]
#  25 F850LP_FLUXERR_AUTO    RMS error for AUTO flux                                    [uJy]
#  26 F850LP_MAG_AUTO        Kron-like elliptical aperture magnitude                    [mag]
#  27 F850LP_MAGERR_AUTO     RMS error for AUTO magnitude                               [mag]
'''