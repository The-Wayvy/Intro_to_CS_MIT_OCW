# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:57:04 2015

@author: Damian of Brooklyn
"""

# Optimized Course Selection 

"""
Plan of Action
--------------------
~ make a Course class
    init with name, value, work
    make a __repr__ method    
~ make getVal, getWork, getRatio functions (take a Course instance)
~ make a print courses function (takes a list of courses)
~ make a load courses function (read in a text file and make a list of Course instances)

~ make a GreedyAdvisor function (takes a list Courses,maxWork,and Comparator)
~ make an OptimalAdvisor function (takes a list of Courses and maxWork)
"""


class Course(object):
    """a Course object"""
    def __init__(self,name,value,work):
        self.name = name
        self.value = value
        self.work = work
    def __repr__(self):
        return 'name: ' + self.name + '    ' + 'value: ' + str(self.value) + '    ' + 'work: ' + str(self.work)

def getVal(course):
    """returns a course object's value"""
    return course.value

def getWork(course):
    """returns the inverse of a course object's work"""
    return 1.0 / course.work
    
def getRatio(course):
    """returns a course object's value:work ratio"""
    return float(course.value)/course.work
    
def printCourses(list_of_courses):
    """list_of_courses: list of Course instances
    prints essential info"""
    total_work = 0
    total_val = 0  
    print 'COURSES'
    for course in list_of_courses:
        print course
        total_work += (1 / getWork(course))
        total_val += getVal(course)
    ratio = float(total_val)/(total_work)
    print 'total value: ' + str(total_val) + '    ' + 'total work: ' + str(total_work) + '    ' + 'overall ratio: ' + str(ratio) 

def loadCourses(filename):
    """takes a text file containing courses
    returns a list of Course instances"""
    course_catalog = []    
    course_file = open(filename,'r')    
    for course in course_file:
        course = course.split(',')
        course_catalog.append(Course(course[0],int(course[1]),int(course[2])))
    return course_catalog
    
def chooseGreedy(course_list,maxWork,sort_method):
    """Returns the optimal schedule as decided by a greedy algorithm
    course_list: list, a list of Course instances
    maxWork: int, max value for the total work required by the schedule
    sort_method: function, takes a Course instance returns val,1/work,or val:work ratio
    """
    thecourses = course_list[:]
    thecourses.sort(key=sort_method,reverse=True)
    
    schedule = []    
    total_work = 0
    for course in thecourses:
        if total_work + 1.0/getWork(course) > maxWork:
            continue
        schedule.append(course)
        total_work += 1.0/getWork(course)
        if total_work == maxWork:
            break
    if sort_method == getVal:
        print 'BY VALUE'
    if sort_method == getWork:
        print 'BY WORK'
    if sort_method == getRatio:
        print 'BY VALUE TO WORK RATIO'
    assert total_work <= maxWork
    printCourses(schedule)

#==============================================================================
# small_catalog = [Course('6.00',16,8),Course('1.00',7,7),Course('6.01',5,3),Course('15.01',9,6)]
# chooseGreedy(small_catalog,15,getVal)
# chooseGreedy(small_catalog,15,getWork)
# chooseGreedy(small_catalog,15,getRatio)
#==============================================================================

def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n)==int and type(numDigits)==int and n >= 0 and n < 2**numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n//2
    while numDigits - len(bStr) > 0:
        bStr = '0' + bStr
    return bStr

def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items)
    templates = []
    for i in range(numSubsets):
        templates.append(dToB(i, len(Items)))
    pset = []
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    return pset

def chooseOptimal(course_list,maxWork):
    """Returns the globally optimal schedule
    course_list: list of Course instances
    maxWork: int, constraint
    """
    pset = genPset(course_list)
    
    best_schedule = None
    best_value = 0
    
    for schedule in pset:
        total_work = 0
        total_value = 0
        for course in schedule:
            total_work += (1.0/getWork(course))
            if total_work > maxWork:
                break
            total_value += getVal(course)
        if total_value > best_value:
            best_value = total_value
            best_schedule = schedule
    printCourses(best_schedule)

#==============================================================================
# lotsa_courses = loadCourses("shortened_subjects.txt")
# 
# chooseOptimal(lotsa_courses,3)
# chooseOptimal(lotsa_courses,4)
# chooseOptimal(lotsa_courses,5)
# chooseOptimal(lotsa_courses,6)
# chooseOptimal(lotsa_courses,7)    
#==============================================================================
