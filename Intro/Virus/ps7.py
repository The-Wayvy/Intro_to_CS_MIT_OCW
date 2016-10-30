# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """
        fate = random.random()
        if fate <= self.clearProb:
            return True
        else:
            return False

    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        fate = random.random()
        if fate <= self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb,self.clearProb)
        else: 
            raise NoChildException
        

class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop


    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)        


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        
        number_cleared = 0
        for virus in self.viruses:
            if virus.doesClear():
                number_cleared += 1
        self.viruses = self.viruses[number_cleared:]
        
        popDensity = self.getTotalPop() / float(self.maxPop)
        assert popDensity >= 0.0 and popDensity <= 1.0
        
        baby_viruses = []
        for virus in self.viruses:
            try:
                new_virus = virus.reproduce(popDensity)
                assert new_virus.__class__ == SimpleVirus 
                baby_viruses.append(new_virus)
            except:
                next 
        self.viruses = self.viruses + baby_viruses
        return self.getTotalPop()


#
# PROBLEM 2
#
def simulationWithoutDrug(time_steps,repro,clear,initPop,maxPop):

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.  
    time_steps: int
    repro: float
    clear: float
    initPop = int
    maxPop = int
    """
    #intialize a person with 100 viruses
    viruses = []    
    for x in range(initPop):
        virus = SimpleVirus(repro,clear)
        viruses.append(virus)
    
    person = SimplePatient(viruses,maxPop)
    
    virus_pop = []
    times = range(time_steps)
    for t in times:
        person.update()
        virus_pop.append(person.getTotalPop())
        
    return virus_pop
    
def typical_case(time_steps,repro,clear,initPop,maxPop,numPatients):
    time = range(time_steps)
    virus_pops = []
    for patient in range(numPatients):
        viruses = simulationWithoutDrug(time_steps,repro,clear,initPop,maxPop)
        virus_pops.append(viruses)
    virus_pops = numpy.array(virus_pops)
    averages = virus_pops.mean(0)
    print averages.shape
    print averages
    pylab.plot(time,averages)
    pylab.xlabel('time')
    pylab.ylabel('expected # of viruses')
    pylab.title('average virus population over time in %s patients'%(numPatients))
    pylab.ylim(0,600)
    pylab.xticks(range(0,301,30))
    pylab.yticks(range(0,601,30))    
    pylab.grid(True)
    pylab.show()     
    
#==============================================================================
# typical_case(300,.1,.05,100,1000,100)
#==============================================================================
        
