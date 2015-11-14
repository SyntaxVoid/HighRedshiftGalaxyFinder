# ##                         ## #
#  Authored by John Gresl 2015  #
# ##                         ## #
import os
import time
from libs.jtools import tokenize_str,print_tokenized
from GLOBALS import *



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



DETECTION_IMAGE = "FullMaps/gs_f160w_cropcal.fits"


def _sextractor(filter_name,zp,sex_args = ""):
    print("\n#SExtracting FullMaps/gs_{}_cropcal.fits".format(filter_name))
    t1 = time.time()
    sex_str = "sextractor {1} FullMaps/gs_{0}_cropcal.fits -c SExtractorConfig/default.sex {3} -MAG_ZEROPOINT {2}" +\
           "|| sex -c default.sex {1} FullMaps/gs_{0}_cropcal.fits {3} -MAG_ZEROPOINT {2}"
    command = sex_str.format(filter_name,DETECTION_IMAGE,zp,sex_args)
    if filter_name == "f435w":
        command = command.replace("MAP_RMS","NONE")
    print_tokenized(*tokenize_str(command[command.find(" "):command.find("||")]),start="     -")
    os.system(command)
    t2 = time.time()
    if "MAP_RMS" in command:
        print("  #Catalog written to {}/Catalogs/RMS/gs_{}_cropcal.cat".format(os.getcwd(),filter_name))
    else:
        print("  #Catalog written to {}/Catalogs/NONE/gs_{}_cropcal.cat".format(os.getcwd(),filter_name))
    print("  #Time Elapsed: {:.2f} seconds".format(t2-t1))
    return


def run(rms=False):
    #rms is either True or False, and tells us whether to use RMS maps or not
    t1 = time.time()
    _sex_args = "-CATALOG_NAME Catalogs/{}/gs_{}_cropcal.cat " + \
                "-WEIGHT_TYPE {} -WEIGHT_IMAGE FullRMSMaps/gs_{}_rms.fits"
    if rms:
        _sex_args = _sex_args.format("RMS","{0}","MAP_RMS","{0}")
    else:
        _sex_args = _sex_args.format("NONE","{0}","NONE","{0}")
    print("\n" + "="*80)
    print("="*26+"Now Running Source Extractor"+"="*26)
    print("="*80 + "\n")
    print("If you get a \"sextractor not found\" error, then the program will" +
          "automatically\ntry using the \"sex\" command instead.")
    for f in FILTERS:
        sex_args = _sex_args.format(f)
        _sextractor(f,eval("ZP_{}".format(f)),sex_args)
    t2 = time.time()

    print("#Total Time Elapsed: {:.2f}".format(t2-t1))
    print("\n" + ("="*80 + "\n")*3)
    return


if __name__ == '__main__':
    run(True)
    run(False)
