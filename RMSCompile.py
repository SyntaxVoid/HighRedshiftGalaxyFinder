import os

import numpy
import pyfits

import libs.jastro



def run():
    f_list = sorted(['HalfExposureMaps/' + f for f in os.listdir('HalfExposureMaps/')])
    out_dir = 'FullRMSMaps/'
    n = len(f_list)
    for i in range(0,n,2):
        f1 = f_list[i]
        f2 = f_list[i+1]
        with pyfits.open(f1) as f1o:
            with pyfits.open(f2) as f2o:
                f1data = f1o[0].data
                f2data = f2o[0].data
                head = f1o[0].header
                total  = f1data+f2data
                with numpy.errstate(divide='ignore', invalid='ignore'):
                    nptotal = numpy.array(total)
                    rms = 1 / numpy.sqrt(nptotal)
                    rms[rms == numpy.inf] = 0
                    rms = numpy.nan_to_num(rms)

                pyfits.writeto(out_dir+f1[17:25]+"_rms.fits",rms,clobber=True,header=head)
    return


if __name__ == '__main__':
    run()