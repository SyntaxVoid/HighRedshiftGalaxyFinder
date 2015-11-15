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
import SelectionCriteria
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
    USE_RMS        = 0
    USE_NONE       = 0
    CATS           = 1  # Creates catalogs using SExtractor
    ERRORS         = 0  # Plot the errors in magnitude vs a private Candels catalog
    SELECT_ME      = 0  # Runs through our master catalog and applies selection criteria
    COLOR_COLOR_ME = 0  # Makes color-color plots. SELECT must be True
    SELECT_C       = 0
    COLOR_COLOR_C  = 0
    MY_COLORS_VS_C = 0

    if EXPOSURE:
        RMSCompile.run()
        pass

    if FITS:
        FitsCompile.run()

    if CATS:
        if USE_RMS:
            CatCompile.run(True)
            libs.jastro.combine_catalogs(header,sorted(['Catalogs/RMS/'+ f for f in os.listdir('Catalogs/RMS/')]),[2,3,4,5,6,7],8,"masterRMS.cat",conversion_factor = 1)
        if USE_NONE:
            CatCompile.run(False)
            libs.jastro.combine_catalogs(header,sorted(['Catalogs/NONE/'+ f for f in os.listdir('Catalogs/NONE/')]),[2,3,4,5,6,7],8,"masterNONE.cat",conversion_factor = 1)
    if ERRORS:
        MagErrors.run(False)
        MagErrors.run(True)

    if SELECT_ME:

        pass

    if COLOR_COLOR_ME:
            B_colors = [[Bvz,Bbv]]
            V_colors = [[Viz,Vvi]]
            I_colors = [[Ivz,Iiz]]

            libs.jastro.color_color([B_colors],'V-Z','B-V','*MY* B435 Drop Outs -- {} Detected'.format(len(b435_drops)),
                                    xthresh=1.6,ythresh=1.1,xlim=[-1,4],ylim=[-1,6],
                                    a=1.1,b=1.0,graphall='yes')

            libs.jastro.color_color([V_colors],'I-Z','V-I','*MY* V606 Drop Outs -- {} Detected'.format(len(v606_drops)),
                                    xthresh=1.3,ythresh=1.2,xlim=[-1,4],ylim=[-1,6],
                                    a=1.47,b=0.89,graphall='yes')
            #show()

    if SELECT_C:
        print("\n" + "="*80)
        num_params = 73  # Length (in lines) of the header of the catalog
        b435_cat_dir = "/SelectedObjects/Candels/b435_Candels.cat"
        v606_cat_dir = "/SelectedObjects/Candels/v606_Candels.cat"
        i775_cat_dir = "/SelectedObjects/Candels/i775_Candels.cat"
        z7_cat_dir   = "/SelectedObjects/Candels/z7_Candels.cat"
        z6_cat_dir   = "/SelectedObjects/Candels/z6_Candels.cat"
        z5_cat_dir   = "/SelectedObjects/Candels/z5_Candels.cat"
        z4_cat_dir   = "/SelectedObjects/Candels/z4_Candels.cat"

        # Flux Values and Errors:

        [j125F,h160F,b435F,v606F,i775F,z850F] = \
            libs.jastro.param_get('/home/john/Documents/Cooray/01_KetronsMaps/Candels_Catalog/CANDELS.GOODSS.F160W.v1_1.photom.cat',[35,38,14,17,20,26],74)

        [b125Ferr,b160Ferr,b435Ferr,v606Ferr,i775Ferr,z850Ferr] = \
            libs.jastro.param_get('/home/john/Documents/Cooray/01_KetronsMaps/Candels_Catalog/CANDELS.GOODSS.F160W.v1_1.photom.cat',[36,39,15,18,21,27],74)
        # Mag values
        [j125M,h160M,b435M,v606M,i775M,z850M] = \
            [libs.jastro.flux_list2mag(xx,23.9) for xx in [j125F,h160F,b435F,v606F,i775F,z850F]]



        # Will append the line of the master catalog to these lists if
        # they meet the selection criteria.
        b435_drops = []
        v606_drops = []
        i775_drops = []
        z7 = []
        z6 = []
        z5 = []
        z4 = []
        z3 = []

        # Notation: Bbv indicates the list corresponding to the B dropout with values of b_mags - v_mags
        Bbv = []
        Bvz = []

        Vvi = []
        Viz = []

        Iiz = []
        Ivz = []

        with open('/home/john/Documents/Cooray/01_KetronsMaps/Candels_Catalog/CANDELS.GOODSS.F160W.v1_1.photom.cat') as cat_data:
            cat_lines = cat_data.readlines()
            num_lines = len(cat_lines)-num_params
            for i in range(num_lines):
                # B435 Drops (Must wait for b435 data)
        #         if SelectionCriteria.b435_dropout(b435M[i],v606M[i],i775M[i],z850M[i],
        #                                           (v606F[i]/v606Ferr[i]),(i775F[i]/i775Ferr[i])):
        #             b435_drops.append(cat_lines[i+num_params].split())
        #             Bbv.append(b435M[i]-v606M[i])
        #             Bvz.append(v606M[i]-z850M[i])
        #
        #         # V606 Drops (Must wait for b435 data)
                if SelectionCriteria.v606_dropout(b435M[i],v606M[i],i775M[i],z850M[i],
                                                    (z850F[i]/z850Ferr[i]),(b435F[i]/b435Ferr[i])):
                    v606_drops.append(cat_lines[i+num_params].split())
                    Vvi.append(v606M[i]-i775M[i])
                    Viz.append(i775M[i]-z850M[i])
        #
        #         # I775 Drops
        #         if SelectionCriteria.i775_dropout(v606M[i],i775M[i],z850M[i],
        #                                             (z850F[i]/z850Ferr[i]),(v606F[i]/v606Ferr[i]),i):
        #             i775_drops.append(cat_lines[num_params+i].split())
        #             Iiz.append(i775M[i]-z850M[i])
        #             Ivz.append(v606M[i]-z850M[i])
        #
        #         # We need to check backwords from Z~7 to Z~4 to make sure we don't double
        #         # count any galaxies.
        #         # z~7
        #         elif SelectionCriteria.z7(j125M[i],j125M[i],h160M[i],i775M[i],z850M[i],
        #                                   (b435F[i]/b435Ferr[i]),(v606F[i]/v606Ferr[i]),
        #                                   (i775F[i]/i775Ferr[i]),(i775F[i]/i775Ferr[i])):
        #             z7.append(cat_lines[num_params+i].split())
        #
        #         #z~6
        #         elif SelectionCriteria.z6(j125M[i],j125M[i],h160M[i],v606M[i],i775M[i],i775M[i],z850M[i],
        #                                   b435F[i]/b435Ferr[i],v606F[i]/v606Ferr[i],i775F[i]/i775Ferr[i]):
        #             z6.append(cat_lines[num_params+i].split())
        #
        #         #z~5
        #         elif SelectionCriteria.z5(h160M[i],v606M[i],i775M[i],z850M[i],b435F[i]/b435Ferr[i]):
        #             z5.append(cat_lines[num_params+i].split())
        #
        #         #z~4
        #         elif SelectionCriteria.z4(j125M[i],b435M[i],v606M[i],i775M[i]):
        #             z4.append(cat_lines[num_params+i].split())
        # libs.jtools.write_table(b435_drops,header,cwd + b435_cat_dir,"B435 Drops","4<=z<=6",verbose=True)
        libs.jtools.write_table(v606_drops,header,cwd + v606_cat_dir,"V606 Drops","4<=z<=6",verbose=True)
        # libs.jtools.write_table(i775_drops,header,cwd + i775_cat_dir,"I775 Drops","4<=z<=6",verbose=True)
        # libs.jtools.write_table(z4,header,cwd + z4_cat_dir,"Z~4","Z~4",verbose=True)
        # libs.jtools.write_table(z5,header,cwd + z5_cat_dir,"Z~5","Z~5",verbose=True)
        # libs.jtools.write_table(z6,header,cwd + z6_cat_dir,"Z~6","Z~6",verbose=True)
        # libs.jtools.write_table(z7,header,cwd + z7_cat_dir,"Z~7","Z~7",verbose=True)

        if COLOR_COLOR_C:
            #B_colors = [[Bvz,Bbv]]
            VC_colors = [[Viz,Vvi]]
            #I_colors = [[Ivz,Iiz]]

            # Candels Data (photom catalog)
            [v606_matchF,i775_matchF,z850_matchF] = libs.jastro.param_get('TestCatalogs/My606vsCandels.cat',[17+27,20+27,26+27],2)
            [v606_matchM,i775_matchM,z850_matchM] = [libs.jastro.flux_list2mag(xx,23.9) for xx in [v606_matchF,i775_matchF,z850_matchF]]
            VMiz = libs.jtools.list_operate(i775_matchM,z850_matchM,'-')
            VMvi = libs.jtools.list_operate(v606_matchM,i775_matchM,'-')
            VM_colors = [[VMiz,VMvi]]


            # Candels Data (photz catalog)
            [v606_mF,i775_mF,z850_mF] = libs.jastro.param_get('TestCatalogs/My606vsCandelsPhotz.cat',[16,20,24],1)
            [v606_mM,i775_mM,z850_mM] = [libs.jastro.flux_list2mag(xx,23.9) for xx in [v606_mF,i775_mF,z850_mF]]
            VmMiz = libs.jtools.list_operate(i775_mM,z850_mM,'-')
            VmMvi = libs.jtools.list_operate(v606_mM,i775_mM,'-')
            VmM_colors = [[VmMiz,VmMvi]]




            # libs.jastro.color_color([B_colors],'V-Z','B-V','*Candels* B435 Drop Outs -- {} Detected'.format(len(b435_drops)),
            #                         xthresh=1.6,ythresh=1.1,xlim=[-1,4],ylim=[-1,6],
            #                         a=1.1,b=1.0,graphall='yes')
            libs.jastro.color_color([VC_colors,V_colors,VM_colors],'I-Z','V-I','V606 Drop Outs (Mine vs. Candels photom vs. Candels photz',
                                   xthresh=1.3,ythresh=1.2,xlim=[-1,4],ylim=[-1,6],
                                   a=1.47,b=0.89,graphall='yes')

            libs.jastro.color_color([VmM_colors],'I-Z','V-I','My catalog matched against Candels photz',
                                   xthresh=1.3,ythresh=1.2,xlim=[-1,4],ylim=[-1,6],
                                   a=1.47,b=0.89,graphall='yes')

            # xx = [V_colors,VC_colors]
            # for n,i in enumerate(xx):
            #     for (a,b) in i:
            #         matplotlib.pyplot.plot(a,b,'ro' if n == 0 else 'go')

            #matplotlib.pyplot.plot(VC_colors,'go')


            # Plotting redshift distribution
            candelsZ = libs.jastro.param_get('TestCatalogs/MineVsCandelsZFull.cat',[37],2)
            matplotlib.pyplot.figure()
            matplotlib.pyplot.hist(candelsZ, bins=[0,1,2,3,4,5,6,7,8])
            matplotlib.pyplot.title('Redshift Distribution')
            matplotlib.pyplot.xlabel('Redshift')
            matplotlib.pyplot.ylabel('Num. Targets')
            matplotlib.pyplot.grid(True)


            show()


    if MY_COLORS_VS_C:
        [my_v,my_i,my_z] = libs.jastro.param_get('TestCatalogs/MasterVsCandels.cat',[18,22,26],2)
        [fc_v, fc_i, fc_z ] = libs.jastro.param_get('TestCatalogs/MasterVsCandels.cat',
                                                 [27+17,27+20,27+26],2)
        [c_v, c_i, c_z ] = [libs.jastro.flux_list2mag(xx) for xx in [fc_v, fc_i, fc_z ]]

        my_h = libs.jastro.param_get('TestCatalogs/MasterVsCandels.cat',[10],2)[0]

        x_del_vi = libs.jtools.list_operate(libs.jtools.list_operate(my_v,my_i,'-'),libs.jtools.list_operate(c_v,c_i,'-'),'-')
        x_del_iz = libs.jtools.list_operate(libs.jtools.list_operate(my_i,my_z,'-'),libs.jtools.list_operate(c_i,c_z,'-'),'-')

        #Filter everything larger than 20
        del_vi = [ ]
        del_iz = [ ]
        my_h_vi= [ ]
        my_h_iz= [ ]
        for n,a in enumerate(x_del_vi):
            if abs(a) <= 20 and my_h[n] < 95:
                del_vi.append(a)
                my_h_vi.append(my_h[n])
        for n,a in enumerate(x_del_iz):
            if abs(a) <= 20 and my_h[n] < 95:
                del_iz.append(a)
                my_h_iz.append(my_h[n])

        matplotlib.pyplot.figure()
        matplotlib.pyplot.plot(my_h_vi,del_vi,'r.')
        matplotlib.pyplot.ylabel('My Colors - Candels Colors (V-I)')
        matplotlib.pyplot.xlabel('H160 magnitude')
        matplotlib.pyplot.title('Difference in Colors \nMy(V-I)-Candels(V-I) vs H160 Magnitude')
        matplotlib.pyplot.grid(True)

        matplotlib.pyplot.figure()
        matplotlib.pyplot.plot(my_h_iz,del_iz,'r.')
        matplotlib.pyplot.ylabel('My Colors - Candels Colors (I-Z)')
        matplotlib.pyplot.xlabel('H160 magnitude')
        matplotlib.pyplot.title('Difference in Colors \nMy(I-Z)-Candels(I-Z) vs H160 Magnitude')
        matplotlib.pyplot.grid(True)

        matplotlib.pyplot.show()


    t2 = time.time()
    print("\n##Total time elapsed in main.py: {:.2f} seconds".format(t2-t1))