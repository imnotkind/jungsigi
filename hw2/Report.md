# HW2 Report

20160463 성해빈



# Objective

Our objective is to make a SIR, SIRS, SIR with vaccine model and plot it, and observe the results. 



# Method and Algorithm

In the SIR model, every node (human) has 3 states : susceptible(S), infectious(I), and recovered(R). 

The probability that susceptible could change to infectious is beta. Note that this is an independent event on every infectious neighbor on that node. So the total probability is 1 - p(getting uninfected by all infectious neighbors) = 1 - (1-beta)^(number of infectious neighbors)

The probability that infectious could change to recovered is gamma.

The probability that recovered could change to susceptible is zeta. Note that SIR model is the case when zeta=0, so nobody gets susceptible after recovering.



Initially, we set some random people into infectious status, with the fraction initial_inf. Then we start iterating the timestamp. Each timestamp, according to the probability stated above, every node has a chance to change its status. When the timestamp reaches tmax, we return the values of fraction of susceptible, infectious, and recovered people for each timestamp.



For SIR with vaccines, before we initiate state transition on all nodes, we pick a susceptible single target to change to recovered status. The most effective target is probably the one that has the most probability to get infected, with is the one that has the most infectious neighbors. So we count who has the most infectious neighbors, and change that node's status from susceptible to recovered right away. 



We test it with various networks, like complete graphs, or erdos renyi graphs, or barabasi_albert_graphs. Those networks each have different connections. We sample the results 10 times to reduce noise in the results.



# Discussion

### SIR : Complete Graph

The first graph is the SIR model with Complete(Fully connected) graph.

![image-20201125224924462](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201125224924462.png)

Note that initially, The number of Infectious population rapidly increases. Then it decreases, which means people are turning into recovered status gradually. Eventually, everyone gets recovered.

### SIR : Erdos Renyi Graph

![image-20201125225335190](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201125225335190.png)

Comparing to the Complete graph, the Erdos Renyi graph has fewer connections. So you can see it takes more time to infect people, and the peak of infectious people are lower than the complete graph. This is because connections are related to possibility in infection. The timing of everyone recovering is also slow, because infection is slow. 

### SIR : Barabasi Albert Graph

![image-20201125225616231](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201125225616231.png)

The Barabasi Albert Graph is even more sparse than the Erdos Renyi graph. It takes more time to infect people, and it takes more time for everyone to get recovered. Basically, the connection of networks decide how the SIR result looks like, because that's the only factor that decides the probability of infection when every other parameters, like beta, gamma, initial_inf are the same, like in this case.

### SIRS : Barabasi Albert Graph

![image-20201125230746434](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201125230746434.png)

Now we have a probability of zeta : having a change from recovered to susceptible. This model definitely has more noise than SIR.  I think this is because this model is more unstable than SIR, since people's status are keep changing even after convergence, and SIR just maintained everyone fully recovered and no one's status changing after convergence. I could have smoothed it more by doing more runs, but I thought maintaining the other conditions the same with other models is important to observe and compare. The interesting thing is, no more full recovery. It seems like R, I, S are having an equibrillium not at a value of 0 or 1, unlike SIR models. 



### SIR with vaccine : Barabasi Albert Graph

![image-20201125231139849](C:\Users\haebin\AppData\Roaming\Typora\typora-user-images\image-20201125231139849.png)

With vaccines, the speed of recovery gets faster, since we have a shorcut to susceptible -> recovered. But like our current status of the world, we have too less amounts of vaccines, only 1 per t in this example. So the change is barely noticable. 

# Time spent on assignment

About 2 hours