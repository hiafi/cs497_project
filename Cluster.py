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
import Point

#-------------------------------------------------------------------------------
class Cluster:
    #---------------------------------------------------------------------------
    def __init__(self, points):
        #Check if cluster is empty
        if ( len(points) == 0 ):
            raise Exception("ILLEGAL: empty cluster")

        #Check if all points in cluster are the same dimensions
        self.points = points
        self.n = points[0].n
        for p in points:
            if ( p.n != self.n):
                raise Exception("ILLEGAL: wrong dimensions")
        
        self.centroid = self.calculateCentroid()

    #---------------------------------------------------------------------------
    def __repr__(self):
        return str(self.points)

    #---------------------------------------------------------------------------
    def update(self, points, distanceFormula):
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        return distanceFormula(old_centroid, self.centroid)

    #---------------------------------------------------------------------------
    def calculateCentroid(self):
        reduce_coord = lambda i:reduce(lambda x,p : x + p.coords[i], self.points, 0.0)
        centroid_coords = [reduce_coord(i) /  len(self.points) for i in range(self.n)]
        return Point.Point(centroid_coords)
