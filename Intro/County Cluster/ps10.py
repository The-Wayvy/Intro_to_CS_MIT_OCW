# Problem Set 10
# Name:
# Collaborators:
# Time:

#Code shared across examples
import pylab, random, string, copy, math

class Point(object):
    def __init__(self, name, originalAttrs, normalizedAttrs = None):
        """normalizedAttrs and originalAttrs are both arrays"""
        self.name = name
        self.unNormalized = originalAttrs
        self.attrs = normalizedAttrs
    def dimensionality(self):
        return len(self.attrs)
    def getAttrs(self):
        return self.attrs
    def getOriginalAttrs(self):
        return self.unNormalized
    def distance(self, other):
        #Euclidean distance metric
        difference = self.attrs - other.attrs
        return sum(difference * difference) ** 0.5
    def getName(self):
        return self.name
    def toStr(self):
        return self.name + str(self.attrs)
    def __str__(self):
        return self.name

class County(Point):
    weights = pylab.array([1.0] * 14)
    
    # Override Point.distance to use County.weights to decide the
    # significance of each dimension
    def distance(self, other):
        difference = self.getAttrs() - other.getAttrs()
        return sum(County.weights * difference * difference) ** 0.5
    
class Cluster(object):
    def __init__(self, points, pointType):
        self.points = points
        self.pointType = pointType
        self.centroid = self.computeCentroid()
    def getCentroid(self):
        return self.centroid
    def computeCentroid(self):
        dim = self.points[0].dimensionality()
        totVals = pylab.array([0.0]*dim)
        for p in self.points:
            totVals += p.getAttrs()
        meanPoint = self.pointType('mean',
                                   totVals/float(len(self.points)),
                                   totVals/float(len(self.points)))
        return meanPoint
    def update(self, points):
        oldCentroid = self.centroid
        self.points = points
        if len(points) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0
    def getPoints(self):
        return self.points
    def contains(self, name):
        for p in self.points:
            if p.getName() == name:
                return True
        return False
    def toStr(self):
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]
    def __str__(self):
        result = ''
        for p in self.points:
            result = result + str(p) + ', '
        return result[:-2]
        

    
def kmeans(points, k, cutoff, pointType, minIters = 3, maxIters = 100, toPrint = False):
    """ Returns (Cluster list, max dist of any point to its cluster) """
    #Uses random initial centroids
    initialCentroids = random.sample(points,k)
    clusters = []
    for p in initialCentroids:
        clusters.append(Cluster([p], pointType))
    numIters = 0
    biggestChange = cutoff
    while (biggestChange >= cutoff and numIters < maxIters) or numIters < minIters:
        print "Starting iteration " + str(numIters)
        newClusters = []
        for c in clusters:
            newClusters.append([])
        for p in points:
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            for i in range(len(clusters)):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            newClusters[index].append(p)
        biggestChange = 0.0
        for i in range(len(clusters)):
            change = clusters[i].update(newClusters[i])
            #print "Cluster " + str(i) + ": " + str(len(clusters[i].points))
            biggestChange = max(biggestChange, change)
        numIters += 1
        if toPrint:
            print 'Iteration count =', numIters
    maxDist = 0.0
    for c in clusters:
        for p in c.getPoints():
            if p.distance(c.getCentroid()) > maxDist:
                maxDist = p.distance(c.getCentroid())
    print 'Total Number of iterations =', numIters, 'Max Diameter =', maxDist
    print biggestChange
    return clusters, maxDist

#US Counties example
def readCountyData(fName, numEntries = 14):
    dataFile = open(fName, 'r')
    dataList = []
    nameList = []
    maxVals = pylab.array([0.0]*numEntries)
    #Build unnormalized feature vector
    for line in dataFile:
        if len(line) == 0 or line[0] == '#':
            continue
        dataLine = string.split(line)
        name = dataLine[0] + dataLine[1]
        features = []
        #Build vector with numEntries features
        for f in dataLine[2:]:
            try:
                f = float(f)
                features.append(f)
                if f > maxVals[len(features)-1]:
                    maxVals[len(features)-1] = f
            except ValueError:
                name = name + f
        if len(features) != numEntries:
            continue
        dataList.append(features)
        nameList.append(name)
    return nameList, dataList, maxVals
    
