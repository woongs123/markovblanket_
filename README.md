# 클래스 Point 구현

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

    def State(self) : #return its Height 
        #Z-point
        self.zx = self.x - sign(self.x)
        self.zy = self.y - sign(self.y)
        
        #Entropy and Height state
        if(self.x==0 | self.y==0):
            self.entropy = 12
            self.height = 10
        else :
            self.entropy = ((self.zx + self.entropy) * (20151123 + self.zy) + 20200728) % 20201117
            self.height = self.height + 7 - (self.entropy % 15)
        return self.height

# Sign 함수 구현

def sign(x) :
    if x>0 :
        return 1
    elif x==0 :
        return 0
    else :
        return -1

# 어느쪽으로 갈지 정하고, 높이의 차이가 5이상나면 서있고, 아니면 움직임 

def Move_or_Stay(start_point,end_point): #get parameter point instance
    if(end_point.y < 0) :
        print("Cant go down to the surface")
    elif(end_point.y > start_point.y) : 
        if(abs(start_point.State() - end_point.State()) >= 5) :
            print("You can't move to up because it is so high")
        else :
            x = y
    elif(end_point.y < start_point.y) : 
        if(abs(start_point.State() - end_point.State()) >= 5) :
            print("You can't move to down because it is so high")
        else :
            x = y
    elif(end_point.x < start_point.x) : 
        if(abs(start_point.State() - end_point.State()) >= 5) :
            print("You can't move to left because it is so high")
        else :
            x = y
    elif(end_point.x > start_point.x) : 
        if(abs(start_point.State() - end_point.State()) >= 5) :
            print("You can't move to right because it is so high")
        else :
            x = y
