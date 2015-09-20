import functions
import pyfits
import os




if __name__ == '__main__':
    CONVERSION = 4.611764706 * pow(10,10)
# To convert nW . m^-2 . sr^-1 to uJy
#
#  nW    1      1 W             1 sr             (0.14 arcsec)^2      1         1 Jy              10^6 uJy
# --- x --- x ------- x -------------------  x  ------------------ x --- x ------------------- x ---------
# m^2    sr   10^9 nW   4.25*10^10 arcsec^2        (1 pixel)^2        f    10^-26 W.m^-2.Hz^-1     1 Jy
#
#                          1
# = 4.611764706 * 10^10 x --- uJy
#                          f

    f1 = 'HalfMaps/gs_f125w_half1_cropcal.fits'
    f2 = 'HalfMaps/gs_f125w_half2_cropcal.fits'
    f3 = 'HalfMaps/gs_f160w_half1_cropcal.fits'
    f4 = 'HalfMaps/gs_f160w_half2_cropcal.fits'
    f5 = 'HalfMaps/gs_f606w_half1_cropcal.fits'
    f6 = 'HalfMaps/gs_f606w_half2_cropcal.fits'
    f7 = 'HalfMaps/gs_f775w_half1_cropcal.fits'
    f8 = 'HalfMaps/gs_f775w_half2_cropcal.fits'
    f9 = 'HalfMaps/gs_f850l_half1_cropcal.fits'
    f10= 'HalfMaps/gs_f850l_half2_cropcal.fits'

    # Central wavelengths were found from http://www.stsci.edu/hst/wfc3/documents/ISRs/2003/WFC3-2003-07.pdf
    # and http://etc.stsci.edu/etcstatic/users_guide/appendix_b_acs.html
    center_f125w = 12449.36
    center_f160w = 15405.16
    center_f606w =  5917.7
    center_f775w =  7693.0
    center_f850l =  9145.2

    print("---f125w---")
    functions.fits_add([f1,f2], 'FullMaps/gs_f125w_cropcal.fits', header_index = 1, conversion_factor = CONVERSION/center_f125w)


    print("---f160w---")
    functions.fits_add([f3,f4], 'FullMaps/gs_f160w_cropcal.fits', header_index = 1, conversion_factor = CONVERSION/center_f160w)


    print("---f606w---")
    functions.fits_add([f5,f6], 'FullMaps/gs_f606w_cropcal.fits', header_index = 1, conversion_factor = CONVERSION/center_f606w)

    print("---f775w---")
    functions.fits_add([f7,f8], 'FullMaps/gs_f775w_cropcal.fits', header_index = 1, conversion_factor = CONVERSION/center_f775w)

    print("---f850l---")
    functions.fits_add([f9,f10],'FullMaps/gs_f850l_cropcal.fits', header_index = 1, conversion_factor = CONVERSION/center_f850l)
