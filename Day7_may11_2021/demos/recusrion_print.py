def rec_increment(p):
    if len(p) == 0:
        return ""
    else:
        #r = list(p)
        print(p[0])
        return rec_increment(p[1:])

rec_increment([1,2,3,4])