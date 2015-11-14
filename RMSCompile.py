import os

import numpy
import pyfits

import libs.jastro



def run():
    print("\n" + "="*80)
    print("="*29 + "Now Compiling RMS Maps" + "="*29)
    print("="*80 + "\n")
    f_list = sorted(['HalfExposureMaps/' + f for f in os.listdir('HalfExposureMaps/')])
    out_dir = 'FullRMSMaps/'
    n = len(f_list)
    for i in range(0,n,2):
        f1 = f_list[i]
        f2 = f_list[i+1]
        with pyfits.open(f1) as f1o:
            with pyfits.open(f2) as f2o:
                print("#Compiling FullMaps_gs_{}_rms.fits".format(f1[17:25]))
                f1data = f1o[0].data
                f2data = f2o[0].data
                head = f1o[0].header
                total  = f1data+f2data
                with numpy.errstate(divide='ignore', invalid='ignore'):
                    nptotal = numpy.array(total)
                    rms = 1 / numpy.sqrt(nptotal)
                    rms[rms == numpy.inf] = 1
                    rms = numpy.nan_to_num(rms)
                pyfits.writeto(out_dir+f1[17:25]+"_rms.fits",rms,clobber=True,header=head)
    print("\n" + ("="*80 + "\n")*3)
    return


if __name__ == '__main__':
    run()