# ##                         ## #
#  Authored by John Gresl 2015  #
# ##                         ## #
import os


DETECTION_IMAGE = "FullMaps/gs_f160w_cropcal.fits"

# ############################################################ #
#                 Zero Points calculated from                  #
#    http://www.stsci.edu/hst/acs/analysis/zeropoints/zpt.py   #
#                           and                                #
#         http://www.stsci.edu/hst/wfc3/phot_zp_lbn            #
# ############################################################ #

# ZP_f125w = 26.2303
# ZP_f160w = 25.9546
# ZP_f606w = 26.493
# ZP_f775w = 25.662
# ZP_f850l = 24.857


# Every map except for 435 is in the units of uJy which has a defined ZP as 23.9.
# The ZP for 435 was calculated from http://www.stsci.edu/hst/acs/analysis/zeropoints/zpt.py
ZP_f125w = 23.9
ZP_f160w = 23.9
ZP_f435w = 25.665
ZP_f606w = 23.9
ZP_f775w = 23.9
ZP_f850l = 23.9


def run():

    print("\n" + "="*80)
    print("If you get a \"sextractor not found\" error, then the program will" +
          "automatically try using the \"sex\" command instead.")

    # f125w
    print('---f125w---')
    os.system("sextractor -c SExtractorConfig/f125w.sex {} FullMaps/gs_f125w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f125w) +
              "|| sex -c SExtractorConfig/f125w.sex {} FullMaps/gs_f125w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f125w))
    print('\tCatalog written to {}'.format(os.getcwd()+'/Catalogs/gs_f125w_cropcal.cat'))

    # f160w
    print('---f160w---')
    os.system("sextractor -c SExtractorConfig/f160w.sex {} FullMaps/gs_f160w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f160w) +
              "|| sex -c SExtractorConfig/f160w.sex {} FullMaps/gs_f160w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f160w))
    print('\tCatalog written to {}'.format(os.getcwd()+'/Catalogs/gs_f160w_cropcal.cat'))

    # f435w
    print("---f435w---")
    os.system("sextractor -c SExtractorConfig/f435w.sex {} FullMaps/gs_f435w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f435w) +
              "|| sex -c SExtractorConfig/f435w.sex {} FullMaps/gs_f435w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f435w))
    print('\tCatalog written to {}'.format(os.getcwd()+'/Catalogs/gs_f435w_cropcal.cat'))

    # f606w
    print('---f606w---')
    os.system("sextractor -c SExtractorConfig/f606w.sex {} FullMaps/gs_f606w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f606w) +
              "|| sex -c SExtractorConfig/f606w.sex {} FullMaps/gs_f606w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f606w))
    print('\tCatalog written to {}'.format(os.getcwd()+'/Catalogs/gs_f606w_cropcal.cat'))

    # f775w
    print('---f775w---')
    os.system("sextractor -c SExtractorConfig/f775w.sex {} FullMaps/gs_f775w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f775w) +
              "|| sex -c SExtractorConfig/f775w.sex {} FullMaps/gs_f775w_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f775w))
    print('\tCatalog written to {}'.format(os.getcwd()+'/Catalogs/gs_f775w_cropcal.cat'))

    # f850l
    print('---f850l---')
    os.system("sextractor -c SExtractorConfig/f850l.sex {} FullMaps/gs_f850l_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f850l) +
              "|| sex -c SExtractorConfig/f850l.sex {} FullMaps/gs_f850l_cropcal.fits -MAG_ZEROPOINT {}"
              .format(DETECTION_IMAGE, ZP_f850l))
    print('\tCatalog written to {}'.format(os.getcwd()+'/Catalogs/gs_f850l_cropcal.cat'))
    return
