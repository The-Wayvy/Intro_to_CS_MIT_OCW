# 6.00 Problem Set 11
#
# graph.py
#
# A set of data structures to represent graphs
#

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

class Weighted_Edge(Edge):
  def __init__(self, src, dest, tot_dist, out_dist):
    self.src = str(src)
    self.dest = str(dest)
    self.tot_dist = tot_dist
    self.out_dist = out_dist
  def getTotDist(self):
    return self.tot_dist
  def getOutDist(self):
    return self.out_dist

class Digraph(object):
  """
  A directed graph
  """
  def __init__(self):
    self.nodes = set([])
    self.edges = {}
  def addNode(self, node):
    node = node.getName()
    if node in self.nodes:
      pass
    else:
      self.nodes.add(node)
      self.edges[node] = []
  def addEdge(self, edge):
    src = edge.getSource()
    dest = edge.getDestination()
    if not(src in self.nodes and dest in self.nodes):
      raise ValueError('Node not in graph')
    self.edges[src].append(dest)
  def childrenOf(self, node):
    return self.edges[node]
  def hasNode(self, node):
    return node in self.nodes
  def __str__(self):
    res = ''
    for k in self.edges:
      for d in self.edges[k]:
        res = res + str(k) + '->' + str(d) + '\n'
    return res[:-1]

class Weighted_Digraph(Digraph):
  """
  A weighted digraph
  edges stored as a dictionary from source to a tuple of destination, total distance and outdoor distance
  """
  def addNode(self,node):
    if node in self.nodes:
      return
    self.nodes.add(node)
    self.edges[node] = {}
  def addEdge(self,edge):
    src = edge.getSource()
    dst = edge.getDestination()
    tot_dist = edge.getTotDist()
    out_dist = edge.getOutDist()
    if not (src in self.nodes and dst in self.nodes):
      raise ValueError('Node not in graph')
    self.edges[src][dst] = (tot_dist,out_dist)
  def childrenOf(self,node):
    return self.edges[node].keys()