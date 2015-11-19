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
    COLOR_COMPARE  = 0

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
        #My Color - Candels Color (Two plots, V-I and I-Z) as a function of my h160w magnitude

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
    # if MY_COLORS_VS_C:
    #     [my_v,my_i,my_z] = libs.jastro.param_get('TestCatalogs/MasterVsCandels.cat',[18,22,26],2)
    #     [fc_v, fc_i, fc_z ] = libs.jastro.param_get('TestCatalogs/MasterVsCandels.cat',
    #                                              [27+17,27+20,27+26],2)
    #     [c_v, c_i, c_z ] = [libs.jastro.flux_list2mag(xx) for xx in [fc_v, fc_i, fc_z ]]
    #
    #     my_h = libs.jastro.param_get('TestCatalogs/MasterVsCandels.cat',[10],2)[0]
    #
    #     x_del_vi = libs.jtools.list_operate(libs.jtools.list_operate(my_v,my_i,'-'),libs.jtools.list_operate(c_v,c_i,'-'),'-')
    #     x_del_iz = libs.jtools.list_operate(libs.jtools.list_operate(my_i,my_z,'-'),libs.jtools.list_operate(c_i,c_z,'-'),'-')
    #
    #     #Filter everything larger than 20
    #     del_vi = [ ]
    #     del_iz = [ ]
    #     my_h_vi= [ ]
    #     my_h_iz= [ ]
    #     for n,a in enumerate(x_del_vi):
    #         if abs(a) <= 20 and my_h[n] < 95:
    #             del_vi.append(a)
    #             my_h_vi.append(my_h[n])
    #     for n,a in enumerate(x_del_iz):
    #         if abs(a) <= 20 and my_h[n] < 95:
    #             del_iz.append(a)
    #             my_h_iz.append(my_h[n])
    #
    #     matplotlib.pyplot.figure()
    #     matplotlib.pyplot.plot(my_h_vi,del_vi,'r.')
    #     matplotlib.pyplot.ylabel('My Colors - Candels Colors (V-I)')
    #     matplotlib.pyplot.xlabel('H160 magnitude')
    #     matplotlib.pyplot.title('Difference in Colors \nMy(V-I)-Candels(V-I) vs H160 Magnitude')
    #     matplotlib.pyplot.grid(True)
    #
    #     matplotlib.pyplot.figure()
    #     matplotlib.pyplot.plot(my_h_iz,del_iz,'r.')
    #     matplotlib.pyplot.ylabel('My Colors - Candels Colors (I-Z)')
    #     matplotlib.pyplot.xlabel('H160 magnitude')
    #     matplotlib.pyplot.title('Difference in Colors \nMy(I-Z)-Candels(I-Z) vs H160 Magnitude')
    #     matplotlib.pyplot.grid(True)
    #
    #     matplotlib.pyplot.show()


    t2 = time.time()
    print("\n##Total time elapsed in main.py: {:.2f} seconds".format(t2-t1))