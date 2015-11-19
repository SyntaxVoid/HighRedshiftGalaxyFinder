from __future__ import print_function
import sys
sys.dont_write_bytecode = True

import os
cwd = os.getcwd()
import time
import matplotlib.pyplot
from matplotlib.pyplot import show

import libs.jastro
import libs.jtools
import RMSCompile
import FitsCompile
import CatCompile
import MagErrors
import RunSelections
import ColorColor
import ColorCompare
import RedShift

from GLOBALS import *

'''
then subtract candels from our fits image
plot candels (i) from THEIR cat vs candels (i) from MY cat
'''

if __name__ == '__main__':
    t1 = time.time()
    EXPOSURE         = 0  # Compiles the RMS maps from the EXPOSURE maps
    FITS             = 0  # Compiles Fits Files
    CATS             = 0  # Creates catalogs using SExtractor
    ERRORS           = 0  # Plot the errors in magnitude vs a private Candels catalog
    SELECT           = 0  # Runs through our master catalog and applies selection criteria
    COLOR_COLOR      = 0  # Makes color-color plots. SELECT must be True
    COLOR_COMPARE    = 0  # Compares My Colors with Candels Colors vs. H-Band magnitude
    RED_SHIFT        = 0  # Plots a redshift histogram of my objects using Candels redshift values
    CANDELS_V_KETRON = 0
    SUBTRACT_MAPS    = 0
    if EXPOSURE:
        RMSCompile.run()
    if FITS:
        FitsCompile.run()
    if CATS:
        CatCompile.run(rms=True)
        CatCompile.run(rms=False)
    if ERRORS:
        MagErrors.run(rms=False)
        MagErrors.run(rms=True)
    if SELECT:
        RunSelections.run("masterNONE.cat","SelectedObjects/Mine/",header,MASTER_COL_DICT,False)
        RunSelections.run("masterRMS.cat","SelectedObjects/Mine/",header,MASTER_COL_DICT,True)
        RunSelections.run("Candels_Catalog/CANDELS.GOODSS.F160W.v1_1.photom.cat","SelectedObjects/Candels/",candels_header,MASTER_CANDELS_DICT,False)
    if COLOR_COLOR:
        ColorColor.run("My {0} Selections ({1})","SelectedObjects/Mine/NONE/","ketron",False)
        ColorColor.run("My {0} Selections ({1})","SelectedObjects/Mine/RMS/","ketron",True)
        ColorColor.run("Candels {0} Selections ({1})","SelectedObjects/Candels/NONE/","candels",False)
        show()
    if COLOR_COMPARE:
        ColorCompare.run("TestCatalogs/MatchedNONE.cat","Color-Color Comparison \n(Without RMS Maps)")
        ColorCompare.run("TestCatalogs/MatchedRMS.cat","Color-Color Comparison \n(With RMS Maps)")
        show()
    if REDSHIFT:
        RedShift.run("B435-Drops\n(Without RMS Maps)","TestCatalogs/MatchedNONE_b435_Z.cat",36)
        RedShift.run("V606-Drops\n(Without RMS Maps)","TestCatalogs/MatchedNONE_v606_Z.cat",36)
        RedShift.run("I775-Drops\n(Without RMS Maps)","TestCatalogs/MatchedNONE_i775_Z.cat",36)
        show()

        RedShift.run("B435-Drops\n(With RMS Maps)","TestCatalogs/MatchedRMS_b435_Z.cat",36)
        RedShift.run("V606-Drops\n(With RMS Maps)","TestCatalogs/MatchedRMS_v606_Z.cat",36)
        RedShift.run("I775-Drops\n(With RMS Maps)","TestCatalogs/MatchedRMS_i775_Z.cat",36)
        show()

        RedShift.run("B435-Drops\n(Using Candels Catalogs)","TestCatalogs/MatchedCandels_b435.cat",82)
        RedShift.run("V606-Drops\n(Using Candels Catalogs)","TestCatalogs/MatchedCandels_v606.cat",82)
        RedShift.run("I775-Drops\n(Using Candels Catalogs)","TestCatalogs/MatchedCandels_i775.cat",82)
        show()


    t2 = time.time()
    print("\n##Total time elapsed in main.py: {:.2f} seconds".format(t2-t1))