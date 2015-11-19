## The filters [str] which we are looking at in this project
FILTERS = ['f125w','f160w','f435w','f606w','f775w','f850l']

SELECTIONS = ["b435","i775","v606","z4","z5","z6","z7","z8"]


# Column number corresponding to each column name of my header
MASTER_COL_DICT = {"Number": 0, "RA": 1, "ALPHA_J2000": 1, "DEC": 2,"DELTA_J2000": 2,
               "F125W_FLUX": 3 , "F125W_FLUXERR": 4 , "F125W_MAG": 5 , "F125W_MAGERR": 6 ,
               "F160W_FLUX": 7 , "F160W_FLUXERR": 8 , "F160W_MAG": 9 , "F160W_MAGERR": 10,
               "F435W_FLUX": 11, "F435W_FLUXERR": 12, "F435W_MAG": 13, "F435W_MAGERR": 14,
               "F606W_FLUX": 15, "F606W_FLUXERR": 16, "F606W_MAG": 17, "F606W_MAGERR": 18,
               "F775W_FLUX": 19, "F775W_FLUXERR": 20, "F775W_MAG": 21, "F775W_MAGERR": 22,
               "F850L_FLUX": 23, "F850L_FLUXERR": 24, "F850L_MAG": 25, "F850L_MAGERR": 26}

MASTER_CANDELS_DICT = {"Number": 0, "IAU_Name": 1, "RA": 2, "ALPHA_J2000": 2,"DEC":3, "DELTA_J2000": 3,
                       "F160W_LIMIT_MAG": 4, "FLAGS": 5, "CLASS_STAR": 6, "CITO_U_FLUX": 7, "CITO_U_FLUXERR": 8,
                       "CITO_U_WEIGHT": 9, "VIMOS_U_FLUX": 10, "VIMOS_U_FLUXERR": 11, "VIMOS_U_WEIGHT": 12,
                       "F435W_FLUX": 13, "F435W_FLUXERR": 14, "F435W_WEIGHT": 15,
                       "F606W_FLUX": 16, "F606W_FLUXERR": 17, "F606W_WEIGHT": 18,
                       "F775W_FLUX": 19, "F775W_FLUXERR": 20, "F775W_WEIGHT": 21,
                       "F814W_FLUX": 22, "F814W_FLUXERR": 23, "F814W_WEIGHT": 24,
                       "F850L_FLUX": 25, "F850L_FLUXERR": 26, "F850L_WEIGHT": 27,
                       "F098M_FLUX": 28, "F098M_FLUXERR": 29, "F098M_WEIGHT": 30,
                       "F105W_FLUX": 31, "F105W_FLUXERR": 32, "F105W_WEIGHT": 33,
                       "F125W_FLUX": 34, "F125W_FLUXERR": 35, "F125W_WEIGHT": 36,
                       "F160W_FLUX": 37, "F160W_FLUXERR": 38, "F160W_WEIGHT": 39}


MY_COLOR_COLOR_OPS = {"b435": [[MASTER_COL_DICT["F435W_MAG"],MASTER_COL_DICT["F606W_MAG"]],
                              [MASTER_COL_DICT["F606W_MAG"],MASTER_COL_DICT["F850L_MAG"]]],
                     "v606": [[MASTER_COL_DICT["F606W_MAG"],MASTER_COL_DICT["F775W_MAG"]],
                              [MASTER_COL_DICT["F775W_MAG"],MASTER_COL_DICT["F850L_MAG"]]],
                     "i775": [[MASTER_COL_DICT["F606W_MAG"],MASTER_COL_DICT["F850L_MAG"]],
                              [MASTER_COL_DICT["F775W_MAG"],MASTER_COL_DICT["F850L_MAG"]]]}

CANDELS_COLOR_COLOR_OPS = {"b435": [[MASTER_CANDELS_DICT["F435W_FLUX"],MASTER_CANDELS_DICT["F606W_FLUX"]],
                                   [MASTER_CANDELS_DICT["F606W_FLUX"],MASTER_CANDELS_DICT["F850L_FLUX"]]],
                           "v606": [[MASTER_CANDELS_DICT["F606W_FLUX"],MASTER_CANDELS_DICT["F775W_FLUX"]],
                                   [MASTER_CANDELS_DICT["F775W_FLUX"],MASTER_CANDELS_DICT["F850L_FLUX"]]],
                           "i775": [[MASTER_CANDELS_DICT["F606W_FLUX"],MASTER_CANDELS_DICT["F850L_FLUX"]],
                                   [MASTER_CANDELS_DICT["F775W_FLUX"],MASTER_CANDELS_DICT["F850L_FLUX"]]]}

COLOR_RULES = {"b435": ["V-Z","B-V",1.6,1.1,[-1,4],[-1,6],1.10,1.00,'yes'],
               "v606": ["I-Z","V-I",1.3,1.2,[-2,5],[-1,6],1.47,0.89,'yes'],
               "i775": ["V-Z","I-Z",1.2,1.3,[-1,4],[-1,6],1.20,1.30,'yes']}

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


MY_MAPS = ["FullMaps/gs_f125w_cropcal.fits","FullMaps/gs_f160w_cropcal.fits","FullMaps/gs_f606w_cropcal.fits",
           "FullMaps/gs_f775w_cropcal.fits","FullMaps/gs_f850l_cropcal.fits"]
