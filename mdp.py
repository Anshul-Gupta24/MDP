# Sutton Chapter 3
# Special Staates: A, B
# Rewards = -1:out of grid, 10:anything from A, 5:anything from B, 0:else
# Actions: Equiprobable
# gamma = 0.9


import numpy as np


actions = [np.array((0,1)), np.array((0,-1)), np.array((1,0)), np.array((-1,0))]

def reward(coord,action):
    newcoord=coord+action
    A=np.array((1,4))
    B=np.array((3,4))


    if((np.equal(coord,A)).all()):
        return 10
    if((np.equal(coord,B)).all()):
        return 5
    elif(newcoord[0]<0 or newcoord[0] > 4 or newcoord[1] < 0 or newcoord[1] > 4):
        return -1
    else:
        return 0

def action(p):
    if(p<0.25):
        return actions[0]
    elif(p>=0.25 and p<0.5):
        return actions[1]
    elif(p>=0.5 and p<0.75):
        return actions[2]
    else:
        return actions[3]

def new_coord(coord,a):
            newcoord=coord+a
            A=np.array((1,4))
            B=np.array((3,4))

            if(newcoord[0]<0):
                newcoord[0]=0
            if(newcoord[0]>4):
                newcoord[0]=4
            if(newcoord[1]<0):
                newcoord[1]=0
            if(newcoord[1]>4):
                newcoord[1]=4
            if((np.equal(coord,A)).all()):
                newcoord=np.array((1,0))
            elif((np.equal(coord,B)).all()):
                newcoord=np.array((3,2))

            return newcoord
            

#value function

v = np.zeros(25)

gamma=0.9

coords=[0]*25
c=0
for i in range(0,5):
    for j in range(0,5):
        coords[c]=np.array((i,j))
        c+=1
    
linear_index=np.reshape(range(0,25),(5,5))

while(True): 
    vnew = np.zeros(25)
    for cd in coords:
        l=linear_index[tuple(cd)]
        for a in actions:
            newcoord = new_coord(cd,a)
            ld=linear_index[tuple(newcoord)]
            vnew[l] += (0.25 * (reward(cd,a) + gamma * v[ld]))

    if(np.sum(np.abs(v - vnew)) < 1e-4):
        break

    v=vnew

print v    
