# ##                         ## #
#  Authored by John Gresl 2015  #
# ##                         ## #


import libs.jastro
import pyfits

C = 299792458.  # speed of light m/s
CONVERSION = 46117.647060 * pow(10,6)

# To convert nW . m^-2 . sr^-1 to Jy
#
#  nW    1      1 W             1 sr             (0.14 arcsec)^2      1         1 Jy                10^6 uJy
# --- x --- x ------- x -------------------  x  ------------------ x --- x -------------------  x  ----------
# m^2    sr   10^9 nW   4.25*10^10 arcsec^2        (1 pixel)^2        f    10^-26 W.m^-2.Hz^-1        1 Jy
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


def tinker_factor(delta):
    return pow(10., delta/2.5)


center_f125w = C/(12449.36*pow(10, -10)) * tinker_factor(0.0)
center_f160w = C/(15405.16*pow(10, -10)) * tinker_factor(0.0)
center_f606w = C/( 5917.7 *pow(10, -10)) * tinker_factor(1.8)
center_f775w = C/( 7693.0 *pow(10, -10)) * tinker_factor(1.9)
center_f850l = C/( 9145.2 *pow(10, -10)) * tinker_factor(1.7)


def run():
    print("\n" + "="*80)
    print("="*27 + "Now Compiling .fits Images" + "="*27)
    print("="*80 + "\n")
    filters = ["f125w","f160w","f435w","f606w","f775w","f850l"]
    file_str = "HalfMaps/gs_{0}_half{1}_cropcal.fits"
    for f in filters:
        print("#Compiling FullMaps/gs_{}_cropcal.fits".format(f))
        if f != "f435w":
            libs.jastro.fits_add([file_str.format(f,"1"),file_str.format(f,"2")],
                                 "FullMaps/gs_{}_cropcal.fits".format(f),
                                 header_index=1, conversion_factor=CONVERSION/eval("center_{}".format(f)))
        else:
            b435 = pyfits.open('HalfMaps/gs_f435w_cropcal.fits')
            b435data = b435[0].data * tinker_factor(2.2)
            b435head = b435[0].header
            pyfits.writeto('FullMaps/gs_f435w_cropcal.fits',b435data,b435head,clobber=1)
    print("\n" + ("="*80 + "\n")*3)
    return


if __name__ == '__main__':
    run()
