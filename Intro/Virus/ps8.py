# 6.00 Problem Set 8
#
# Name:
# Collaborators:
# Time:



import numpy
import random
import pylab
from ps7 import *

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """      

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb


    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances[drug]
        
    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        for drug in activeDrugs:
            if self.resistances[drug] == False:
                raise NoChildException
        fate = random.random()
        if fate <= self.maxBirthProb * (1 - popDensity):
            baby_resistances = {}
            for drug in self.resistances:
                if random.random() <= self.mutProb:
                    baby_resistances[drug] = not self.resistances[drug]
                else:
                    baby_resistances[drug] = self.resistances[drug]
            return ResistantVirus(self.maxBirthProb,self.clearProb,baby_resistances,self.mutProb)
        else:
            raise NoChildException
            

class Patient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []
    
    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug in self.drugs:
            pass
        else: 
            self.drugs.append(newDrug)

    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.drugs
        

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        
        resistantPop = 0
        
        for virus in self.viruses:
            for drug in drugResist:
                if not virus.isResistantTo(drug):
                    break
            else:
                resistantPop += 1
        
        return resistantPop    
    
    def getPopDensity(self):
        """Returns the Population Density"""
        return len(self.viruses)/float(self.maxPop)                   
    
    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        survivors = []
        for virus in self.viruses:
            fate = random.random()
            if fate >= virus.clearProb:
                survivors.append(virus)
        self.viruses = survivors
        
        popDensity = self.getPopDensity()
        
        babies = []
        for virus in self.viruses:
            try:
                baby_virus = virus.reproduce(popDensity,self.getPrescriptions())
                assert baby_virus.__class__ == ResistantVirus
                babies.append(baby_virus)
            except:
                next
        self.viruses = self.viruses + babies
        return self.getTotalPop()                
                


#
# PROBLEM 2
#

def simulationWithDrug():

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    T: int, time at which drug is administered
    """
    list_total_pops = []
    list_res_pops = []
    for trial in range(500):
    
        viruses = []
        for x in range(100):
            viruses.append(ResistantVirus(.1,.05,{'guttagonal':False},.005))
        
        person = Patient(viruses,1000)
        
        total_pops = []
        resistant_pops = []
        total_pops.append(100)
        resistant_pops.append(0)
        for time in range(1,226):
            if time == 76:
                person.addPrescription('guttagonal')
            total_pop = person.update()
            print person.getPrescriptions()
            print 'total pop', total_pop
            print 'resistant pop', person.getResistPop(['guttagonal'])
            total_pops.append(total_pop)
            resistant_pops.append(person.getResistPop(['guttagonal']))
        list_total_pops.append(total_pops)
        list_res_pops.append(resistant_pops)
    list_total_pops = pylab.array(list_total_pops)
    list_total_pops = list_total_pops.mean(0)    
    list_res_pops = pylab.array(list_res_pops)
    list_res_pops = list_res_pops.mean(0)
    pylab.figure()
    pylab.plot(list_total_pops,'ro')
    pylab.xlabel('time')
    pylab.ylabel('total number of viruses')
    pylab.title('virus population over time')
    pylab.ylim(0,600)    
    pylab.figure()    
    pylab.plot(list_res_pops,'go')
    pylab.ylim(0,600)
    pylab.xlabel('time')
    pylab.ylabel('number of resistant viruses')
    pylab.title('resistant virus population over time')
    pylab.show()
    
#simulationWithDrug()    
#
# PROBLEM 3
#        

def simulationDelayedTreatment():

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    final_vir_pops = []
    treatment_start_times = [300,150,75,0]
    for treatment_start_time in treatment_start_times:
        final_vir_pop = []        
        for trial in range(500):
            viruses = []
            for x in range(100):
                viruses.append(ResistantVirus(.1,.05,{'guttagonal':False},.005))
            person = Patient(viruses,1000)    
            for time in range(1,treatment_start_time+151):
                if time == treatment_start_time:
                    person.addPrescription('guttagonal')
                if treatment_start_time == 0 and time == 1:
                    person.addPrescription('guttagonal')
                person.update()
            final_vir_pop.append(person.getTotalPop())
        final_vir_pops.append(final_vir_pop)
    print final_vir_pops

    pylab.figure()
    pylab.subplot(221)
    pylab.hist(final_vir_pops[0])
    pylab.title('final virus pops, treatment started at t = 300')
    pylab.xlabel('number of viruses')
    pylab.ylabel('frequency')
    pylab.subplot(222)
    pylab.hist(final_vir_pops[1])
    pylab.title('final virus pops, treatment started at t = 150')
    pylab.xlabel('number of viruses')
    pylab.ylabel('frequency')
    pylab.subplot(223)
    pylab.hist(final_vir_pops[2])
    pylab.title('final virus pops, treatment started at t = 75')
    pylab.xlabel('number of viruses')
    pylab.ylabel('frequency')
    pylab.subplot(224)
    pylab.hist(final_vir_pops[3])
    pylab.title('final virus pops, treatment started at t = 0')
    pylab.xlabel('number of viruses')
    pylab.ylabel('frequency')
    pylab.show()

