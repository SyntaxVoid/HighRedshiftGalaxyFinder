
from GLOBALS import *
from libs.jastro import mag_errors,plot_mag_errors
from matplotlib.pyplot import show

def run():
    print("\n" + "="*80)
    print("="*25 + "Now Compiling Magnitude Errors" + "="*25)
    print("="*80 + "\n")
    xlab = "My Magnitude"
    ylab = "Candels Magnitude - My Magnitude"
    for f in FILTERS:
        [m,p,d] = mag_errors("Matches/Cats/Matched_{}.cat".format(f),4,PUB_COL_DICT[f],2,eval("ZP_{}".format(f)))
        plot_mag_errors(m,d,title="{} Magnitude Errors".format(f.upper()),xlabel=xlab,ylabel=ylab)
    show()
    return

if __name__ == '__main__':
    run()