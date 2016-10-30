# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:44:43 2015

@author: Damian of Brooklyn
"""
import pylab
import numpy
import random


#==============================================================================
# pylab.plot([1,2,3,4],[8,8,8,8],':r8')
# pylab.plot([1,2,3,4],[9,7,9,7],'+-.m')
# pylab.axis([1,4,0,12])
# pylab.xticks(range(1,5))
# pylab.yticks(range(6,10))
# pylab.show()
#==============================================================================


#what if i want to change formatting for different parts of the line?


def plot_function(f,x):
    """x: list of values to pass into the function
    f: an integer function with a get_name method
    plots the f(x)"""
    f_x = []
    for value in x:
        y_value = f(value)
        f_x.append(y_value)
    pylab.plot(x,f_x,'-*g')
    pylab.xlabel('x')
    pylab.ylabel('f(x)')
    pylab.title('a function')
    pylab.xticks(x)
    pylab.yticks(range(min(f_x),max(f_x)+1))
    pylab.show()
    
def cube(x):
    """x: int
    returns x**3"""
    return x**3
    
#==============================================================================
# X = numpy.arange(1,2,.01)
# #Like range, but can take floats as a step
# print X
#==============================================================================
    
Y = numpy.arange(1.0,11.0,.01)
pylab.plot(Y,Y**-1,'c-',Y,Y**-2,'y-',Y,Y**-3,'g-')
pylab.axis([0,10,0,1])
pylab.title('negative exponents')
pylab.yticks(numpy.arange(0.0,1.0,.05))
pylab.xticks(range(11))
pylab.grid(True,axis='y')
pylab.text(7.0,.665,'Valerie Xu',color='blue')
pylab.annotate('sensitive5',xy=(7.0,.665),xytext=(5.0,.9),arrowprops=dict(facecolor='red',shrink=.005))
pylab.legend(['x^-1', 'x^-2', 'x^-3'])        
#==============================================================================
# 
# X = pylab.plot([1,2,3],[7,8,2])
# pylab.setp(X)
# pylab.setp(X,color='r',marker='o',mfc='y',markersize=10.0,linewidth=5.0)
# pylab.show()
#==============================================================================

#==============================================================================
# pylab.figure(1)
# pylab.subplot(221)
# pylab.plot([1,2,3],[4,5,6],'k')
# pylab.subplot(222)
# pylab.plot([1,2,3],[6,5,4],'b')
# pylab.subplot(224)
# pylab.plot([1,2,3],[3,4,3],'g')
# pylab.subplot(223)
# pylab.plot([1,2,3],[19,7,6],'y')
# pylab.subplot(111)
# pylab.plot([1,2,3],[1,2,3],'o')
# pylab.figure(2)
# pylab.plot([2,3],[1,2])
# pylab.figure(1)
# pylab.close()
# pylab.show()
#==============================================================================
























