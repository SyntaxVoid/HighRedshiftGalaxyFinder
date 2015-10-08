import functions

if __name__ == '__main__':
    test_f = 'Matches/Cats/Matched_f850l.cat'
    x = functions.param_get(test_f,[34,35],2)
    print(x[0][0],x[1][0])
    pass