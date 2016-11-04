# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
	"""
	A Position represents a location in a two-dimensional room.
	"""
	def __init__(self, x, y):
		"""
		Initializes a position with coordinates (x, y).
		"""
		self.x = x
		self.y = y
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getNewPosition(self, angle, speed):
		"""
		Computes and returns the new Position after a single clock-tick has
		passed, with this object as the current position, and with the
		specified angle and speed.

		Does NOT test whether the returned position fits inside the room.

		angle: float representing angle in degrees, 0 <= angle < 360
		speed: positive float representing speed

		Returns: a Position object representing the new position.
		"""
		old_x, old_y = self.getX(), self.getY()
		# Compute the change in position
		delta_y = speed * math.cos(math.radians(angle))
		delta_x = speed * math.sin(math.radians(angle))
		# Add that to the existing position
		new_x = old_x + delta_x
		new_y = old_y + delta_y
		return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
	"""
	A RectangularRoom represents a rectangular region containing clean or dirty
	tiles.

	A room has a width and a height and contains (width * height) tiles. At any
	particular time, each of these tiles is either clean or dirty.
	"""
	def __init__(self, width, height):
		"""
		Initializes a rectangular room with the specified width and height.

		Initially, no tiles in the room have been cleaned.

		width: an integer > 0
		height: an integer > 0
		"""
		self.height = height
		self.width = width 
		tiles = {}
		for x in range(width):
			for y in range(height):
				tiles[(x,y)] = "dirty"
		self.tiles = tiles

	def cleanTileAtPosition(self, pos):
		"""
		Mark the tile under the position POS as cleaned.

		Assumes that POS represents a valid position inside this room.

		pos: a Position
		"""
		x = int(math.floor(pos.getX()))
		y = int(math.floor(pos.getY()))
		self.tiles[(x,y)] = "clean"        

	def isTileCleaned(self, m, n):
		"""
		Return True if the tile (m, n) has been cleaned.

		Assumes that (m, n) represents a valid tile inside the room.

		m: an integer
		n: an integer
		returns: True if (m, n) is cleaned, False otherwise
		"""
		if self.tiles[(m,n)] == "clean":
			return True
		else:
			return False

	def getNumTiles(self):
		"""
		Return the total number of tiles in the room.

		returns: an integer
		"""
		return self.width * self.height

	def getNumCleanedTiles(self):
		"""
		Return the total number of clean tiles in the room.

		returns: an integer
		"""
		cleaned = 0
		for tile in self.tiles:
			if self.tiles[tile] == "clean":
				cleaned += 1
		return cleaned

	def getRandomPosition(self):
		"""
		Return a random position inside the room.

		returns: a Position object.
		"""
		return Position(random.random()*self.width, random.random()*self.height)

	def isPositionInRoom(self, pos):
		"""
		Return True if pos is inside the room.

		pos: a Position object.
		returns: True if pos is in the room, False otherwise.
		"""
		if self.width >= pos.getX() and pos.getX() >= 0 and self.height >= pos.getY() and pos.getY() >= 0:
			return True
		else:
			return False 


class Robot(object):
	"""
	Represents a robot cleaning a particular room.

	At all times the robot has a particular position and direction in the room.
	The robot also has a fixed speed.

	Subclasses of Robot should provide movement strategies by implementing
	updatePositionAndClean(), which simulates a single time-step.
	"""
	def __init__(self, room, speed):
		"""
		Initializes a Robot with the given speed in the specified room. The
		robot initially has a random direction and a random position in the
		room. The robot cleans the tile it is on.

		room:  a RectangularRoom object.
		speed: a float (speed > 0)
		"""
		self.room = room
		self.position = room.getRandomPosition()
		self.direction = random.random() * 360
		self.speed = speed

	def getRobotPosition(self):
		"""
		Return the position of the robot.

		returns: a Position object giving the robot's position.
		"""
		return self.position

	def getRobotDirection(self):
		"""
		Return the direction of the robot.

		returns: an integer d giving the direction of the robot as an angle in
		degrees, 0 <= d < 360.
		"""
		return self.direction

	def setRobotPosition(self, position):
		"""
		Set the position of the robot to POSITION.

		position: a Position object.
		"""
		self.position = position

	def setRobotDirection(self, direction):
		"""
		Set the direction of the robot to DIRECTION.

		direction: integer representing an angle in degrees
		"""
		self.direction = direction

	def updatePositionAndClean(self):
		"""
		Simulate the raise passage of a single time-step.

		Move the robot to a new position in the room, and mark the tile it is on as having
		been cleaned.
		"""
		raise NotImplementedError