CANDELS_MAPS = ["CandelsRescaled/gs_all_candels_ers_udf_f125w_060mas_v0.5_drz.fits",
                "CandelsRescaled/gs_all_candels_ers_udf_f160w_060mas_v0.5_drz.fits",
                "CandelsRescaled/gs_presm4_all_acs_f606w_60mas_v3.0_drz.fits",
                "CandelsRescaled/gs_presm4_all_acs_f775w_60mas_v3.0_drz.fits",
                "CandelsRescaled/gs_presm4_all_acs_f850l_60mas_v3.0_drz.fits"]
SUB_DEST = ["SubtractedMaps/f125w_sub.fits","SubtractedMaps/f160w_sub.fits","SubtractedMaps/f606w_sub.fits",
            "SubtractedMaps/f775w_sub.fits","SubtractedMaps/f850l_sub.fits"]

# Header to add to the catalogs that I generate
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

candels_header = '''# 1  ID (F160W SExtractor ID)
# 2  IAU_Name
# 3  RA (F160W coordinate, J2000, degree)
# 4  DEC (F160W coordinate, J2000, degree)
# 5  F160W_LIMITING_MAGNITUDE (AB)
# 6  FLAGS
# 7  CLASS_STAR (F160W SExtractor S/G classifier output)
# 8  CTIO_U_FLUX (uJy)
# 9  CTIO_U_FLUXERR (uJy)
# 10 CTIO_U_WEIGHT
# 11 VIMOS_U_FLUX (uJy)
# 12 VIMOS_U_FLUXERR (uJy)
# 13 VIMOS_U_WEIGHT
# 14 ACS_F435W_FLUX (uJy)
# 15 ACS_F435W_FLUXERR (uJy)
# 16 ACS_F435W_WEIGHT
# 17 ACS_F606W_FLUX (uJy)
# 18 ACS_F606W_FLUXERR (uJy)
# 19 ACS_F606W_WEIGHT
# 20 ACS_F775W_FLUX (uJy)
# 21 ACS_F775W_FLUXERR (uJy)
# 22 ACS_F775W_WEIGHT
# 23 ACS_F814W_FLUX (uJy)
# 24 ACS_F814W_FLUXERR (uJy)
# 25 ACS_F814W_WEIGHT
# 26 ACS_F850LP_FLUX (uJy)
# 27 ACS_F850LP_FLUXERR (uJy)
# 28 ACS_F850LP_WEIGHT
# 29 WFC3_F098M_FLUX (uJy)
# 30 WFC3_F098M_FLUXERR (uJy)
# 31 WFC3_F098M_WEIGHT
# 32 WFC3_F105W_FLUX (uJy)
# 33 WFC3_F105W_FLUXERR (uJy)
# 34 WFC3_F105W_WEIGHT
# 35 WFC3_F125W_FLUX (uJy)
# 36 WFC3_F125W_FLUXERR (uJy)
# 37 WFC3_F125W_WEIGHT
# 38 WFC3_F160W_FLUX (uJy)
# 39 WFC3_F160W_FLUXERR (uJy)
# 40 WFC3_F160W_WEIGHT
# 41 ISAAC_KS_FLUX (uJy)
# 42 ISAAC_KS_FLUXERR (uJy)
# 43 ISAAC_KS_WEIGHT
# 44 HAWKI_KS_FLUX (uJy)
# 45 HAWKI_KS_FLUXERR (uJy)
# 46 HAWKI_KS_WEIGHT
# 47 IRAC_CH1_FLUX (uJy)
# 48 IRAC_CH1_FLUXERR (uJy)
# 49 IRAC_CH1_WEIGHT
# 50 IRAC_CH2_FLUX (uJy)
# 51 IRAC_CH2_FLUXERR (uJy)
# 52 IRAC_CH2_WEIGHT
# 53 IRAC_CH3_FLUX (uJy)
# 54 IRAC_CH3_FLUXERR (uJy)
# 55 IRAC_CH3_WEIGHT
# 56 IRAC_CH4_FLUX (uJy)
# 57 IRAC_CH4_FLUXERR (uJy)
# 58 IRAC_CH4_WEIGHT
# 59 FLUX_ISO (SExtractor F160W FLUX_ISO, uJy)
# 60 FLUXERR_ISO (SExtractor F160W FLUXERR_ISO, uJy)
# 61 FLUX_AUTO (SExtractor F160W FLUX_AUTO, uJy)
# 62 FLUXERR_AUTO (SExtractor F160W FLUXERR_AUTO, uJy)
# 63 FWHM_IMAGE (FWHM of F160W, pixel, 1 pixel=0.06 arcsec)
# 64 A_IMAGE (F160W SExtractor Profile RMS along major axis, pixel)
# 65 B_IMAGE (F160W SExtractor Profile RMS along minor axis, pixel)
# 66 KRON_RADIUS (F160W SExtractor Kron aperture in units of A or B)
# 67 FLUX_RADIUS_1 (F160W SExtractor 20% of light radius, pixel)
# 68 FLUX_RADIUS_2 (F160W SExtractor 50% of light radius, pixel)
# 69 FLUX_RADIUS_3 (F160W SExtractor 80% of light radius, pixel)
# 70 THETA_IMAGE (F160W SExtractor Position angle (CCW/x), degree)
# 71 APCORR (F160W FLUX_AUTO/FLUX_ISO, applied to ACS and WFC3 bands)
# 72 HOT_FLAG (Source enters the catalog as a hot detection (=1) or a cold detection (=0))
# 73 ISOAREAF_IMAGE (SExtractor F160W Isophotal Area)'''