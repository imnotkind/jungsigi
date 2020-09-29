import random
import math
import time

class Kmeans:
    def __init__(self, points, number_of_cluster=5, tolerance=0.001):
        self.points = points
        self.number_of_cluster = number_of_cluster
        self.assigned_cluster = [-1 for _ in points] # what cluster did the point go to
        self.current_centroid = [] # means of cluster centroid
        self.previous_centroid = []
        self.tolerance = tolerance
    
    def calculate_distance(self, x, y = (0,0)):
        sum_square = 0
        for n in range(len(x)):
            sum_square += (x[n] - y[n])**2
        return math.sqrt(sum_square)
        
    
    def initialize_centroid(self):
        # randomly pick k observation from the dataset
        
        choices = random.choices(self.points, k=self.number_of_cluster)
        #choices = self.points[:self.number_of_cluster]
        
        for choice in choices:
            self.current_centroid.append((choice[1], choice[2]))
        
        
        
    
    def assign_points_to_cluster(self):
        # assign each point to cluster that has least MSE
        
        for p in range(len(self.points)):
            min_mse = None
            min_mse_cluster = -1
            
            for i in range(self.number_of_cluster):
                if min_mse == None:
                    min_mse = self.calculate_distance(self.current_centroid[i], self.points[p][1:])
                    min_mse_cluster = i
                else:
                    mse = self.calculate_distance(self.current_centroid[i], self.points[p][1:])
                    if mse < min_mse:
                        min_mse = mse
                        min_mse_cluster = i
                        
            self.assigned_cluster[p] = min_mse_cluster
               
    
    def update_centroid(self):
        # recalculate means of data points assigned to each cluster
        
        ## update current centroid
        for i in range(self.number_of_cluster):
            sum_points = [0,0]
            cluster_size = 0
            
            for p in range(len(self.points)):
                if self.assigned_cluster[p] == i:
                    point = self.points[p]
                    cluster_size += 1
                    sum_points[0] += point[1]
                    sum_points[1] += point[2]
            if cluster_size == 0:
                self.current_centroid[i] = (-1, -1)
            else:
                self.current_centroid[i] = (sum_points[0] / cluster_size, sum_points[1] / cluster_size)
        
        ## check tolerance
        if self.calculate_tolerance() <= self.tolerance:
            return (self.current_centroid, self.assigned_cluster) # stop algorithm
        else:
            self.previous_centroid = self.current_centroid[:] #deep copy
            return True # continue algorithm
    
    def calculate_tolerance(self):
        result = 0
        if(len(self.previous_centroid) == 0):
            self.previous_centroid = self.current_centroid[:] #deep copy
            
        for i in range(self.number_of_cluster):
            result += self.calculate_distance(self.current_centroid[i], self.previous_centroid[i]) / self.calculate_distance(self.previous_centroid[i])
        return result

    
    

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
    
    res = True
    while(res == True):
        k.assign_points_to_cluster()
        res = k.update_centroid()
    centroid, cluster = res
    
    for i in range(len(centroid)):
        print("Centroid {}: {:.4f}, {:.4f}".format(i, centroid[i][0], centroid[i][1]))
        
    output_file = open("result.txt", "w")
    for p in range(len(cluster)):
        output_file.write("{},{}\n".format(p, cluster[p]))
    output_file.close()
    
    print("Total elapsed time: {:.3f} sec".format(time.time() - t))

    
    