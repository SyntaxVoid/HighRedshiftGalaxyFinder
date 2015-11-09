from __future__ import print_function
import sys
sys.dont_write_bytecode = True
# The above stops the cluttering of source folder with .pyc files

import os
cwd = os.getcwd()
import matplotlib.pyplot
from matplotlib.pyplot import show


import libs.jastro
import libs.jtools
import RMSCompile
import FitsCompile
import CatCompile
import SelectionCriteria

# My color - Candels Color (Use V-I and I-Z as color) as a function of H-band magnitude


# ADJUSTED ZERO POINTS (ZP for uJy is 23.9)
ZP_f125w = 23.9#+0.0
ZP_f160w = 23.9#+0.0
ZP_f435w = 23.9#+2.2
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

if __name__ == '__main__':
    EXPOSURE       = 0  # Compiles the RMS maps from the EXPOSURE maps
    FITS           = 0  # Compiles Fits Files
    CATS           = 0  # Creates catalogs using SExtractor
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
        print('. . .Compiling Fits Images. . .')
        FitsCompile.run()
        print ('-'*28)

    if CATS:
        print('. . .Compiling Catalogs. . .')
        CatCompile.run()
        libs.jastro.combine_catalogs(header,
                                     sorted(['Catalogs/'+ f for f in os.listdir('Catalogs/')]),[2,3,4,5,6,7],8,
                                     "master.cat",
                                     conversion_factor = 1)

        print('-'*28)
    if ERRORS:
        FLUX_OR_MAG = 'flux'
        print('. . .Compiling Magnitudes and Errors. . .')

        print("\n"+"="*10+"F125W Magnitude Errors"+"="*10)
        libs.jastro.mag_errors('Matches/Cats/Matched_f125w.cat',FLUX_OR_MAG,4,42,2,ZP_f125w,['stats','plot'])

        print("\n"+"="*10+"F160W Magnitude Errors"+"="*10)
        libs.jastro.mag_errors('Matches/Cats/Matched_f160w.cat',FLUX_OR_MAG,4,45,2,ZP_f160w,['stats','plot'])

        print("\n"+"="*10+"F435W Magnitude Errors"+"="*10)
        libs.jastro.mag_errors('Matches/Cats/Matched_f435w.cat',FLUX_OR_MAG,4,21,2,ZP_f160w,['stats','plot'])

        print("\n"+"="*10+"F606W Magnitude Errors"+"="*10)
        libs.jastro.mag_errors('Matches/Cats/Matched_f606w.cat',FLUX_OR_MAG,4,24,2,ZP_f606w,['stats','plot'])

        print("\n"+"="*10+"F775W Magnitude Errors"+"="*10)
        libs.jastro.mag_errors('Matches/Cats/Matched_f775w.cat',FLUX_OR_MAG,4,27,2,ZP_f775w,['stats','plot'])

        print("\n"+"="*10+"F850L Magnitude Errors"+"="*10)
        libs.jastro.mag_errors('Matches/Cats/Matched_f850l.cat',FLUX_OR_MAG,4,33,2,ZP_f850l,['stats','plot'])
        show() # To stop the windows from immediately being closed at end of script

    if SELECT_ME:
        print("\n" + "="*80)
        num_params = header.count('\n')  # Length (in lines) of the header of the catalog
        b435_cat_dir = "/SelectedObjects/Mine/b435.cat"
        v606_cat_dir = "/SelectedObjects/Mine/v606.cat"
        i775_cat_dir = "/SelectedObjects/Mine/i775.cat"
        z7_cat_dir   = "/SelectedObjects/Mine/z7.cat"
        z6_cat_dir   = "/SelectedObjects/Mine/z6.cat"
        z5_cat_dir   = "/SelectedObjects/Mine/z5.cat"
        z4_cat_dir   = "/SelectedObjects/Mine/z4.cat"

        # Flux Values and Errors:
        [j125F,h160F,b435F,v606F,i775F,z850F] = \
            libs.jastro.param_get('master.cat',[4,8,12,16,20,24],28)
        [b125Ferr,b160Ferr,b435Ferr,v606Ferr,i775Ferr,z850Ferr] = \
            libs.jastro.param_get('master.cat',[5,9,13,17,21,25],28)
        # Mag values
        [j125M,h160M,b435M,v606M,i775M,z850M] = \
            libs.jastro.param_get('master.cat',[6,10,14,18,22,26],28)

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

        with open('master.cat') as cat_data:
            cat_lines = cat_data.readlines()
            num_lines = len(cat_lines)-num_params
            for i in range(num_lines):
                # B435 Drops (Must wait for b435 data)
                if SelectionCriteria.b435_dropout(b435M[i],v606M[i],i775M[i],z850M[i],
                                                  (v606F[i]/v606Ferr[i]),(i775F[i]/i775Ferr[i])):
                    b435_drops.append(cat_lines[i+num_params].split())
                    Bbv.append(b435M[i]-v606M[i])
                    Bvz.append(v606M[i]-z850M[i])

                # V606 Drops (Must wait for b435 data)
                if SelectionCriteria.v606_dropout(b435M[i],v606M[i],i775M[i],z850M[i],
                                                    (z850F[i]/z850Ferr[i]),(b435F[i]/b435Ferr[i])):
                    v606_drops.append(cat_lines[i+num_params].split())
                    Vvi.append(v606M[i]-i775M[i])
                    Viz.append(i775M[i]-z850M[i])

        #         # I775 Drops
                if SelectionCriteria.i775_dropout(v606M[i],i775M[i],z850M[i],
                                                    (z850F[i]/z850Ferr[i]),(v606F[i]/v606Ferr[i]),i):
                    i775_drops.append(cat_lines[num_params+i].split())
                    Iiz.append(i775M[i]-z850M[i])
                    Ivz.append(v606M[i]-z850M[i])

                # We need to check backwords from Z~7 to Z~4 to make sure we don't double
                # count any galaxies.
                # z~7
                elif SelectionCriteria.z7(j125M[i],j125M[i],h160M[i],i775M[i],z850M[i],
                                          (b435F[i]/b435Ferr[i]),(v606F[i]/v606Ferr[i]),
                                          (i775F[i]/i775Ferr[i]),(i775F[i]/i775Ferr[i])):
                    z7.append(cat_lines[num_params+i].split())

                #z~6
                elif SelectionCriteria.z6(j125M[i],j125M[i],h160M[i],v606M[i],i775M[i],i775M[i],z850M[i],
                                          b435F[i]/b435Ferr[i],v606F[i]/v606Ferr[i],i775F[i]/i775Ferr[i]):
                    z6.append(cat_lines[num_params+i].split())

                #z~5
                elif SelectionCriteria.z5(h160M[i],v606M[i],i775M[i],z850M[i],b435F[i]/b435Ferr[i]):
                    z5.append(cat_lines[num_params+i].split())

                #z~4
                elif SelectionCriteria.z4(j125M[i],b435M[i],v606M[i],i775M[i]):
                    z4.append(cat_lines[num_params+i].split())
        libs.jtools.write_table(b435_drops,header,cwd + b435_cat_dir,"B435 Drops","4<=z<=6",verbose=True)
        libs.jtools.write_table(v606_drops,header,cwd + v606_cat_dir,"V606 Drops","4<=z<=6",verbose=True)
        libs.jtools.write_table(i775_drops,header,cwd + i775_cat_dir,"I775 Drops","4<=z<=6",verbose=True)
        libs.jtools.write_table(z4,header,cwd + z4_cat_dir,"Z~4","Z~4",verbose=True)
        libs.jtools.write_table(z5,header,cwd + z5_cat_dir,"Z~5","Z~5",verbose=True)
        libs.jtools.write_table(z6,header,cwd + z6_cat_dir,"Z~6","Z~6",verbose=True)
        libs.jtools.write_table(z7,header,cwd + z7_cat_dir,"Z~7","Z~7",verbose=True)

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
        matplotlib.pyplot.xlabel('My Colors - Candels Colors (V-I)')
        matplotlib.pyplot.ylabel('H160 magnitude')
        matplotlib.pyplot.title('Difference in Colors \nMy(V-I)-Candels(V-I) vs H160 Magnitude')
        matplotlib.pyplot.grid(True)

        matplotlib.pyplot.figure()
        matplotlib.pyplot.plot(my_h_iz,del_iz,'r.')
        matplotlib.pyplot.xlabel('My Colors - Candels Colors (I-Z)')
        matplotlib.pyplot.ylabel('H160 magnitude')
        matplotlib.pyplot.title('Difference in Colors \nMy(I-Z)-Candels(I-Z) vs H160 Magnitude')
        matplotlib.pyplot.grid(True)

        matplotlib.pyplot.show()