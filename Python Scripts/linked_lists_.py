# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:33:20 2015

@author: Damian of Brooklyn
"""

# Linked Lists

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Cases
    # new is before old, and old has no before: new.before = None, new.after = old, old.before = new
    # new is after old, and old has no after: old.after = new, new.before = old, new.after = None
    # new is before old, and old has a before: insert(new,old.before)
    # new is after old, and old has an after: insert(new,old.after)
    
    #end of the line cases
    if newFrob.myName() >= atMe.myName() and atMe.getAfter() == None:
        newFrob.setAfter(None)
        newFrob.setBefore(atMe)
        atMe.setAfter(newFrob)
        return
    elif newFrob.myName() < atMe.myName() and atMe.getBefore() == None:
        newFrob.setBefore(None)
        newFrob.setAfter(atMe)
        atMe.setBefore(newFrob)
        return
    # middle cases
    if newFrob.myName() > atMe.myName():
        after = atMe.getAfter()
        if newFrob.myName() <= after.myName():
            newFrob.setBefore(atMe)
            newFrob.setAfter(after)
            atMe.setAfter(newFrob)
            after.setBefore(newFrob)
            return
        else:
            insert(after,newFrob)
    if newFrob.myName() < atMe.myName():
        before = atMe.getBefore()
        if newFrob.myName() >= before.myName():
            newFrob.setBefore(before)
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
            before.setAfter(newFrob)
            return
        else:
            insert(before,newFrob)
    if newFrob.myName() == atMe.myName():
        before = atMe.getBefore()
        newFrob.setBefore(before)
        newFrob.setAfter(atMe)
        before.setAfter(newFrob)
        atMe.setBefore(newFrob)
        return

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore() == None:
        print start.myName()
    else:
        findFront(start.getBefore())
        
        
# tests
        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        