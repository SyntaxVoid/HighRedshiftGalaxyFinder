import os
from matplotlib.pyplot import show
from GLOBALS import *
from libs.jastro import color_color
def run(title,catalog_dir,rms):
    cats = sorted([catalog_dir + c for c in os.listdir(catalog_dir)])
    for sel,cat in zip(SELECTIONS,cats):
        if "z" in sel or "i" in sel:
            continue
        with open(cat) as cat_data:
            x_ax = []
            y_ax = []
            cat_lines = cat_data.readlines()[header.count("#"):]
            for line in cat_lines:
                y_ax.append(float(line.split()[COLOR_COLOR_OPS[sel][0][0]]) \
                           -float(line.split()[COLOR_COLOR_OPS[sel][0][1]]))
                x_ax.append(float(line.split()[COLOR_COLOR_OPS[sel][1][0]]) \
                           -float(line.split()[COLOR_COLOR_OPS[sel][1][1]]))
        r = COLOR_RULES[sel]
        title = title.format(sel,"Using RMS Maps" if rms else "Not Using RMS Maps")
        color_color([[[x_ax,y_ax]]],r[0],r[1],title,
                    xthresh=r[2],ythresh=r[3],xlim=r[4],ylim=r[5],a=r[6],b=r[7],graphall=r[8])
    return


if __name__ == '__main__':
    #run("My {0} Selections ({1})","SelectedObjects/Mine/NONE/",False)
    #run("My {0} Selections ({1})","SelectedObjects/Mine/RMS/",True)
    show()
    run("Candels {0} Selections ({1})","SelectedObjects/Candels/NONE/",False)
    show()