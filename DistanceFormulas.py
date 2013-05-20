#!/usr/bin/python
#--------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------
#   Credits to pandoricweb.tumblr.com/post/8646701677/python-implementation-of
#   -k-means-clustering for source code
#-------------------------------------------------------------------------------
import Cluster
import Point

#-------------------------------------------------------------------------------
def kmeans(points, k, cutoff, distanceFormula):
    """
        points  -- a set of coordinates
        k       -- k value for k mean
        cutoff  -- value to cutoff poitns
        distanceFormula     -- Distance function to find distance
    """
    initial = random.sample(points, k)
    clusters = [Cluster.Cluster([p]) for p in initial]

    while True:
        lists = [ [] for c in clusters]
        for p in points:
            smallest_distance = distanceFormula(p, clusters[0].centroid)
            index = 0
            for i in range(len(clusters[1:])):
                distance = distanceFormula(p, clusters[i + 1].centroid)
                if ( distance < smallest_distance ):
                    smallest_distance = distance
                    index = i + 1
            lists[index].append(p)
        
        biggest_shift = 0.0
        for i in range(len(clusters)):
            shift = clusters[i].update(lists[i], distanceFormula)
            biggest_shift = max(biggest_shift, shift)

        if ( biggest_shift < cutoff ):
            break

    return clusters

#-------------------------------------------------------------------------------
def EuclideanDistance(a, b):
    if ( a.n != b.n ):
        raise Exception("ILLEGAL: non-comparable points")

    ret = reduce(lambda x,y: x + pow((a.coords[y] - b.coords[y]), 2), range(a.n), 0.0)
    return math.sqrt(ret)
