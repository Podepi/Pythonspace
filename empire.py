import random as rm
import math
from rmword import *
empires = []

class Empire(object):
    def __init__(self):
		self.name = makeword(rm.randint(2,3)) + " Empire"
		self.war = ""
		self.planets = []
		self.techs = []

class Planet(object):
	def __init__(self):
		self.name = makeword(rm.randint(2,3))
		self.pop = rm.randint(1000, 1000000)
		self.prodfocus = [0, 0, 0, 0] # Farmers, workers, miners, scientists
		self.stock = [9999, 9999, 9999] # food, goods, minerals
		self.prodinput = [0.74, 0, 0.9] # -Food/pop/yr, -goods/pop/yr, -minerals/worker/yr
		self.prodoutput= [0.75, 0.1, 0.91] # +Food/farmer/yr, +goods/worker/yr, +minerals/miner/yr
		self.wealth = rm.randint(100000, 100000000)
		self.tax = 1 # Wealth/person/year
		
	def redistProd(self):
		self.prodfocus = [0, 0, 0, 0]
		free_workers = self.pop
		while self.calculateGrowth(1, True) - self.stock[0] < 10 and free_workers < 0:
			self.prodfocus[0] += 100
			free_workers -= 100
		if self.stock[0] <= self.pop:
			self.prodfocus[0] += int(self.pop/10)
			free_workers -= int(self.pop/10)
		self.prodfocus[1] += int(free_workers/2)
		self.prodfocus[2] += int(free_workers/2)
		free_workers = 0
		print self.prodfocus
		print self.stock
		print self.prodoutput
		
	def calcProd(self, t, retmode=False):
		demand = [0,0,0]
		supply = [0,0,0]
		surplus = [0,0,0]
		for i in xrange(len(self.prodinput)):
			demand[i] = int(self.pop * self.prodinput[i] * t)
			supply[i] = int(self.pop * self.prodoutput[i] * t)
			surplus[i] = supply[i] - demand[i]
			self.stock[i] += surplus[i]
		self.wealth += self.tax * self.pop
		#print self.wealth
		
	def calculateGrowth(self, t, retmode=False): # t in years
		startpop = self.pop
		demand = self.pop * self.prodinput[0] * t
		supply = self.stock[0] + self.pop * self.prodoutput[0] * t
		surplus = supply - demand
		if retmode == True:
			return int(surplus)
		else:
			if supply > demand:
				self.pop = int(self.pop * math.exp(0.015 * t))
			else:
				self.pop -= surplus * self.prodinput[0] * t
			#self.stock[0] = surplus
			print "growth: " + str(self.pop - startpop), "pop: " + str(self.pop)
			if self.pop <= 0:
				self.pop = 0
				print "Population destroyed"
				
	def simulate(self):
		redistProd()
		calcProd(1)
		calculateGrowth(1)
		if rm.random() < 0.1:
			randEvent()
	
	def randEvent(self):
		event = rm.randint(0,3)
		if event == 0:
			self.prodoutput[0] -= 0.01
			print "Widespread drought reduces total food production by " + str(0.01 * self.pop)
		elif event == 1:
			self.prodoutput[0] += 0.01
			print "Fertile rains fall, increasing total food production by " + str(0.01 * self.pop)
		elif event == 2:
			self.prodoutput[1] += 0.01
			print "New technologies improve total industry by " + str(0.01 * self.pop)
		elif event == 3:
			self.prodoutput[1] -= 0.01
			print "Catastrophic industrial accident reduces total industry by  " + str(0.01 * self.pop)

			
def createEmpire():
	new_emp = Empire()
	new_emp.planets.append(Planet())
	empires.append(new_emp)

def simulate(empire):
    for p in empire.planets:
		p.simulate()
createEmpire()	
step = 0
while True:
	simulate(empires[0])
	raw_input(step)
	step += 1