def buildCountyPoints(fName):
    """
    Given an input filename, reads County values from the file and returns
    them all in a list.
    """
    nameList, featureList, maxVals = readCountyData(fName)
    points = []
    for i in range(len(nameList)):
        originalAttrs = pylab.array(featureList[i])
        normalizedAttrs = originalAttrs/pylab.array(maxVals)
        points.append(County(nameList[i], originalAttrs, normalizedAttrs))
    return points

def randomPartition(l, p):
    """
    Splits the input list into two partitions, where each element of l is
    in the first partition with probability p and the second one with
    probability (1.0 - p).
    
    l: The list to split
    p: The probability that an element of l will be in the first partition
    
    Returns: a tuple of lists, containing the elements of the first and
    second partitions.
    """
    l1 = []
    l2 = []
    for x in l:
        if random.random() < p:
            l1.append(x)
        else:
            l2.append(x)
    return (l1,l2)

def getAveIncome(cluster):
    """
    Given a Cluster object, finds the average income field over the members
    of that cluster.
    
    cluster: the Cluster object to check
    
    Returns: a float representing the computed average income value
    """
    tot = 0.0
    numElems = 0
    for c in cluster.getPoints():
        tot += c.getOriginalAttrs()[1]

    return float(tot) / len(cluster.getPoints())


def test(points, k = 200, cutoff = 0.1):
    """
    A sample function to show you how to do a simple kmeans run and graph
    the results.
    """
    incomes = []
    print ''
    clusters, maxSmallest = kmeans(points, k, cutoff, County)

    for i in range(len(clusters)):
        if len(clusters[i].points) == 0: continue
        incomes.append(getAveIncome(clusters[i]))

    pylab.hist(incomes)
    pylab.xlabel('Ave. Income')
    pylab.ylabel('Number of Clusters')
    pylab.show()

        
points = buildCountyPoints('counties.txt')
#==============================================================================
# random.seed(123)
# testPoints = random.sample(points, len(points)/10)
#==============================================================================

def get_my_cluster(county_name):
    """returns the cluster containing your county, does this three times"""
    my_clusters = []
    for i in range(3):
        cluster_set, maxdist = kmeans(points,50,.1,County)
        for cluster in cluster_set:
            for point in cluster.points:
                if point.getName() == county_name:
                    my_clusters.append(cluster)
    return my_clusters

my_clusters = get_my_cluster('NYKings')
    
    
def graphRemovedErr(points, kvals = [25, 50, 75, 100, 125, 150], cutoff = 0.1):
    """
    Should produce graphs of the error in training and holdout point sets, and
    the ratio of the error of the points, after clustering for the given values of k.
    For details see Problem 1.
    """
    holdout_set, training_set = randomPartition(points,.2)
    cluster_set = []    
    for kval in kvals:
        clusters,dist = kmeans(training_set,kval,cutoff,County)
        cluster_set.append(clusters)
    # ^^^ get all the clusterings
    training_error = []
    # iterate over the list of clusters. Calculate total error for each cluster, then append
  
    for clusters in cluster_set:
        clusters_error = 0.0
        for cluster in clusters:
            clust_error = 0.0            
            for point in cluster.points:
                clust_error += point.distance(cluster.getCentroid())**2
            clusters_error += clust_error
        training_error.append(clusters_error)
    
    holdout_error = []
        # find the squared distance of each point from the nearest centroid
    for clusters in cluster_set:
        centroids = []
        error = 0.0
        for cluster in clusters:
            centroids.append(cluster.getCentroid())
        for point in holdout_set:
            min_dist = None
            for centroid in centroids:
                if point.distance(centroid)**2 < min_dist or min_dist == None:
                    min_dist = point.distance(centroid)**2
            error += min_dist
        holdout_error.append(error)
    
    ratios = []
    for i in range(len(training_error)):
        ratios.append(training_error[i]/holdout_error[i])
    pylab.figure()
    pylab.plot(kvals,training_error,'ro')
    pylab.plot(kvals,holdout_error,'go')
    pylab.figure()
    pylab.plot(kvals,ratios,'y-')    
    pylab.show()

#graphRemovedErr(points)

#my county 

def get_avg_pov(cluster):
    """Returns the average poverty of a cluster"""
    total = 0.0
    num = len(cluster.getPoints())
    for point in cluster.getPoints():
        total += point.getOriginalAttrs()[2]
    return total / num
    
