# ##                         ## #
#  Authored by John Gresl 2015  #
# ##                         ## #


import libs.jastro

C = 299792458.  # speed of light m/s
CONVERSION = 46117.647060

# To convert nW . m^-2 . sr^-1 to Jy
#
#  nW    1      1 W             1 sr             (0.14 arcsec)^2      1         1 Jy
# --- x --- x ------- x -------------------  x  ------------------ x --- x -------------------
# m^2    sr   10^9 nW   4.25*10^10 arcsec^2        (1 pixel)^2        f    10^-26 W.m^-2.Hz^-1
#
#                     1
# = 46117.640760  x  --- Jy
#                     f

f0 = 'HalfMaps/gs_f125w_half1_cropcal.fits'
f1 = 'HalfMaps/gs_f125w_half2_cropcal.fits'
f2 = 'HalfMaps/gs_f160w_half1_cropcal.fits'
f3 = 'HalfMaps/gs_f160w_half2_cropcal.fits'
f4 = 'HalfMaps/gs_f606w_half1_cropcal.fits'
f5 = 'HalfMaps/gs_f606w_half2_cropcal.fits'
f6 = 'HalfMaps/gs_f775w_half1_cropcal.fits'
f7 = 'HalfMaps/gs_f775w_half2_cropcal.fits'
f8 = 'HalfMaps/gs_f850l_half1_cropcal.fits'
f9 = 'HalfMaps/gs_f850l_half2_cropcal.fits'

# Central wavelengths were found from http://www.stsci.edu/hst/wfc3/documents/ISRs/2003/WFC3-2003-07.pdf
# and http://etc.stsci.edu/etcstatic/users_guide/appendix_b_acs.html
center_f125w = C/(12449.36*pow(10, -10))
center_f160w = C/(15405.16*pow(10, -10))
center_f606w = C/(5917.7*pow(10, -10))
center_f775w = C/(7693.0*pow(10, -10))
center_f850l = C/(9145.2*pow(10, -10))


def tinker_factor(delta):
    return pow(10., delta/2.5)


def run():
    print("---f125w---")
    libs.jastro.fits_add([f0, f1],
                         'FullMaps/gs_f125w_cropcal.fits',
                         header_index=1,
                         conversion_factor=CONVERSION/center_f125w)

    print("---f160w---")
    libs.jastro.fits_add([f2, f3],
                         'FullMaps/gs_f160w_cropcal.fits',
                         header_index=1,
                         conversion_factor=CONVERSION/center_f160w)

    print("---f606w---")
    libs.jastro.fits_add([f4, f5],
                         'FullMaps/gs_f606w_cropcal.fits',
                         header_index=1,
                         conversion_factor=CONVERSION*tinker_factor(1.8)/center_f606w)

    print("---f775w---")
    libs.jastro.fits_add([f6, f7],
                         'FullMaps/gs_f775w_cropcal.fits',
                         header_index=1,
                         conversion_factor=CONVERSION*tinker_factor(1.9)/center_f775w)

    print("---f850l---")
    libs.jastro.fits_add([f8, f9],
                         'FullMaps/gs_f850l_cropcal.fits',
                         header_index=1,
                         conversion_factor=CONVERSION*tinker_factor(1.7)/center_f850l)

    return
