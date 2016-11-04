# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#
import itertools

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.

    courses = {}

    inputFile = open(filename)
    for line in inputFile:
        name,value,work = line.split(",")
        value = int(value)
        work = int(work)
        courses[name] = (value,work)

    return courses

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    if subInfo1[0] > subInfo2[0]:
        return True
    else:
        return False

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    if subInfo1[1] < subInfo2[1]:
        return True
    else:
        return False

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    if subInfo1[0] / float(subInfo1[1]) > subInfo2[0] / float(subInfo2[1]):
        return True
    else:
        return False

def greedyAdvisor(subjects, maxWork, comparator):
	"""
	Returns a dictionary mapping subject name to (value, work) which includes
	subjects selected by the algorithm, such that the total work of subjects in
	the dictionary is not greater than maxWork.  The subjects are chosen using
	a greedy algorithm.  The subjects dictionary should not be mutated.

	subjects: dictionary mapping subject name to (value, work)
	maxWork: int >= 0
	comparator: function taking two tuples and returning a bool
	returns: dictionary mapping subject name to (value, work)
	"""

	def merge_sort(my_array):
		'''
		sort array in decreasing order of goodness
		'''
		if len(my_array) == 1:
			return my_array
		else:
			mid = len(my_array) / 2
			left = merge_sort(my_array[:mid])
			right = merge_sort(my_array[mid:])
			together = []
			left_ind = 0
			right_ind = 0
			while True:
				first_class = left[left_ind]
				second_class = right[right_ind]
				if comparator(subjects[first_class], subjects[second_class]):
					together.append(first_class)
					left_ind += 1
					if left_ind == len(left):
						together.extend(right[right_ind:])
						break
				else:
					together.append(second_class)
					right_ind += 1
					if right_ind == len(right):
						together.extend(left[left_ind:])
						break
			return together

	courses = subjects.keys()
	sorted_courses = merge_sort(courses)
	willpower = maxWork
	selected_courses = {}
	for course in sorted_courses:
		work_required = subjects[course][1]
		if willpower - work_required >= 0:
			selected_courses[course] = subjects[course]
			willpower -= work_required
	return selected_courses

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceAdvisor(subjects, maxWork):
	"""
	Returns a dictionary mapping subject name to (value, work), which
	represents the globally optimal selection of subjects using a brute force
	algorithm.

	subjects: dictionary mapping subject name to (value, work)
	maxWork: int >= 0
	returns: dictionary mapping subject name to (value, work)
	"""

	def eval_combo(combo,subjects=subjects):
		"""
		return the total work required and value gained from the "combo" of courses

		combo : tuple of int
		courses : list of string
		subject_to_val_work : dict

		return : (int, int)
		"""

		tot_work = 0
		tot_val = 0
		for course in combo:
			tot_work += subjects[course][1]
			tot_val += subjects[course][0]

		return (tot_val,tot_work)

	courses = subjects.keys()
	best_combo = None
	best_combo_value = 0
	best_combo_work = float('inf')
	for combo_size in range(1,len(courses)+1):
		combos = itertools.combinations(courses,combo_size)
		for combo in combos:
			tot_val, tot_work = eval_combo(combo)
			if tot_work <= maxWork and tot_val > best_combo_value:
				best_combo, best_combo_value, best_combo_work = combo, tot_val, tot_work
	selected_courses = {}

	for course in best_combo:
		selected_courses[course] = subjects[course]
	return selected_courses