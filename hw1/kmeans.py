import random
import math
import time
import matplotlib.pyplot as plt

class Kmeans:
    def __init__(self, points, number_of_cluster=5, tolerance=0.001):
        self.points = points # [(index, x, y), ...]
        self.number_of_cluster = number_of_cluster # literally number of clusters
        self.assigned_cluster = [(-1,-1) for _ in points] # what cluster did the point go to : (index of data point, cluster)
        self.current_centroid = [] # means of cluster centroid [(x,y), ...]
        self.previous_centroid = None # previous version of centroid, for calculating tolerance
        self.tolerance = tolerance # stop criteria for tolerance
    
    def calculate_distance(self, x1, x2 = (0,0)):
        # calculate euclidian distance
        
        sum_square = 0
        for i in range(2): # x has 2 dimensions
            sum_square += (x1[i] - x2[i])**2
        return math.sqrt(sum_square)
        
    
    def initialize_centroid(self):
        # randomly pick k observation from the dataset
        
        choices = random.choices(self.points, k=self.number_of_cluster)
        
        for choice in choices:
            self.current_centroid.append((choice[1], choice[2])) # append (x,y) of point
        
    
    def assign_points_to_cluster(self):
        # assign each point to cluster that has least squared Euclidian distance
        
        for p in range(len(self.points)):
            min_dist = None
            min_dist_cluster = -1
            
            for i in range(self.number_of_cluster):
                if min_dist == None:
                    min_dist = self.calculate_distance(self.current_centroid[i], self.points[p][1:]) ** 2
                    min_dist_cluster = i
                else:
                    dist = self.calculate_distance(self.current_centroid[i], self.points[p][1:]) ** 2
                    if dist < min_dist: # just pick the cluster with smaller index if distance is the same
                        min_dist = dist
                        min_dist_cluster = i
                        
            self.assigned_cluster[p] = (self.points[p][0], min_dist_cluster) # (index of data point, min dist cluster)
            
    
    def update_centroid(self):
        # recalculate means of data points assigned to each cluster
        
        ## update current centroid
        for i in range(self.number_of_cluster): # i : iteration of each cluster
            sum_points = [0,0] # sum of x,y value of points in cluster i
            cluster_size = 0 # num of points in cluster i
            
            for p in range(len(self.points)):
                if self.assigned_cluster[p][1] == i: # if assigned cluster of data point equals i
                    cluster_size += 1
                    
                    sum_points[0] += self.points[p][1] # add x
                    sum_points[1] += self.points[p][2] # add y

            if cluster_size == 0:
                self.current_centroid[i] = (-1, -1) # cluster has no member, not likely to happen
            else:
                self.current_centroid[i] = (sum_points[0] / cluster_size, sum_points[1] / cluster_size) # mean of data points
    
    def calculate_tolerance(self):
        # return tolerance value
        
        ## if it is the first assignment, algorithm shouldn't stop
        if(self.previous_centroid == None):
            self.previous_centroid = self.current_centroid[:] # shallow copy
            return None # continue algorithm
        
        result = 0    
        for i in range(self.number_of_cluster):
            result += self.calculate_distance(self.current_centroid[i], self.previous_centroid[i]) / self.calculate_distance(self.previous_centroid[i])
        
        ## check tolerance criteria
        if result <= self.tolerance: # stop algorithm when tolerance is lower or equal than criteria
            return (self.current_centroid, self.assigned_cluster) # stop algorithm
        else:
            self.previous_centroid = self.current_centroid[:] # shallow copy
            return None # continue algorithm

    

if __name__ == "__main__":
    t = time.time()
    
    points = []
    
    input_file = open("data.txt", "r")
    for line in input_file.readlines():
        l = line.rstrip().split(",")
        i = int(l[0])
        x = float(l[1])
        y = float(l[2])
        points.append((i, x, y))
    input_file.close()
    
    k = Kmeans(points)
    k.initialize_centroid()
    
    res = None
    while(res == None):
        k.assign_points_to_cluster()
        k.update_centroid()
        
        res = k.calculate_tolerance()
    centroid, cluster = res
    
    print("Detected centroid:")
    for i in range(len(centroid)):
        print("Centroid {}: {:.4f}, {:.4f}".format(i, centroid[i][0], centroid[i][1]))
        
    output_file = open("result.txt", "w")
    for p in range(len(cluster)):
        output_file.write("{},{}\n".format(cluster[p][0], cluster[p][1])) # index, cluster_no
    output_file.close()
    
    print("\nTotal elapsed time: {:.3f} sec".format(time.time() - t))

    
    