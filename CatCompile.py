###                         ###
# Authored by John Gresl 2015 #
###                         ###
import os

print("If you get a \"sextractor not found\" error, then the program will automatically try using the \"sex\" command instead.")


DETECTION_IMAGE = "FullMaps/gs_f160w_cropcal.fits"

##############################################################
#                Zero Points calculated from                 #
#   http://www.stsci.edu/hst/acs/analysis/zeropoints/zpt.py  #
#                          and                               #
#        http://www.stsci.edu/hst/wfc3/phot_zp_lbn           #
##############################################################
# ZP_f125w = 26.2303
# ZP_f160w = 25.9546
# ZP_f606w = 26.493
# ZP_f775w = 25.662
# ZP_f850l = 24.857

ZP_f125w = 0
ZP_f160w = 0
ZP_f606w = 0
ZP_f775w = 0
ZP_f850l = 0


def run():
    #f125w
    print('---f125w---')
    os.system("sextractor -c SExtractorConfig/f125w.sex {} FullMaps/gs_f125w_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE,ZP_f125w)+ \
                "|| sex -c SExtractorConfig/f125w.sex {} FullMaps/gs_f125w_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE,ZP_f125w))
    #Smooth parameters -> Gaussian 6 (in Saods9)

    #f160w
    print('---f160w---')
    os.system("sextractor -c SExtractorConfig/f160w.sex {} FullMaps/gs_f160w_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE,ZP_f160w)+ \
              "|| sex -c SExtractorConfig/f160w.sex {} FullMaps/gs_f160w_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE,ZP_f160w))
    #Smooth parameters -> Gaussian 6 (in Saods9)

    #f606w
    print('---f606w---')
    os.system("sextractor -c SExtractorConfig/f606w.sex {} FullMaps/gs_f606w_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE,ZP_f606w)+ \
              "|| sex -c SExtractorConfig/f606w.sex {} FullMaps/gs_f606w_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE,ZP_f606w))
    #Smooth parameters -> Gaussian 6 (in Saods9)

    #f775w
    print('---f775w---')
    os.system("sextractor -c SExtractorConfig/f775w.sex {} FullMaps/gs_f775w_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE,ZP_f775w)+ \
              "|| sex -c SExtractorConfig/f775w.sex {} FullMaps/gs_f775w_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE, ZP_f775w))
    #Smooth parameters -> Gaussian 6 (in Saods9)

    #f850l
    print('---f850l---')
    os.system("sextractor -c SExtractorConfig/f850l.sex {} FullMaps/gs_f850l_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE,ZP_f850l)+ \
              "|| sex -c SExtractorConfig/f850l.sex {} FullMaps/gs_f850l_cropcal.fits -MAG_ZEROPOINT {}".format(DETECTION_IMAGE,ZP_f850l))
    #Smooth parameters -> Gaussian 6 (in Saods9)
    return 0


