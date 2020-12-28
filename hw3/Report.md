# HW3 Report

20160463 성해빈



# Objective

Our objective is to implement 3 algorithms solving TSP and 2 improvement algorithms.



# Method and Algorithm

## Nearest Neighbor

randomly select starting node.

each time, add node that is closest to the last node of path.

if every node is added, connect last node with the first node.

## Nearest Addition

choose 2 nodes of minimal distance i, j.

create initial tour i-j-i.

choose node k and position that minimizes increase of length.

## Farthest Addition

start from random node i.

choose node j that is farthest from i.

create initial tour i-j-i.

choose node k that is farthest from nodes of tour.

add k in a position that minimizes increase of length



## 2OPT-full

keep changing the best 2-edge exchange that improves the tour, until no improvement is possible

## 2OPT-greedy

keep changing the first 2-edge exchange that improves the tour, until no improvement is possible



# Discussion

## Nearest Neighbor

![image-20201226072413926](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201226072413926.png)

![image-20201226072426380](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201226072426380.png)

![image-20201226072438679](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201226072438679.png)

nearest neighbor is quite fast, but we can see some "long lines" in the trajectory.

## Nearest Addition

![image-20201226072456277](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201226072456277.png)

![image-20201226072506182](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201226072506182.png)

![image-20201226072520961](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201226072520961.png)

nearest addition is quite slow compared to nearest neighbor, but we can clearly see some distance improvements, and we can clearly see that there are no "long lines", which is quite good.

## Farthest Addition

![image-20201226072537488](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201226072537488.png)

![image-20201226072549094](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201226072549094.png)

![image-20201226072559439](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201226072559439.png)

farthest addition is faster than nearest addition, and it has better output than nearest addition in some cases (TSP10, TSP100).



## 2OPT

for the optimization, I didn't have enough time.

the jupyter notebook has some uncompleted 2OPT implementations, but sadly I didn't have time to debug and fix it.







# Time spent on assignment

About 3 days