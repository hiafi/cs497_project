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
class Point:
    #---------------------------------------------------------------------------
    def __init__(self, coords, reference=None):
        """
            coords -- coordinates of point in a list
            reference -- Type of data.
        """
        self.coords = coords
        self.n = len(coords)
        self.reference = reference 

    #---------------------------------------------------------------------------
    def __repr__(self):
        return str(self.coords)


