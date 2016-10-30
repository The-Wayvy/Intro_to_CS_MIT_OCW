import math
import random
import ps6_visualize


class Position(object):
    """A Position object represents a point in a two-dimensional space"""
    def __init__(self,pos):
        """Initialize a Position object
        x and y are floats >= 0.0"""
        self.x = pos[0]
        self.y = pos[1]
    def get_x(self):
        """returns the x coordinate"""
        return self.x
    def get_y(self):
        """returns the y coordinate"""
        return self.y
    def __str__(self):
        return str((self.get_x(),self.get_y()))
    def get_new_position(self,angle,speed):
        """Return: a new position object representing Roomba's position after 1 unit of time
        angle: float representing radian measure
        speed: 0 < float
        Does not determine if the new position is inside the room
        """
        old_x, old_y = (self.get_x(),self.get_y())
        delta_x, delta_y = ((speed * math.cos(angle)), speed * math.sin(angle))
        new_x, new_y = (old_x + delta_x, old_y + delta_y)
        return Position((new_x,new_y))

class Tile(object):
    """A Tile Object"""
    def __init__(self,pos):
        """pos: tuple with two elements, (x,y)
        x: 0 <= int < width
        y: 0 <= int < height"""
        self.where = pos
        self.cleanliness = 'dirty'
    def cleaned(self):
        """sets the tile's cleanliness attribute to clean"""
        self.cleanliness = 'clean'
    def get_cleanliness(self):
        """returns cleanliness of the current tile"""
        return self.cleanliness
    def __str__(self):
        return 'tile ' + str(self.where) + ' is ' + str(self.cleanliness)

class Floor(object):
    """A Floor object
    """
    def __init__(self, width, height):
        """height and width are positive integers"""
        self.width = width
        self.height = height
        self.tiles = {}
        for x in range(width):
            for y in range(height):
                pos = (x,y)
                self.tiles[pos] = Tile(pos)
    
    def fraction_cleaned(self):
        """returns a float which equals the fraction of clean tiles vs total tiles"""
        cleaned = 0.0
        total = self.get_num_tiles()
        for tile in self.tiles:
            if self.tiles[tile].cleanliness == 'clean':
                cleaned += 1
        return cleaned / total
        
    def get_num_tiles(self):
        """returns the number of tiles in the room"""
        return len(self.tiles.keys())
    
    def how_many_clean_tiles(self):
        clean = 0
        for tile in self.tiles:
            if self.tiles[tile].get_cleanliness() == 'clean':
                clean += 1
        return clean
        
    def cleaning_progress(self):
        """prints the cleanliness of all the tiles in the room"""
        tiles = self.tiles.keys()
        tiles.sort()
        for tile in tiles:
            print self.tiles[tile]
    
    def get_random_spot(self):
        """gets a randoms spot on the floor"""
        x_spot = random.uniform(0.0,float(self.width))
        y_spot = random.uniform(0.0,float(self.height))
        return ((x_spot,y_spot))
    
    def is_on_floor(self,position):
        """Returns true if the (x,y) coordinate stored in position falls within (0,0) and (width,height)
        position: instance of Position object"""
        if position.get_x() < 0 or position.get_x() > self.width:
            return False
        elif position.get_y() < 0 or position.get_y() > self.height:
            return False
        else:
            return True
    def isTileCleaned(self,x_coordinate,y_coordinate):
        """Returns True if the tile is clean, False otherwise
        x_coordinate: 0 <= int <= width - 1
        y_coordinate: 0 <= int <= height - 1
        """
        the_tile = self.tiles[((int(x_coordinate),int(y_coordinate)))]
        if the_tile.get_cleanliness() == 'clean':
            return True
        elif the_tile.get_cleanliness() == 'dirty':
            return False
    
    def get_current_tile(self,position):
        """returns the tile corresponding to the current position"""
        tile_x = int(position.get_x())
        tile_y = int(position.get_y())
        return self.tiles[((tile_x,tile_y))]

class Roomba(object):
    """an object modeling the Roomba autonomous vacuum"""
    def __init__(self,floor,speed):
        """floor: Floor instance
        speed: float > 0
        """
        self.floor = floor
        self.speed = speed            
        self.angle = math.radians(random.uniform(0.0,360.0))
        self.location = Position(self.floor.get_random_spot())
    
    def get_direction(self):
        """return roomba's direction of motion"""
        return self.angle
    def get_location(self):
        """get roomba's location"""
        return self.location
    def get_angle(self):
        """get roomba's angle"""
        return self.angle
    def get_floor(self):
        """get roomba's floor"""
        return self.floor
    
    def reset_direction(self):
        """keeps Roomba from hitting walls
        """
        self.angle = math.radians(random.uniform(0.0,360.0))
        
    def move_and_clean(self,position):
        """moves roomba over one unit of time and cleans the tile it ends moves into
        position: Position instance
        """
        new_position = position.get_new_position(self.angle,self.speed)
        while not self.floor.is_on_floor(new_position):
            self.reset_direction()
            new_position = position.get_new_position(self.angle,self.speed)
        else:
            self.location = new_position
            current_tile = self.floor.get_current_tile(self.get_location())
            current_tile.cleaned()
            
