def rtraverse(seq, i=0):
    if i < len(seq):
        print(seq[i])
        rtraverse(seq, i+1)

rtraverse([1, 2, 3, 4])
