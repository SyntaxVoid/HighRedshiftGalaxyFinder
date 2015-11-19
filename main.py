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

from GLOBALS import *

'''
 My color - Candels Color (Use V-I and I-Z as color) as a function of H-band magnitude
all bands
plot match candels (i) vs ketrons (i)
then subtract candels from our fits image
plot candels (i) from THEIR cat vs candels (i) from MY cat
'''

if __name__ == '__main__':
    t1 = time.time()
    EXPOSURE       = 0  # Compiles the RMS maps from the EXPOSURE maps
    FITS           = 0  # Compiles Fits Files
    CATS           = 0  # Creates catalogs using SExtractor
    ERRORS         = 0  # Plot the errors in magnitude vs a private Candels catalog
    SELECT         = 0  # Runs through our master catalog and applies selection criteria
    COLOR_COLOR    = 0  # Makes color-color plots. SELECT must be True
    COLOR_COMPARE  = 0  # Compares My Colors with Candels Colors vs. H-Band magnitude
    RED_SHIFT      = 0  # Plots a redshift histogram of my objects using Candels redshift values

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

        pass
    #
    #         # Candels Data (photz catalog)
    #         [v606_mF,i775_mF,z850_mF] = libs.jastro.param_get('TestCatalogs/My606vsCandelsPhotz.cat',[16,20,24],1)
    #         [v606_mM,i775_mM,z850_mM] = [libs.jastro.flux_list2mag(xx,23.9) for xx in [v606_mF,i775_mF,z850_mF]]
    #         VmMiz = libs.jtools.list_operate(i775_mM,z850_mM,'-')
    #         VmMvi = libs.jtools.list_operate(v606_mM,i775_mM,'-')
    #         VmM_colors = [[VmMiz,VmMvi]]
    #
    #
    #
    #
    #         # libs.jastro.color_color([B_colors],'V-Z','B-V','*Candels* B435 Drop Outs -- {} Detected'.format(len(b435_drops)),
    #         #                         xthresh=1.6,ythresh=1.1,xlim=[-1,4],ylim=[-1,6],
    #         #                         a=1.1,b=1.0,graphall='yes')
    #         libs.jastro.color_color([VC_colors,V_colors,VM_colors],'I-Z','V-I','V606 Drop Outs (Mine vs. Candels photom vs. Candels photz',
    #                                xthresh=1.3,ythresh=1.2,xlim=[-1,4],ylim=[-1,6],
    #                                a=1.47,b=0.89,graphall='yes')
    #
    #         libs.jastro.color_color([VmM_colors],'I-Z','V-I','My catalog matched against Candels photz',
    #                                xthresh=1.3,ythresh=1.2,xlim=[-1,4],ylim=[-1,6],
    #                                a=1.47,b=0.89,graphall='yes')
    #
    #         # xx = [V_colors,VC_colors]
    #         # for n,i in enumerate(xx):
    #         #     for (a,b) in i:
    #         #         matplotlib.pyplot.plot(a,b,'ro' if n == 0 else 'go')
    #
    #         #matplotlib.pyplot.plot(VC_colors,'go')
    #
    #
    #         # Plotting redshift distribution
    #         candelsZ = libs.jastro.param_get('TestCatalogs/MineVsCandelsZFull.cat',[37],2)
    #         matplotlib.pyplot.figure()
    #         matplotlib.pyplot.hist(candelsZ, bins=[0,1,2,3,4,5,6,7,8])
    #         matplotlib.pyplot.title('Redshift Distribution')
    #         matplotlib.pyplot.xlabel('Redshift')
    #         matplotlib.pyplot.ylabel('Num. Targets')
    #         matplotlib.pyplot.grid(True)
    #
    #
    #         show()
    #
    #

    t2 = time.time()
    print("\n##Total time elapsed in main.py: {:.2f} seconds".format(t2-t1))