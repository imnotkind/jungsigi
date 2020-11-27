# HW2 Report

20160463 성해빈



# Objective

Our objective is to make a SIR, SIRS, SIR with vaccine model and plot it, and observe the results. 



# Method and Algorithm

In the SIR model, every node (human) has 3 states : susceptible(S), infectious(I), and recovered(R). 

The probability that susceptible could change to infectious is beta. The infection probability of one susceptible node is calculated by the fraction of infected neighbors * beta.

The probability that infectious could change to recovered is gamma.

The probability that recovered could change to susceptible is zeta. Note that SIR model is the case when zeta=0, so nobody gets susceptible after recovering.



Initially, we set some random people into infectious status, with the fraction initial_inf. Then we start iterating the timestamp. Each timestamp, according to the probability stated above, every node has a chance to change its status. When the timestamp reaches tmax, we return the values of fraction of susceptible, infectious, and recovered people for each timestamp.



For SIR with vaccines, before we initiate state transition on all nodes, we pick a susceptible single target to change to recovered status. The most effective target is probably the one that has the most probability to get infected, with is the one that has the most infectious neighbors. So we count who has the most infectious neighbors, and change that node's status from susceptible to recovered right away. 



We test it with various networks, like complete graphs, or erdos renyi graphs, or barabasi_albert_graphs. Those networks each have different connections. We sample the results 10 times to reduce noise in the results.



# Discussion

### SIR : Complete Graph

The first graph is the SIR model with Complete(Fully connected) graph.

![image-20201127144343236](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201127144343236.png)

Note that initially, The number of Infectious population increases. Then it decreases, which means people are turning into recovered status gradually. Eventually, everyone gets recovered. S draws a decreasing line, I draws a hill, R draws an increasing line.

### SIR : Erdos Renyi Graph

![image-20201127144439096](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201127144439096.png)

Comparing to the Complete graph, the Erdos Renyi graph has fewer connections. So you can see it takes more time to infect people, and to recover. This is because connections are related to possibility in infection. The timing of everyone recovering is also slow, because infection is slow. 

### SIR : Barabasi Albert Graph

![image-20201127144454872](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201127144454872.png)

The configuration of the Barabasi Albert graph has approximately the same edges as Erdos Renyi graph. We can check that Erdos Renyi has 50059 edges, Barabasi Albert has 50191 edges. So the status of the connection determines the difference. Barabasi Albert tends to have "hubs", which means super nodes that have a lot of connectivity. Barabasi Albert has more concentrated influencers, whereas Erdos Renyi has  about the same amount of connections in every node. The results shows that Barabasi's case is a bit more faster in infection, and slower in full recovery than Erdos Renyi, although it's quite similar since the number of edges are similar. 



### SIRS : Barabasi Albert Graph

![image-20201127144506474](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201127144506474.png)

Now we have a probability of zeta : having a change from recovered to susceptible. This model definitely has more noise than SIR.  I think this is because this model is more unstable than SIR, since people's status are keep changing even after convergence, and SIR just maintained everyone fully recovered and no one's status changing after convergence. I could have smoothed it more by doing more runs, but I thought maintaining the other conditions the same with other models is important to observe and compare. The interesting thing is, no more full recovery. It seems like R, I, S are having an equibrillium not at a value of 0 or 1, unlike SIR models. 



### SIR with vaccine : Barabasi Albert Graph

![image-20201127155309991](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201127155309991.png)

With vaccines, we can clearly notice the maximum infected population decreased than just SIR model. Also, the increase of recovered population is faster. The choice of target was the susceptible one who had the most possibility to get infected, which is the one who has the max score of infected neighbors / neighbors. 

# Time spent on assignment

About 2 hours