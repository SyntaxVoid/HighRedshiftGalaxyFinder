from libs.jtools import check_list_type


def _real_values(v):
    # Returns true if all values in (v) have a |value| < 99.
    for i in v:
        if abs(i) == 99.:
            return False
    return True

def b435_dropout(b435,v606,i775,z850,SNv606,SNi775):
    # From Stark et. al.
    if not _real_values([b435,v606,i775,z850,SNv606,SNi775]):
        return False
    c1 = (b435 - v606) > (1.1 + v606 - z850)
    c2 = (b435 - v606) > (1.1)
    c3 = (v606 - z850) < 1.6
    c4 = SNv606 > 5
    c5 = SNi775 > 3
    return all([c1,c2,c3,c4,c5])


def v606_dropout(b435,v606,i775,z850,SNz850,SNb435):
    # From Stark et. al.
    if not _real_values(b435,v606,i775,z850,SNz850,SNb435):
        return False
    c1 = ((v606 - i775) > (1.47 + 0.89*(i775 - z850)) or (v606 - i775)  > 2)
    c2 = (v606 - i775) > (1.2)
    c3 = (i775 - z850) < (1.3)
    c4 = (SNz850) > (5)
    c5 = ((SNb435) < (2) or (b435 - i775) > (v606 - i775 + 1))
    return all([c1,c2,c3,c4,c5])


def i775_dropout(v606,i775,z850,SNz850,SNv606):
    # From Stark et. al.
    if not _real_values([v606,i775,z850,SNz850,SNv606]):
        return False
    c1 = (i775 - z850) > (1.3)
    c2 = (SNz850) > (5)
    c3 = ((SNv606) < 2 or (v606-z850) > (2.8))
    return all([c1,c2,c3])