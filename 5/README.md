# ID2222 Assignment report 5

Authors:

- Marco Dallagiacoma [<marcoda@kth.se>](mailto:marcoda@kth.se)
- Roberto Bampi [<bampi@kth.se>](mailto:bampi@kth.se)

The purpose of this first assignment is to implement the JaBeJa algorithm for balanced graph partitioning.

The code is implemented using the provided boilerplate.
In particular the code was modified to add a few new command line parameters to accomodate for the requirements of the exercise.
The parameters added are the following:

* `-acceptanceFunction` which controls the acceptance function to use. 
The alternatives are `SIMPLE` which is the linear algorithm provided in the original paper and `EXPONENTIAL` which uses the formula 
$$p = \mathrm{e}^{\frac{old_c - new_c}{T}}$$ to calculate the probability of the swap.

* `-restartAfter` which controls whether or not the simulated annealing process will be restarted. If the parameter is a positive integer, such as 400, the simulated annealing will be restarted when the specified number of iterations is reached. A value of -1, the default, disables this behavior.



# Results
The resulting program was run on the _3elt_, _add20_, _facebook_ and _twitter_ multiple times with different parameters.
Each graph was processed with both the `SIMPLE` and `EXPONENTIAL` acceptance function and both with and without restarts at 600 iterations.
The resulting graphs are attached below.

## 3elt

### exponential
![plot](plots/3elt.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_1.0_D_0.9_RNSS_3_URSS_6_A_2.0_R_1000_AF_EXPONENTIAL_RA_-1.txt.png)

### exponential with restart
![plot](plots/3elt.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_1.0_D_0.9_RNSS_3_URSS_6_A_2.0_R_1000_AF_EXPONENTIAL_RA_600.txt.png)

### simple
![plot](plots/3elt.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_2.0_D_0.03_RNSS_3_URSS_6_A_2.0_R_1000_AF_SIMPLE_RA_-1.txt.png)

### simple with restart
![plot](plots/3elt.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_2.0_D_0.03_RNSS_3_URSS_6_A_2.0_R_1000_AF_SIMPLE_RA_600.txt.png)

## add20

### exponential
![plot](plots/add20.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_1.0_D_0.9_RNSS_3_URSS_6_A_2.0_R_1000_AF_EXPONENTIAL_RA_-1.txt.png)

### exponential with restart
![plot](plots/add20.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_1.0_D_0.9_RNSS_3_URSS_6_A_2.0_R_1000_AF_EXPONENTIAL_RA_600.txt.png)

### simple
![plot](plots/add20.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_2.0_D_0.03_RNSS_3_URSS_6_A_2.0_R_1000_AF_SIMPLE_RA_-1.txt.png)

### simple with restart
![plot](plots/add20.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_2.0_D_0.03_RNSS_3_URSS_6_A_2.0_R_1000_AF_SIMPLE_RA_600.txt.png)

## facebook

### exponential
![plot](plots/facebook.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_1.0_D_0.9_RNSS_3_URSS_6_A_2.0_R_1000_AF_EXPONENTIAL_RA_-1.txt.png)

### exponential with restart
![plot](plots/facebook.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_1.0_D_0.9_RNSS_3_URSS_6_A_2.0_R_1000_AF_EXPONENTIAL_RA_600.txt.png)

### simple
![plot](plots/facebook.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_2.0_D_0.03_RNSS_3_URSS_6_A_2.0_R_1000_AF_SIMPLE_RA_-1.txt.png)

### simple with restart
![plot](plots/facebook.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_2.0_D_0.03_RNSS_3_URSS_6_A_2.0_R_1000_AF_SIMPLE_RA_600.txt.png)

## twitter

### exponential
![plot](plots/twitter.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_1.0_D_0.9_RNSS_3_URSS_6_A_2.0_R_1000_AF_EXPONENTIAL_RA_-1.txt.png)

### exponential with restart
![plot](plots/twitter.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_1.0_D_0.9_RNSS_3_URSS_6_A_2.0_R_1000_AF_EXPONENTIAL_RA_600.txt.png)

### simple
![plot](plots/twitter.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_2.0_D_0.03_RNSS_3_URSS_6_A_2.0_R_1000_AF_SIMPLE_RA_-1.txt.png)

### simple with restart
![plot](plots/twitter.graph_NS_HYBRID_GICP_ROUND_ROBIN_T_2.0_D_0.03_RNSS_3_URSS_6_A_2.0_R_1000_AF_SIMPLE_RA_600.txt.png)
