# 6.00 Problem Set 8
#
# Name:
# Collaborators:
# Time:


import copy
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
        self.mutProb = mutProb
        self.resistances = resistances

    def survives(self):
        """
        determines if virus is killed or not

        return : boolean
        """

        if self.clearProb < random.random():
            return True
        else:
            return False

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


    def update_resistance(self):
        """
        mutates a virus' drug resistances

        return : dictionary (string -> boolean) 
        """
        resistances = copy.copy(self.resistances)
        for drug in resistances:
            if random.random() < self.mutProb:
                resistances[drug] = not resistances[drug]
        return resistances


    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If there is a drug in activeDrugs, which the virus particle is not resistant to,
        then the virus particle does not reproduce. Otherwise, the virus particle reproduces
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
        # check if resistant to at least 1 drug, or there are no drugs, else raise NoChildException
        
        # no medicine
        if activeDrugs == []:
            if random.random() < self.maxBirthProb * (1 - popDensity):
                return ResistantVirus(self.maxBirthProb, self.clearProb, self.update_resistance(), self.mutProb)
            else:
            	raise NoChildException
        
        # medicine
        for drug in activeDrugs:
            if not self.resistances[drug]: 
            	raise NoChildException
        else:
			if random.random() < self.maxBirthProb * (1 - popDensity):
				return ResistantVirus(self.maxBirthProb, self.clearProb, self.update_resistance(), self.mutProb)
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
        self.medicine = []
    

    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        
        if newDrug not in self.medicine:
            self.medicine.append(newDrug)


    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.medicine
        

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        super_bugs = 0
        for virus in self.viruses:
            for drug in drugResist:
                if not virus.resistances[drug]:
                    break
            else:
                super_bugs += 1

        return super_bugs                       


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
            if virus.survives():
                survivors.append(virus)

        new_viruses = []
        pop_density = len(survivors) / float(self.maxPop)
        for virus in survivors:
            try:
                new_virus = virus.reproduce(pop_density, self.medicine)
                new_viruses.append(new_virus) 
            except NoChildException:
                pass
        survivors.extend(new_viruses)

        self.viruses = survivors
        return len(survivors)



#
# PROBLEM 2
#

