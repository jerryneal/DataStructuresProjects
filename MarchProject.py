
'''
    Author : Neal
    Date : 01/2014
    Description : This is a solution for the collecting coin problem
                   where we are running from the top-left corner of the
                   square to the lower-right corner.
                : **  WARNING :  Program keeps running till you select "Exit"               
    Class : CS 320 Project Work
'''

import random


class CoinCollectorStrategy(object):
    def __init__(self):
        pass


    def CoinRow():
        #This coin row algorithm finds bottom up the max amount of money that can be picked up
        #from a coin row without picking two adjacent coints
        coins = [None]
        while(len(coins)<10):#Generate a sample coin row of 10 coin values
            coins.append(random.randint(1,30))
        F = [0,coins[1]]
        for i in range(2,len(coins)):
            F.append(max(coins[i]+F[i-2],F[i-1]))
        print(coins)
        print(F)
        
    def RobotCoinCollector():
        n = 6
        m = 6
        matrix = [ [random.randint(0,1) for i in range(n) ] for j in range(m)]#generating matrix of 0s or 1s
        F = [ [0 for i in range(n) ] for j in range(m)] #generate helper matrix
        F[0][0]=matrix[0][0]
        for j in range(1,m):
            F[0][j]=F[0][j-1]+matrix[0][j]
        for i in range(1,n):
            F[i][0] = F[i-1][0] + matrix[i][0]
            for j in range(1,m):
                F[i][j]=max(F[i-1][j],F[i][j-1]+matrix[i][j])
        print(F[n-1][m-1])
        return F[n-1][m-1]

def main():

    optionNum = eval(input("Which do you want to run? \n1) CoinRow \n2)RobotCoinCollector\n3)Exit\n"))
    
    if optionNum == 1:
        CoinCollectorStrategy.CoinRow()
        
    elif optionNum == 2: 
        CoinCollectorStrategy.RobotCoinCollector()

    elif optionNum ==3:
        exit()

    else:
        print("invalid option, try again")
        main()
main()
