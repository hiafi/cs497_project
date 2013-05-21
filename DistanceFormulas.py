#!/usr/bin/python
#--------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#-------------------------------------------------------------------------------
def EuclideanDistance(a, b):
    if ( a.n != b.n ):
        raise Exception("ILLEGAL: non-comparable points")

    ret = reduce(lambda x,y: x + pow((a.coords[y] - b.coords[y]), 2), range(a.n), 0.0)
    return math.sqrt(ret)
