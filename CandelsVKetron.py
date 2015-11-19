import matplotlib.pyplot as plt
import numpy as np

def _plot(x,y,**kwargs):
    xlin = np.linspace(-40,40)
    plt.figure()
    plt.plot(x,y,'go')
    plt.plot(xlin,xlin,'r-')
    plt.xlabel(kwargs["xlab"])
    plt.ylabel(kwargs["ylab"])
    plt.xlim(-5,max(x)+5)
    plt.ylim(-5,max(y)+5)
    plt.title(kwargs["title"])
    plt.grid()

    return

def run(catalog,title):
    my_flux_col = 3
    candels_flux_col = 3 + 20
    my = [ ]
    dif = [ ]
    with open(catalog) as cat_data:
        cat_lines = cat_data.readlines()
        for obj in cat_lines:
            if obj[0] == "#":
                continue
            myF = float(obj.split()[my_flux_col])
            candelsF= float(obj.split()[candels_flux_col])
            if abs(myF) > 40 or abs(candelsF) > 40:
                continue
            my.append(myF)
            dif.append(candelsF)
    _plot(my,dif,title=title,xlab="My i-Band Flux",ylab="Candels i-Band Flux")
    return



if __name__ == '__main__':
    run("Matches/NONE/Matched_f775w.cat","Flux Comparisons\n(No RMS Map)")
    run("Matches/RMS/Matched_f775w.cat","Flux Comparisons\n(RMS Map)")
    plt.show()