# === Problem 2
class StandardRobot(Robot):
	"""
	A StandardRobot is a Robot with the standard movement strategy.

	At each time-step, a StandardRobot attempts to move in its current direction; when
	it hits a wall, it chooses a new direction randomly.
	"""
	def updatePositionAndClean(self):
		"""
		Simulate the passage of a single time-step.

		Move the robot to a new position and mark the tile it is on as having
		been cleaned.
		"""
		old_position = self.getRobotPosition()
		new_position = old_position.getNewPosition(self.getRobotDirection(), self.speed)
		while not self.room.isPositionInRoom(new_position):
			new_angle = random.random() * 360
			self.setRobotDirection(new_angle)
			new_position = old_position.getNewPosition(self.getRobotDirection(), self.speed)

		self.setRobotPosition(new_position)
		x,y = math.floor(new_position.getX()), math.floor(new_position.getY())
		if not self.room.isTileCleaned(x,y):
			self.room.cleanTileAtPosition(new_position)  


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type):
	"""
	Runs NUM_TRIALS trials of the simulation and returns the mean number of
	time-steps needed to clean the fraction MIN_COVERAGE of the room.

	The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
	speed SPEED, in a room of dimensions WIDTH x HEIGHT.

	num_robots: an int (num_robots > 0)
	speed: a float (speed > 0)
	width: an int (width > 0)
	height: an int (height > 0)
	min_coverage: a float (0 <= min_coverage <= 1.0)
	num_trials: an int (num_trials > 0)
	robot_type: class of robot to be instantiated (e.g. Robot or
	            RandomWalkRobot)
	""" # hypo : robots are not moving.
	total_time = 0.0
	for trial in range(num_trials):
		room = RectangularRoom(width,height)
		robots = []
		for robot_id in range(num_robots):
			robot = robot_type(room,speed)
			robots.append(robot)
		time_taken = 0
		while room.getNumCleanedTiles() / float(room.getNumTiles()) < min_coverage:
			for robot in robots:
				robot.updatePositionAndClean()
			time_taken += 1
		total_time += time_taken
	return total_time / num_trials

# === Problem 4
#
# 1) How long does it take to clean 80% of a 20by20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20by20, 25by16, 40by10, 50by8, 80by5, and 100by4?

def showPlot1():
	"""
	Produces a plot showing dependence of cleaning time on number of robots.
	80% of a 20 by 20 with 1 through 10 robots, mean time over 15 trials
	""" 
	mean_time = [runSimulation(num_robots,1.0,20,20,.8,100,StandardRobot) for num_robots in range(1,11)]
	num_robots = range(1,11)
	pylab.clf()
	pylab.plot(num_robots,mean_time)
	pylab.ylim(max(min(mean_time)-10,0),max(mean_time)+10)
	pylab.title("Time taken to clean 80 percent of a 20 by 20 room")
	pylab.xlabel("number of robots")
	pylab.ylabel("time averaged over 100 trials")
	pylab.savefig('time_versus_number_robots.png', bbox_inches='tight')

def showPlot2():
	"""
	Produces a plot showing dependence of cleaning time on room shape.
	2 robots clean 80% of rooms with equal area but different shapes 
	"""
	shapes = ((20,20),(25,16),(40,10),(50,8),(80,5),(100,4))
	mean_time = [runSimulation(2,1.0,w,h,.8,1000,StandardRobot) for w,h in shapes]
	shape_ratios = [float(w)/h for w,h in shapes]
	pylab.clf()
	pylab.plot(shape_ratios,mean_time)
	pylab.ylim(max(min(mean_time)-10,0),max(mean_time)+10)
	pylab.title("Time taken by 2 robots to clean differently shaped rooms of area 400 sqft")
	pylab.xlabel("ratio of room width to height")
	pylab.ylabel("time averaged over 1000 trials")
	pylab.savefig('time_vs_room_shape.png', bbox_inches='tight')

# === Problem 5

class RandomWalkRobot(Robot):
	"""
	A RandomWalkRobot is a robot with the "random walk" movement strategy: it
	chooses a new direction at random after each time-step.
	"""
	def updatePositionAndClean(self):
		"""
		Simulate the passage of a single time-step.

		Move the robot to a new position and mark the tile it is on as having
		been cleaned.
		"""
		old_position = self.getRobotPosition()
		new_angle = random.random() * 360
		self.setRobotDirection(new_angle)
		new_position = old_position.getNewPosition(self.getRobotDirection(), self.speed)
		while not self.room.isPositionInRoom(new_position):
			new_angle = random.random() * 360
			self.setRobotDirection(new_angle)
			new_position = old_position.getNewPosition(self.getRobotDirection(), self.speed)

		self.setRobotPosition(new_position)
		x,y = math.floor(new_position.getX()), math.floor(new_position.getY())
		if not self.room.isTileCleaned(x,y):
			self.room.cleanTileAtPosition(new_position)    


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
	"""
	Produces a plot comparing the two robot strategies.
	"""
	mean_time_standard = [runSimulation(num_robots,1.0,20,20,.8,100,StandardRobot) for num_robots in range(1,11)]
	mean_time_random = [runSimulation(num_robots,1.0,20,20,.8,100,RandomWalkRobot) for num_robots in range(1,11)]
	num_robots = range(1,11)
	pylab.clf()
	pylab.plot(num_robots,mean_time_standard,'-b',label="standard")
	pylab.plot(num_robots,mean_time_random,'-r',label="random walk")
	y_max = max(max(mean_time_standard),max(mean_time_random))+100
	pylab.ylim(0,y_max)
	pylab.yticks(range(0,int(y_max)+99,100))
	pylab.title("Time taken to clean 80 percent of a 20 by 20 room")
	pylab.xlabel("number of robots")
	pylab.ylabel("time averaged over 100 trials")
	pylab.grid(b=True, which='m',linestyle='--')
	pylab.legend(loc=1)
	pylab.savefig('two_strategies_compared.png', bbox_inches='tight')



if __name__ == "__main__":
	showPlot3()