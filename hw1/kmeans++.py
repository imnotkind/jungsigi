import random
import math
import time
from kmeans import Kmeans

class KmeansPlusPlus(Kmeans): # inherit Kmeans
    def __init__(self, points, number_of_cluster=5, tolerance=0.001):
        super().__init__(points, number_of_cluster, tolerance)
        self.weights = [-1 for _ in points] #for kmeans++ initialization step
        
    
    def initialize_centroid(self):
        # initialize using distance
        while len(self.current_centroid) < self.number_of_cluster:
            if len(self.current_centroid) == 0:
                choice = random.choices(self.points, k=1)[0] # at first choose a center uniformly at random
                
                self.current_centroid.append((choice[1], choice[2]))
            else:
                for p in range(len(self.points)):
                    self.weights[p] = self.calculate_distance(self.current_centroid[-1], self.points[p]) ** 2 # calculate distance with latest chosen center
                choice = random.choices(self.points, weights=self.weights, k=1)[0] # give weights to random.choices to choose from a weighted probability distribution
                self.current_centroid.append((choice[1], choice[2]))

    
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
    
    k = KmeansPlusPlus(points)
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
        output_file.write("{},{}\n".format(cluster[p][0], cluster[p][1]))
    output_file.close()
    
    print("\nTotal elapsed time: {:.3f} sec".format(time.time() - t))

    