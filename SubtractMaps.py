import pyfits
from GLOBALS import *

def run():
    for map1,map2,dest in zip(MY_MAPS,CANDELS_MAPS,SUB_DEST):
        with pyfits.open(map1) as mp1, pyfits.open(map2) as mp2:
            d1 = mp1[0].data
            d2 = mp2[0].data
            hd = mp1[0].header
            dif = d1-d2
            pyfits.writeto(dest,dif,hd,clobber=True)
    return



if __name__ == '__main__':
    run()