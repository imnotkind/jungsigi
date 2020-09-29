import random
import math
import time
from kmeans import Kmeans

class KmeansPlusPlus(Kmeans):
    def __init__(self, points, number_of_cluster=5, tolerance=0.001):
        super().__init__(points, number_of_cluster, tolerance)
        self.weights = [-1 for _ in points] #for kmeans++ initialization step
    
    def calculate_distance(self, x, y = (0,0)):
        sum_square = 0
        for n in range(len(x)):
            sum_square += (x[n] - y[n])**2
        return math.sqrt(sum_square)
        
    
    def initialize_centroid(self):
        # initialize using distance
        while len(self.current_centroid) < self.number_of_cluster:
            if len(self.current_centroid) == 0:
                choice = random.choices(self.points, k=1)[0]
                self.current_centroid.append(choice[1:])
            else:
                for p in range(len(self.points)):
                    self.weights[p] = self.calculate_distance(choice, self.points[p]) / 2
                choice = random.choices(self.points, weights=self.weights, k=1)[0][1:]
                self.current_centroid.append(choice)
        

    
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

    
    