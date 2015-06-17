'''
    Title  : closest_pair.py
    Author : Neal, Heui and Niyi
    Date   : 06/17/2015
    Description : February Project to determine the closest pair in a set of graph points for CS 320
'''

import time
import math
import random

class CP:

    def __init__(self,n):
        self.P = []
        self.Q = []
        self.P_list = []
        
    #This function calculates the closest pair    
    def eff_closest_pair(self,P,Q):
        n = len(P)
        if n <= 3:
            return self.min_dist(P)
        else:
            P_l,P_r = P[:n//2],P[n//2:]
            Q_l,Q_r = Q[:n//2],Q[n//2:]
            d_l = self.eff_closest_pair(P_l,Q_l)
            d_r = self.eff_closest_pair(P_r,Q_r)
            d = min(d_l,d_r)
            
            m = P[:(n//2) -1]
            S = []
            for i in P:
                for k in m:
                    for j in Q:
                        if abs(i - k) < d:
                            S.append((i,j))
            
            dminsq = d**2
            num = len(S)
            for i in range(0,num):
                k = i+1
                while k <= num - 1 and (S[k][1] - S[i][1])**2 < dminsq:
                    dminsq = min((S[k][0]- S[i][0])**2 + (S[k][1] - S[i][1])**2,dminsq)
                    k+=1
        return math.sqrt(dminsq)
        
	 #This function calculates the minimum distance
    def min_dist(self,P):
        f = len(P)
        d = float('inf')
        for i in range(1,f-1):
            for j in range(i+1,f):
                p,q = P[i],P[j]
                d=min(d,(math.sqrt(((p-q)**2) + (p-q)**2)))
        return d
        
    #This function generates random points
    def gen_rand_points(self,n):
        self.P = []
        low,high = 0,100
        for i in range(n):
            rand = random.randint
            x = rand(low+1, high-1)
            y = rand(low+1, high-1)
            self.P.append((x,y))
        return self.P

def main():
    n = eval(input("Enter the random number of points:" ))
    newCP = CP(n)
    P_list = newCP.gen_rand_points(n)
    P = [P_list[0][0] for P_list[0] in P_list]
    Q = [P_list[0][1] for P_list[0] in P_list]
    v = newCP.eff_closest_pair(P,Q)
    print("The closest pair is", v)

if __name__== '__main__':
    main()
            


    
                    
            