def simulationWithDrug(administration_time=150):

    """
    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    tot_pop = [0 for time_step in range(administration_time+150)]
    guttag_resist_pop = [0 for time_step in range(administration_time+150)]
    for trial in range(1000):
        viruses = []
        for v_id in range(100):
            viruses.append(ResistantVirus(.1, .05, {'guttagonol': False}, .005))

        patient = Patient(viruses,1000)

        for time_step in range(administration_time):
            tot_pop[time_step] += patient.update()
            guttag_resist_pop[time_step] += patient.getResistPop(['guttagonol']) 

        patient.addPrescription('guttagonol')
        for time_step in range(150):
            tot_pop[time_step+administration_time] += patient.update()
            guttag_resist_pop[time_step+administration_time] += patient.getResistPop(['guttagonol'])     

    mean_pop = [pop / 1000.0 for pop in tot_pop]
    mean_resist_pop = [pop / 1000.0 for pop in guttag_resist_pop]

    pylab.plot(range(administration_time+150),mean_pop,'-b',label='num viruses')
    pylab.plot(range(administration_time+150),mean_resist_pop,'-r',label='resistant viruses')
    pylab.ylim(0,1005)
    pylab.xlabel('time')
    pylab.ylabel('number of viruses (averaged over 1000 trials)')
    pylab.title('number of viruses and resistant viruses over time. guttagonol administered at time 150')
    pylab.legend(loc=2)
    pylab.savefig("virus_plot_1.png", bbox_inches = "tight")
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
    for delay in [0,75,150,300]:    
        final_pop = []
        for trial in range(1000):
            viruses = []
            for v_id in range(100):
                viruses.append(ResistantVirus(.1, .05, {'guttagonol': False}, .005))

            patient = Patient(viruses,1000)

            for time_step in range(delay):
                patient.update() 

            patient.addPrescription('guttagonol')
            for time_step in range(150):
                patient.update()     

            final_pop.append(len(patient.viruses))

        pylab.clf()
        pylab.ylim(0,1000)
        pylab.hist(final_pop)
        pylab.xlabel('number of viruses')
        pylab.ylabel('frequency')
        pylab.title('distribution of final virus population size. treatment delay: ' + str(delay))
        pylab.legend(loc=2)
        pylab.savefig("one_drug_fin_pop_delay"+str(delay)+".png", bbox_inches = "tight")
    

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
    for delay in [0,75,150,300]:    
        final_pop = []

        for trial in range(1000):
            viruses = []
            for v_id in range(100):
                viruses.append(ResistantVirus(.1, .05, {'guttagonol': False, 'grimpex': False}, .005))
            patient = Patient(viruses,1000)

            for time_step in range(150):
                patient.update() 
            patient.addPrescription('guttagonol')
            for time_step in range(delay):
                patient.update()     
            patient.addPrescription('grimpex')
            for time_step in range(150):
                patient.update()

            final_pop.append(len(patient.viruses))

        pylab.clf()
        pylab.hist(final_pop)
        pylab.ylim(0,1000)
        pylab.xlim(-0.5,1000)
        pylab.xlabel('number of viruses')
        pylab.ylabel('frequency')
        pylab.title('distribution of final virus population size. treatment delay: ' + str(delay))
        pylab.legend(loc=2)
        pylab.savefig("two_drug_fin_pop_delay_"+str(delay)+".png", bbox_inches = "tight")

    



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
	# for delay in [0,300]:
	for delay in [300]:
		total_pop = [0 for time_step in range(delay + 300)]
		guttag_pop = [0 for time_step in range(delay + 300)]
		grimp_pop = [0 for time_step in range(delay + 300)]
		both_pop = [0 for time_step in range(delay + 300)]

		for trial in range(1000):
			print "trial",trial+1

			viruses = []
			for v_id in range(100):
				viruses.append(ResistantVirus(.1, .05, {'guttagonol': False, 'grimpex': False}, .005))
			patient = Patient(viruses,1000)

			for time_step in range(150):
				total_pop[time_step] += patient.update()
				both_pop[time_step] += patient.getResistPop(['guttagonol','grimpex'])
				guttag_pop[time_step] += patient.getResistPop(['guttagonol'])
				grimp_pop[time_step] += patient.getResistPop(['grimpex']) 
			patient.addPrescription('guttagonol')
			for time_step in range(delay):
				total_pop[time_step+150] += patient.update()
				both_pop[time_step+150] += patient.getResistPop(['guttagonol','grimpex'])
				guttag_pop[time_step+150] += patient.getResistPop(['guttagonol'])
				grimp_pop[time_step+150] += patient.getResistPop(['grimpex'])     
			patient.addPrescription('grimpex')
			for time_step in range(150):
				total_pop[time_step+150+delay] += patient.update()
				both_pop[time_step+150+delay] += patient.getResistPop(['guttagonol','grimpex'])
				guttag_pop[time_step+150+delay] += patient.getResistPop(['guttagonol'])
				grimp_pop[time_step+150+delay] += patient.getResistPop(['grimpex'])

		t_pop = [pop / 1000.0 for pop in total_pop]
		b_pop = [pop / 1000.0 for pop in both_pop]
		gt_pop = [pop / 1000.0 for pop in guttag_pop]
		gr_pop = [pop / 1000.0 for pop in grimp_pop]

		pylab.clf()
		pylab.plot(range(300 + delay),t_pop,label="total")
		pylab.plot(range(300 + delay),b_pop,label="resists both")
		pylab.plot(range(300 + delay),gt_pop,label="resists gutag")
		pylab.plot(range(300 + delay),gr_pop,label="resists grimp")
		pylab.legend(loc=2)
		pylab.xlabel("time")
		pylab.ylabel("number of viruses (averaged over 1000 trials")
		pylab.title("admin time ... guttagonol: 150, grimpex: " + str(150+delay))
		pylab.ylim(0,600)
		pylab.savefig("two_drug_pop_over_time_delay"+str(delay)+".png", bbox_inches="tight")


if __name__ == "__main__":
	simulationTwoDrugsVirusPopulations() # after first, resistant to guttag goes up, after second drug, resistant to both goes up,