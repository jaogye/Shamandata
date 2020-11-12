# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 08:26:23 2020

@author: jaaxx
"""

eps = 0.000000001 # epsilon to tie-break  inequalities  

# Given the positions of the first and second players x°0 and x1 
# this method computes the end of game choosing the best postion for thrid 
# forth pmayers and then computes the correrspondig payoff u
#  Putput : x positions of the players, u: payoff of the players

def game(x0, x1):

# p saves the ascending order of the positions
  x = [x0, x1, 0, 0]; p= [0,0,0,0]; u= [0,0,0,0]
  if x[1] - x[0] >= 2 * max(x[0], 1-x[1]):
    x[2] = (x[0] + x[1])/2
    D = max(x[0], 1-x[1], (x[2] - x[0])/2, (x[1] - x[2])/2)

    if x[0] == D:
       x[3] = x[0] - eps
       # 0 < x[3] < x[0] < x[2] < x[1] < 1 
       p = [3,0,2,1]

    if x[2] - x[0] == 2 * D:
         x[3] = (x[2] + x[0])/2
         # 0 < x[0] < x[3] < x[2] < x[1] < 1 
         p = [0,3,2,1]

    if x[1] - x[2] == 2 * D:
       x[3] = (x[1] + x[2])/2
       # 0 < x[0] < x[2] < x[3] < x[1] < 1 
       p = [0,2,3,1]
    if 1-x[1] == D:
       x[3] = x[1] + eps
       # 0 < x[0] < x[2] < x[1] < x[3] < 1
       p = [0,2,1,3]

  if x[0] >= max( (x[1] - x[0])/2 , 1-x[1]):
     x[2] = max( (x[1] - x[0])/2 , 1-x[1], x[0]/3 ) - eps
     D = min((x[0]- x[2] )/2, (x[1] - x[0])/2 , 1-x[1]) 
     if x[0] - x[2] == 2*D:
        x[3] = (x[0] + x[2])/2
        # 0 < x[2] < x[3] < x[0] < x[1] < 1
        p = [2,3,0,1]

     if x[1] - x[0] == 2*D:
        x[3] = (x[1] + x[0])/2
        # 0 < x[2] < x[0] < x[3] < x[1] < 1
        p = [2,0,3,1] 

     if 1-x[1] == D:
        x[3] = x[1] + eps
        # 0 < x[2] < x[0] < x[1] < x[3] < 1
        p = [2,0,1,3]   


  if 1 - x[1] > max( (x[1] - x[0])/2 , x[0]):
     x[2] =  max( 1- (x[1] - x[0])/2 , 1-x[0], (2 + x[1])/3 ) + eps
     D = max((x[2] - x[1] )/2, (x[1] - x[0])/2 , x[0] ) 
     if x[2] - x[1] == 2*D:
        x[3] = (x[2] + x[1])/2 
        # 0 < x[0] < x[1] < x[3] < x[2] < 1
        p = [0,1,3,2] 

     if x[1] - x[0] == 2*D:
        x[3] = (x[1] + x[0])/2 
        # 0 < x[0] < x[3] < x[1] < x[2] < 1
        p = [0,3,1,2] 

     if x[0] == D:
        x[3] = x[0] - eps
        # 0 <x[3] < x[0] < x[1] < x[2] < 1
        p = [3,0,1,2]
                 

  x[2]=x[2] ; x[3]=x[3] 

  u[p[0]] = x[p[0]] + ( x[p[1]] -x[p[0]]) / 2 
  u[p[1]] = ( x[p[2]] -x[p[0]]) / 2 
  u[p[2]] = ( x[p[3]] -x[p[1]]) / 2
  u[p[3]]= 1 -x[p[3]] + (x[p[3]] -x[p[2]] ) /2 
  return u,x


# best2 saves the best positions for the second player based on the position
# of the first player
best2 = [ [0,0,0,0] for i in range(0,51) ] 
for i in range(0,51):
   best2[i][1] = -1
   for j in range(i+1,101): 
       u,x = game(i/100, j/100)
       if u[1] > best2[i][1]:
          best2[i][0] = x[1]
          best2[i][1] = u[1]          
          best2[i][2] = x[0]
          best2[i][3] = u[0]          

    
# Findding the best position  for the first player    
rmax = -1      
for i in range(len(best2)):
    if best2[i][1] > rmax:
       rmax = best2[i][3]
       kmax = best2[i][2]          
       
print('The optimal position for the first player is ', kmax)
       
       
