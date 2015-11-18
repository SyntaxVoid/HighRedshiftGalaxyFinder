import time

from SelectionCriteria import *
from GLOBALS import *
from libs.jtools import write_table

def stats(drop,name,num_obj,lst):
    print("   #{:5d} objects out of {:5d} met the {:4s} dropout criteria from {}".format(len(lst),num_obj,drop,name))


def run(catalog,destination,col_dict,rms):
    print("\n" + "="*80)
    print("="*25 + "Now applying Selection Criteria"+ "="*24)
    print("="*80 + "\n")
    t1 = time.time()
    dir_str = destination + "{}/{}.cat"
    rms_or_none = "RMS" if rms else "NONE"
    out = [[],[],[],[],[],[],[],[]]
    with open(catalog,'r') as cat_file:
        cat_lines = cat_file.readlines()
        temp = 0
        for line in cat_lines:
            if line[0] == "#":
                temp += 1
                continue
            if b435_dropout(line,col_dict):
                out[0].append(line.split())
            if i775_dropout(line,col_dict):
                out[1].append(line.split())
            if v606_dropout(line,col_dict):
                out[2].append(line.split())
            if z4(line,col_dict):
                out[3].append(line.split())
            if z5(line,col_dict):
                out[4].append(line.split())
            if z6(line,col_dict):
                out[5].append(line.split())
            if z7(line,col_dict):
                out[6].append(line.split())
            if z8(line,col_dict):
                out[7].append(line.split())
        num_objects = len(cat_lines) - temp
    for n,s in enumerate(SELECTIONS):
        name = "Stark  et. al." if "z" not in s else "Bouwen et. al."
        stats(s,name,num_objects,out[n])
        write_table(out[n],header,dir_str.format(rms_or_none,s))
    t2 = time.time()
    print("#Catalogs written to: " + destination + rms_or_none + "/")
    print("#Time Elapsed: {:.2f} seconds".format(t2-t1))
    print("\n" + ("\n" + "="*80)*3)
    return out


if __name__ == '__main__':
    #run("masterNONE.cat","SelectedObjects/Mine/NONE/",MASTER_COL_DICT,False)
    #run("masterRMS.cat","SelectedObjects/Mine/RMS/",MASTER_COL_DICT,True)
    run("Candels_Catalog/CANDELS.GOODSS.F160W.v1_1.photom.cat","SelectedObjects/Candels/",MASTER_CANDELS_DICT,False)