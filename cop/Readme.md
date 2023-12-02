Suppose there are n stations and denote the set of stations by S = {1, 2, ..., n}. Also, denote the time cost for traveling from station i to j by c_ij.
  We define an auxiliary function called f(i, S) that calculates the minimum time cost to reach station j from station i using the stations in set S.
The auxiliary function f(i, S) can be defined recursively:
f(i, S) = min(c_ij + f(j, S - {j})), for every j ∈ S and i ≠ j
The basic condition for this recursion is that if S contains only one member (|S| = 1), then f(i, S) is zero.
Using the auxiliary function f(i, S), we can calculate the minimum time cost between two stations using f(starting station number, set of all stations).
  By using the dynamic programming method and solving the auxiliary function f(i, S), it is possible to find the route that has the lowest cost.
