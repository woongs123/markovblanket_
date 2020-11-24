#!/usr/bin/env python
# coding: utf-8

# In[80]:


# Class Point and function definitions 

class point():
    
    # initial state
    x = 0
    y = 0
    zx = 0
    zy = 0
    entropy = 12
    height = 10 

    def __init__(self,grid_point): #2-d array world
        self.x += grid_point[0]
        self.y += grid_point[1]
        print(self.x)
        print(self.y)

    def State(self) : #return its Height 
        #Z-point
        self.zx = self.x - sign(self.x)
        self.zy = self.y - sign(self.y)
        print(self.zx)
        print(self.zy)
        
        #Entropy and Height state
        if(self.x==0 and self.y==0):
            self.entropy = 12
            self.height = 10
        else :
            self.entropy = ((self.zx + self.entropy) * (20151123 + self.zy) + 20200728) % 20201117
            print(self.entropy)
            self.height = self.height + 7 - (self.entropy % 15)
            print(self.height)
        return self.height
    
def sign(x) :
    if x>0 :
        return 1
    elif x==0 :
        return 0
    else :
        return -1

# Grid world  definition
start = [0,0]
up_move = [0,1]
down_move = [0,-1]
left_move =[-1,0]
right_move =[1,0]

# position 

start_position = [0,0]

def Move_or_Stay(start_point,end_point): #get parameter point instance
    if(end_point.y < 0) :
        print("Cant go down to the surface")
    elif(end_point.y > start_point.y) : 
        if(abs(start_point.State() - end_point.State()) >= 5) :
            print("You can't move to up because it is so high")
        else :
            start_position[1] += 1
    elif(end_point.y < start_point.y) : 
        if(abs(start_point.State() - end_point.State()) >= 5) :
            print("You can't move to down because it is so high")
        else :
            start_position[1] -= 1
    elif(end_point.x < start_point.x) : 
        if(abs(start_point.State() - end_point.State()) >= 5) :
            print("You can't move to left because it is so high")
        else :
            start_position[0] -= 1
    elif(end_point.x > start_point.x) : 
        if(abs(start_point.State() - end_point.State()) >= 5) :
            print("You can't move to right because it is so high")
        else :
           start_position[0] += 1