def graphPredictionErr(points, dimension, kvals = [25, 50, 75, 100, 125, 150], cutoff = 0.1):
    """
    Given input points and a dimension to predict, should cluster on the
    appropriate values of k and graph the error in the resulting predictions,
    as described in Problem 3.
    """
    for x in range(14):
        County.weights[x] = 1
    
    holdout_set, training_set = randomPartition(points,.2)
    clusters_sets = []    
    for kval in kvals:
        clusters,dist = kmeans(training_set,kval,cutoff,County)
        clusters_sets.append(clusters)
    # for each set in cluster sets
    # find the average poverty of each cluster in the set
    # then for each point in holdout, take the closest centroid's cluster
    # and add (the_points_poverty - the_clusters_poverty)**2 to that k's error
    for x in range(14):
        if x == 2:
            County.weights[x] = 0
        else:
            County.weights[x] = 1
    
    errors = []
    for clusters_set in clusters_sets:
        error = 0.0
        avg_poverties = []
        centroids = []
        for cluster in clusters_set:
            avg_poverty = get_avg_pov(cluster)
            avg_poverties.append(avg_poverty)
            centroids.append(cluster.getCentroid())
        for point in holdout_set:
            min_dist = None
            min_index = None
            for i in range(len(centroids)):
                if point.distance(centroids[i])**2 < min_dist or min_dist == None:
                    min_dist = point.distance(centroids[i])**2
                    min_index = i
            error += (point.getOriginalAttrs()[2]-avg_poverties[min_index])**2
        errors.append(error)            
    
    for x in range(14):
        if x != 9 or x != 8:
            County.weights[x] = 0
        else:
            County.weights[x] = 1
    special_errors = []    
    for clusters_set in clusters_sets:
        error = 0.0
        avg_poverties = []
        centroids = []
        for cluster in clusters_set:
            avg_poverty = get_avg_pov(cluster)
            avg_poverties.append(avg_poverty)
            centroids.append(cluster.getCentroid())
        for point in holdout_set:
            min_dist = None
            min_index = None
            for i in range(len(centroids)):
                if point.distance(centroids[i])**2 < min_dist or min_dist == None:
                    min_dist = point.distance(centroids[i])**2
                    min_index = i
            error += (point.getOriginalAttrs()[2]-avg_poverties[min_index])**2
        special_errors.append(error)    
    
    for x in range(14):
        if x == 0 or x == 1:
            County.weights[x] = 1
        else:
            County.weights[x] = 0
    
    income_house_errors = []
    for clusters_set in clusters_sets:
        error = 0.0
        avg_poverties = []
        centroids = []
        for cluster in clusters_set:
            avg_poverty = get_avg_pov(cluster)
            avg_poverties.append(avg_poverty)
            centroids.append(cluster.getCentroid())
        for point in holdout_set:
            min_dist = None
            min_index = None
            for i in range(len(centroids)):
                if point.distance(centroids[i])**2 < min_dist or min_dist == None:
                    min_dist = point.distance(centroids[i])**2
                    min_index = i
            error += (point.getOriginalAttrs()[2]-avg_poverties[min_index])**2
        income_house_errors.append(error)        
    
    for x in range(14):
        if x == 2:
            County.weights[x] = 1
        else:
            County.weights[x] = 0
    poverty_errors = []
    for clusters_set in clusters_sets:
        error = 0.0
        avg_poverties = []
        centroids = []
        for cluster in clusters_set:
            avg_poverty = get_avg_pov(cluster)
            avg_poverties.append(avg_poverty)
            centroids.append(cluster.getCentroid())
        for point in holdout_set:
            min_dist = None
            min_index = None
            for i in range(len(centroids)):
                if point.distance(centroids[i])**2 < min_dist or min_dist == None:
                    min_dist = point.distance(centroids[i])**2
                    min_index = i
            error += (point.getOriginalAttrs()[2]-avg_poverties[min_index])**2
        poverty_errors.append(error)        
    
    
    pylab.plot(kvals,errors,'ro',label='all-pov')
    pylab.plot(kvals,special_errors,'go',label='only ed')
    pylab.plot(kvals,income_house_errors,'yo',label='inc + house')
    pylab.plot(kvals,poverty_errors,'ko',label='pov only')
    pylab.legend()
    pylab.show()
graphPredictionErr(points,2)            

        
    