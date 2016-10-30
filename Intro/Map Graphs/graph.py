# 6.00 Problem Set 11
#
# graph.py
#
# A set of data structures to represent graphs
#

# note: __repr__ is used both when an object is returned
# note: __str__ is used when an object is printed

class Node(object):
   def __init__(self, name):
       self.name = str(name)
   def getName(self):
       return self.name
   def __str__(self):
       return self.name
   def __repr__(self):
      return self.name
   def __eq__(self, other):
      return self.name == other.name
   def __ne__(self, other):
      return not self.__eq__(other)

class Edge(object):
   def __init__(self, src, dest):
       self.src = src
       self.dest = dest
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def __str__(self):
       return str(self.src) + '->' + str(self.dest)

#==============================================================================
# class WeightedEdge(Edge):
#     def __init__(self, src, dest, tot_dist, out_dist):
#         self.src = src
#         self.dest = dest
#         self.tot_dist = tot_dist
#         self.out_dist = out_dist
#     def getTotalDistance(self):
#         return self.tot_dist
#     def getOutDoorDistance(self):
#         return self.out_dist
#     def __str__(self):
#         return str(self.src) + '->' + str(self.dest) + '. Distance: ' + str(self.tot_dist) + ', Outdoor Distance: ' + str(self.out_dist)
#==============================================================================

class Digraph(object):
   """
   A directed graph
   """
   def __init__(self):
       """
       nodes: list of strings
       edges: keys are strings, map to a list of strings
       """
       self.nodes = []
       self.edges = {}
   def addLine(self, source, destination):
       """
       lalala
       """
       if source in self.nodes:
           pass
       else:
           self.nodes.append(source)
           self.edges[source] = []
       self.edges[source].append(destination)
   def childrenOf(self, node):
       return self.edges[node]
   def hasNode(self, node):
       return node in self.nodes
   def __str__(self):
       res = ''
       for k in self.edges:
           for d in self.edges[k]:
               res = res + k + ' -> ' + d + ' -> '
       return res[:-4]

#==============================================================================
# class WeightedDigraph(Digraph):
#     """
#     A directed graph with weights
#     """
#     def addEdge(self,edge):
#         """
#         adds a weighted edge
#         source is represented as a dictionary key
#         destination, total distance, and outdoor distance are represented as a tuple inside the list value corresponding to the source key
#         """
#         src = edge.getSource()
#         dest = edge.getDestination()
#         tot_dist = edge.getTotalDistance()
#         out_dist = edge.getOutDoorDistance() 
#         the_node = None
#         for nowd in self.nodes:
#             if src == nowd:
#                 the_node = nowd
#                 break
#         for nowd_2 in self.nodes:
#             if dest == nowd_2:
#                 the_noder = nowd_2 
#         self.edges[the_node].append((the_noder,tot_dist,out_dist))       
#==============================================================================

def load_map(mapFilename):
    """
    Constructs an unweighted map
    """
    mit_map = Digraph()
    map_data = open(mapFilename,'r')
    for line in map_data:
        line = line.rstrip()
        line = line.split()
        source,destination = (line[0],line[1])
        mit_map.addLine(source,destination)
    map_data.close()
    return mit_map

mit_map = load_map('mit_map.txt')



def find_all_paths(digraph,start,end,path=[],visited=[]):
    """
    print all valid paths from start to end
    """   
    if start == end:
        path.append(start)
        visited.append(start)
        the_way = ''
        for building in path:
            the_way += building + ' -> '
        print 'The Way:',the_way[:-4]
    
    else:
        if start not in visited: 
            path.append(start)
            visited.append(start)
            for next_building in digraph.edges[start]:
                find_all_paths(digraph,next_building,end,path[:],visited[:])
                
find_all_paths(mit_map,'32','50')