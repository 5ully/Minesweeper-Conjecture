'''
Created on Oct 17, 2022

@author: Torgeir Sulheim
'''

'''
Game Restrictions:

* The board must be quadratic, with side length of N.
* There must be N mines on a board with dimensions N x N.
* N must be greater, or equal to 2.

'''
import random
import numpy as np
from scipy.ndimage import convolve

def minesweeper(N):
    arr = np.array([[0 for row in range(N)] for column in range(N)])
    for i in range(N):
        x = random.randint(0, N-1)
        y = random.randint(0, N-1)
        arr[x][y] = 1   

    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    
    c = convolve(arr, kernel, mode = 'constant')
    
    return(c)

def MonteCarlo(N, R):
    
    '''
    N is the max board size
    R is the repetitions count
    '''
    avg = np.array([])
    avg_diff = np.array([])
    
    for i in range(2, N):
        val = np.array([])
        for j in range(R):
            val = np.append(val, np.sum(minesweeper(i)))
            
        
        avg = np.append(avg, np.average(val))
    
    for i in range(1, len(avg)):
        if i == 0:
            avg_diff = np.append(avg_diff, avg[i])
        else:
            avg_diff = np.append(avg_diff, avg[i]-avg[i-1])
    
    total_avg = np.average(avg_diff)
    
    res = total_avg/2.5
    print(res)
        
    
    
        