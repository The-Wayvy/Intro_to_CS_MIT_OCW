# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:47:09 2015

@author: Damian of Brooklyn
"""
class Meow(Exception):
    """an exception"""

def add_x(X,y):
    """adds all elements in X, equal to y, to a list Z """
    Z = []
    for x in X:
        try:
            if x == y:
                Z.append(x)
            else:
                raise Meow
        except:
            next
    return Z

#print add_x([1,2,3,4,1],1)


try:
    x = Meow
except:
    print "ok"
            