class RandomRoomba(Roomba):
    """a roomba that changes direction after every move"""
    def __init__(self,floor,speed):
        Roomba.__init__(self,floor,speed)
        
    def move_and_clean(self,position):
        """like Roomba move and clean, but changes direction after each move.
        position: Position instance"""
        
        new_position = position.get_new_position(self.angle,self.speed)
        while not self.floor.is_on_floor(new_position):
            self.reset_direction()
            new_position = position.get_new_position(self.angle,self.speed)
        else:
            self.location = new_position
            self.reset_direction()
            current_tile = self.floor.get_current_tile(self.get_location())
            current_tile.cleaned()        
        
        
def run_trial(num_roombas,speed,width,height,min_coverage,roomba_model):
    """Runs one trial
    Return: int, amount of time it took to clean min_coverage of the tiles
    num_roombas: int >= 1
    speed: float > 0.0
    width: int > 0
    height: int > 0
    min_coverage: 0.0 <= float <= 1.0
    """
    #anim = ps6_visualize.RobotVisualization(num_roombas,width,height)
    the_floor = Floor(width,height)
    the_roombas = []
    for one_roomba in range(num_roombas):
        the_roombas.append(roomba_model(the_floor,speed)) 
    time = 0
    while the_floor.fraction_cleaned() < min_coverage:
        #anim.update(the_floor,the_roombas)        
        time += 1
        for roomba in the_roombas:
            roomba.move_and_clean(roomba.get_location())
    else:
        #anim.done()
        print 'cleaned everything'
        return time



import numpy
def run_simulation_(num_roombas,speed,width,height,min_coverage,num_trials,roomba_model):
    """runs a simulation
    num_trials: int >= 1"""
    times_needed = []
    for trial in range(num_trials):
        time = run_trial(num_roombas,speed,width,height,min_coverage,roomba_model)
        times_needed.append(time)
    return numpy.mean(times_needed)
    print 'average time to clean ' + str(100*min_coverage) + '% ' + 'of a ' + str(width) + ' by ' + str(height) + ' room: ' + str(sum(times_needed)/len(times_needed))

#==============================================================================
# print 't should be about 150'
# run_simulation_(1,1.0,5,5,1.0,1000,'meow')
# print 't should be about 190'
# run_simulation_(1,1.0,10,10,.75,10,'meow')
# print 't should be about 310'
# run_simulation_(1,1.0,10,10,.9,100,'meow')
# print 't should be about 3250'
# run_simulation_(1,1.0,20,20,1.0,100,'meow')
# 
#==============================================================================
import pylab
def more_roomba_more_clean(num_roombas,room_width,room_height):
    time_needed = []    
    for num_roomba in range(1,num_roombas):
        time = run_simulation_(num_roomba,1.0,room_width,room_height,1.0,15,'meow')
        time_needed.append(time)
    num_roombas = range(1,num_roombas)
    pylab.plot(num_roombas,time_needed)
    pylab.xlabel('number of roombas')
    pylab.ylabel('time required')
    pylab.xticks(range(1,len(num_roombas)))
    pylab.title('time it takes ' + str(len(num_roombas)) + ' roombas to clean a ' + str(room_width) + ' by ' + str(room_height) + ' room')
    pylab.show()

# time decreases exponentially with increases in roombas

def more_room_more_time():
    """plots relationship between room size and cleaning time"""
    room_sizes = [(20,20),(25,16),(40,10),(50,8),(80,5),(100,4)]    
    room_ratios = []
    average_times = []    
    for room in room_sizes:
        room_ratio = float(room[0])/room[1]
        room_ratios.append(room_ratio)
    for room_size in room_sizes:
        average_time = run_simulation_(8,1.0,room_size[0],room_size[1],1.0,100,'meow')
        average_times.append(average_time)
    pylab.plot(room_ratios,average_times)
    pylab.xlabel('width to height ratio')
    pylab.ylabel('time required for 2 roombas to finish cleaning')
    pylab.title('width to height ratio & cleaning time')
    pylab.show()        
    
def random_better_worse():
    random_roomba_average = run_simulation_(5,1.0,10,10,1.0,10,RandomRoomba)    
    normal_roomba_average = run_simulation_(5,1.0,10,10,1.0,10,Roomba)
    
# cleaning time for a fixed room size is independent of room proportions        
        
        