#simulationDelayedTreatment()
#   
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment():

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    lag_times = [300,150,75,0]
    final_pops_list = []
    
    for lag_time in lag_times:
        final_pops = []
        for trial in range(500):
            viruses = []
            for x in range(100):
                viruses.append(ResistantVirus(.1,.05,{'guttagonal':False,'grimpex':False},.005))
            person = Patient(viruses,1000)
            for time in range(300 + lag_time):
                if time == 150:
                    person.addPrescription('guttagonal')
                if time == 150 + lag_time:
                    person.addPrescription('grimpex')
                person.update()
            final_pops.append(person.getTotalPop())
        final_pops_list.append(final_pops)
    
    pylab.figure()
    pylab.subplot(221)
    pylab.hist(final_pops_list[0])
    pylab.title('final virus pops, lag = 300')
    pylab.xlabel('number of viruses')
    pylab.ylabel('frequency')
    pylab.subplot(222)
    pylab.hist(final_pops_list[1])
    pylab.title('final virus pops, lag = 150')
    pylab.xlabel('number of viruses')
    pylab.ylabel('frequency')
    pylab.subplot(223)
    pylab.hist(final_pops_list[2])
    pylab.title('final virus pops, lag = 75')
    pylab.xlabel('number of viruses')
    pylab.ylabel('frequency')
    pylab.subplot(224)
    pylab.hist(final_pops_list[3])
    pylab.title('final virus pops, lag = 0')
    pylab.xlabel('number of viruses')
    pylab.ylabel('frequency')
    pylab.show()
  
#simulationTwoDrugsDelayedTreatment()  
#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations():

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    total_pops_300 = []    
    res_pops_300 = []
    gutt_pops_300 = []
    grim_pops_300 = []    
    for trial in range(100):
        total_pop = []
        res_pop = []
        gutt_pop = []
        grim_pop = []        
        viruses = []
        for x in range(100):
            viruses.append(ResistantVirus(.1,.05,{'guttagonal':False,'grimpex':False},.005))
        person = Patient(viruses,1000)
        for time in range(600):
            if time == 150:
                person.addPrescription('guttagonal')
            if time == 450:
                person.addPrescription('grimpex')            
            total_pop.append(person.getTotalPop())
            res_pop.append(person.getResistPop(['guttagonal','grimpex']))
            gutt_pop.append(person.getResistPop(['guttagonal']))
            grim_pop.append(person.getResistPop(['grimpex']))
            person.update()
        total_pops_300.append(total_pop)
        res_pops_300.append(res_pop)
        gutt_pops_300.append(gutt_pop)
        grim_pops_300.append(grim_pop)
    total_pops_300 = pylab.array(total_pops_300)
    total_pops_300 = total_pops_300.mean(0)
    res_pops_300 = pylab.array(res_pops_300)
    res_pops_300 = res_pops_300.mean(0)
    gutt_pops_300 = pylab.array(gutt_pops_300)
    gutt_pops_300 = gutt_pops_300.mean(0)
    grim_pops_300 = pylab.array(grim_pops_300)
    grim_pops_300 = grim_pops_300.mean(0)        
        
    total_pops_0 = []    
    res_pops_0 = []
    gutt_pops_0 = []
    grim_pops_0 = []    
    for trial in range(100):
        total_pop = []
        res_pop = []
        gutt_pop = []
        grim_pop = []        
        viruses = []
        for x in range(100):
            viruses.append(ResistantVirus(.1,.05,{'guttagonal':False,'grimpex':False},.005))
        person = Patient(viruses,1000)
        for time in range(300):
            if time == 150:
                person.addPrescription('guttagonal')
                person.addPrescription('grimpex')
            total_pop.append(person.getTotalPop())
            res_pop.append(person.getResistPop(['guttagonal','grimpex']))
            gutt_pop.append(person.getResistPop(['guttagonal']))
            grim_pop.append(person.getResistPop(['grimpex']))
            person.update()
        total_pops_0.append(total_pop)
        res_pops_0.append(res_pop)
        gutt_pops_0.append(gutt_pop)
        grim_pops_0.append(grim_pop)
    total_pops_0 = pylab.array(total_pops_0)
    total_pops_0 = total_pops_0.mean(0)
    res_pops_0 = pylab.array(res_pops_0)
    res_pops_0 = res_pops_0.mean(0)
    gutt_pops_0 = pylab.array(gutt_pops_0)
    gutt_pops_0 = gutt_pops_0.mean(0)
    grim_pops_0 = pylab.array(grim_pops_0)
    grim_pops_0 = grim_pops_0.mean(0)
        
    pylab.figure()
    pylab.plot(total_pops_300, 'r-', label = 'total')
    pylab.plot(res_pops_300,'c-',label=' both res')
    pylab.plot(gutt_pops_300,'y-',label='gutt res')
    pylab.plot(grim_pops_300,'g-',label='grim res')
    pylab.title('pop over time, lag = 300')    
    pylab.legend()    
    pylab.figure()
    pylab.plot(total_pops_0,'r-',label='total')
    pylab.plot(res_pops_0,'c-',label='both res')
    pylab.plot(gutt_pops_0,'y-',label='gutt resis')
    pylab.plot(grim_pops_0,'g-',label='grim resis')
    pylab.title('pop over time, lag = 0')    
    pylab.legend()    
    pylab.show()

simulationTwoDrugsVirusPopulations()

