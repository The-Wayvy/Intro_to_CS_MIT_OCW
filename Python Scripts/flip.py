# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:28:58 2015

@author: Damian of Brooklyn
"""

"""
Lectures between Roomba and Virus simulations
"""

import numpy
import pylab
import random

#==============================================================================
# def flip(numFlips):
#     heads = 0
#     for i in range(numFlips):
#         if random.random() < 0.5:
#             heads += 1
#     return heads/float(numFlips)
# 
# def flipSim(numFlipsPerTrial, numTrials):
#     fracHeads = []
#     for i in range(numTrials):
#         fracHeads.append(flip(numFlipsPerTrial))
#     mean = sum(fracHeads)/float(len(fracHeads))
#     return (mean)
# 
# 
# def flipPlot(minExp, maxExp):
#     ratios = []
#     diffs = []
#     xAxis = []
#     for exp in range(minExp, maxExp + 1):
#         xAxis.append(2**exp)
#     for numFlips in xAxis:
#         numHeads = 0
#         for n in range(numFlips):
#             if random.random() < 0.5:
#                 numHeads += 1
#         numTails = numFlips - numHeads
#         ratios.append(numHeads/float(numTails))
#         diffs.append(abs(numHeads - numTails))
#     pylab.title('Difference Between Heads and Tails')
#     pylab.xlabel('Number of Flips')
#     pylab.ylabel('Abs(#Heads - #Tails')
#     pylab.plot(xAxis, diffs)
#     pylab.figure()
#     pylab.plot(xAxis, ratios)
#     pylab.title('Heads/Tails Ratios')
#     pylab.xlabel('Number of Flips')
#     pylab.ylabel('Heads/Tails')
#     pylab.figure()
#     pylab.title('Difference Between Heads and Tails')
#     pylab.xlabel('Number of Flips')
#     pylab.ylabel('Abs(#Heads - #Tails')
#     pylab.plot(xAxis, diffs, 'bo')
#     pylab.semilogx()
#     pylab.semilogy()
#     pylab.figure()
#     pylab.plot(xAxis, ratios, 'bo')
#     pylab.title('Heads/Tails Ratios')
#     pylab.xlabel('Number of Flips')
#     pylab.ylabel('Heads/Tails')
#     pylab.semilogx()
# 
# flipPlot(4, 20)
# pylab.show()
#==============================================================================

X = numpy.arange(101)
Y = X**2
print X
print Y
pylab.subplot(211)
pylab.plot(X,Y,'y-')
pylab.semilogy()
pylab.subplot(212)
pylab.plot(X,Y,'y-')
pylab.show()








