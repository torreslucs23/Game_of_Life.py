

#############################################
#############################################
#############################################
### Name: LUCAS DE ARAUJO TORRES          ###
###                                       ###
### this is a simple project called game  ###
### of life. works with cells that are    ###
### born and die depending on game rules  ###
###                                       ###
### 1-Any live cell with fewer than two   ###
### live neighbours dies, as if by        ###
### underpopulation.                      ###
###                                       ###
### 2-Any live cell with two or three     ###
### live neighbours lives on to the next  ###
### generation.                           ###
###                                       ###
### 3-Any live cell with more than three  ###
### live neighbours dies, as if by        ###
### overpopulation.                       ###
###                                       ###
### 4-Any dead cell with exactly three    ###
### live neighbours becomes a live        ###
### cell, as if by reproduction.          ###
#############################################
#############################################
#############################################


import time
import random

#creates an empty map
def empty_map(m):
    for i in range(30):
        array=[]
        for w in range (50):
            array.append(" ")
        m.append(array)
    return m

#creates an empty array of values
def empty_values(m):
    for i in range(30):
        array=[]
        for w in range (50):
            array.append(0)
        m.append(array)
    return m

#print the map
def print_map(m):
    for i in m:
        print(" ".join(i))

#creates a map with random position 
def setup_map(m):
    for i in range (len(m)):
        for w in range(len(m[i])):
            x=random.randint(1,4)
            if (x==1):
                m[i][w]="*"
    return m


#set of functions that check neighboring cells and count
def verif_leftSide(n,m,x,y):
    w=y-1
    if (w==-1):
        w=len(m[0])-1
    if (m[x][w]=="*"):
        n[x][y]+=1
    return n

def verif_rightSide(n,m,x,y):
    w=y+1
    if (w==len(m[0])):
        w=0
    if (m[x][w]=="*"):
        n[x][y]+=1
    return n

def verif_upper(n,m,x,y):
    w=x-1
    if (w==-1):
        w=len(m)-1
    if (m[w][y]=="*"):
        n[x][y]+=1
    return n

def verif_downSide(n,m,x,y):
    w=x+1
    if (w==len(m)):
        w=0
    if (m[w][y]=="*"):
        n[x][y]+=1
    return n


def verif_leftUpperDiagonal(n,m,x,y):
    w,k = x-1,y-1
    if (w == -1):
        w = len(m)-1        
    if (k == -1):
        k = len(m[0])-1
    if (m[w][k] == "*"):
        n[x][y] += 1
    return n

def verif_rightUpperDiagonal(n,m,x,y):
    w,k = x-1,y+1
    if (w == -1):
        w = len(m)-1        
    if (k == len(m[0])):
        k = 0
    if (m[w][k] == "*"):
        n[x][y] += 1
    return n

def verif_leftDownDiagonal(n,m,x,y):
    w,k = x+1,y-1
    if (w == len(m)):
        w = 0        
    if (k == -1):
        k = len(m[0])-1
    if (m[w][k] == "*"):
        n[x][y] += 1
    return n

def verif_rightDownDiagonal(n,m,x,y):
    w,k = x+1,y+1
    if (w == len(m)):
        w = 0        
    if (k == len(m[0])):
        k = 0
    if (m[w][k] == "*"):
        n[x][y] += 1
    return n

#function that updates the map according to the data of the neighbors
def update_map(m,n):
    for i in range (len(n)):
        for w in range(len(n[0])):
            if (n[i][w]<2 or n[i][w]>3):
                m[i][w] = " "
            elif (n[i][w]==3 and m[i][w]==" "):
                  m[i][w] = "*"
    return m



#multidimensional array m is the map
m=empty_map([])
#multidimensional array n contains the neighbors values of each cell
n=empty_values([])

m=setup_map(m)
print_map(m)

print("""_______________________________________________________________________
_______________________________________________________________________________
_____________________________________________________________________________""")

time.sleep(1)

print("\n"*130)

while True:
    for x in range(len(m)):
        for y in range(len(m[0])):
            #first check the neighbors values of each cell and increments in the array
            n=verif_leftSide(n,m,x,y)
            n=verif_rightSide(n,m,x,y)
            n=verif_upper(n,m,x,y)
            n=verif_downSide(n,m,x,y)
            n=verif_leftUpperDiagonal(n,m,x,y)
            n=verif_rightUpperDiagonal(n,m,x,y)
            n=verif_leftDownDiagonal(n,m,x,y)
            n=verif_rightDownDiagonal(n,m,x,y)
    #updates the map through the values of n array
    m=update_map(m,n)
    #empty the array
    n=empty_values([])
    print_map(m)
    time.sleep(1)
    print("""______________________________________________________________________________________________________
__________________________________________________________________________________________________________________
__________________________________________________________________________________________________________________""")
    print("\n"*130)


            
