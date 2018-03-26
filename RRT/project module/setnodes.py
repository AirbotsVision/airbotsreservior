import math
import pygame
import sys
import matplotlib.pyplot as p
#pygame.init()
coordinates=eval(input("enter the coordinates"))            #enter the input coordinates
endcordinates=eval(input("enter the end coordinates"))
endor=endcordinates
xpointslist=[]
ypointslist=[]
stepsize=1
noofsteps=eval(input("enter the no of steps"))              #enter the stepsize
n=eval(input("enter the size you want to seperate"))
def setnodes(coordinates,n):
    ang=360//n
    if(ang==90):
        up(coordinates)
        down(coordinates)
        left(coordinates)
        right(coordinates)                                  #check whether the angle is 90 or not
    else:
        up(coordinates)
        upright(ang)
        left(coordinates)
        downright(ang)
        down(coordinates)
        downleft(ang)
        left(coordinates)
        upleft(ang)
	 		
def setnode1(x):
	left(x)
	right(x)
	up(x)                                                 #assign common direction function to a node'
	down(x)
	
def left(points):
	x=(points[0]-stepsize,points[1])                      #assign individual points to the node
	check(x)

def right(points):
	x=(points[0]+stepsize,points[1])
	check(x)

def upright(angle):
	a=math.sin(angle)
	b=math.cos(angle)
	x=(a,b)
	check(x)                                             

def upleft(angle):
	a=math.sin(angle)
	b=math.cos(angle)
	x=((-a),b)
	check(x)

def downright(angle):
	a=math.sin(angle)                                  #calculate the next pair  of nodes for both straight line and cross line 
	b=math.cos(angle)
	x=(a,(-b))
	check(x)

def downleft(angle):                            #for cross line calculate using angle betweeen th nearest lines
	a=math.sin(angle)
	b=math.cos(angle)
	x=((-a),(-b))
	check(x)

def up(points):                                     #for straight line calculate using tyhe stepsize
	x=(points[0],points[1]+stepsize)
	check(x)

def down(points):
	x=(points[0],points[1]-stepsize)
	check(x)

def check(x):
	n=len(x)
	count=0                                        #check whether any point of node is grreater than the end coordinates
	for i in range(0,n):
		if(x[i]>float(endor[i])):
			break
		else:
			count+=1
	if count==2:
		append(x)


def append(x):
    xpointslist.append(x[0])
    ypointslist.append(x[1])                    #after checking append the nodein to a list and print it
	
#def another(xpointslist,ypointslist):
#    setnode1(xpointslist)
#    setnode1(ypointslist)
    
setnodes(coordinates,n)
#another(xpointslist,ypointslist)

def plot(xpointslist,ypointslist):
    n=len(xpointslist)
    for i in range(0,n):
        p.plot(xpointslist[i],ypointslist[i],color="green",marker='o',linestyle="dashed",linewidth=12,markersize=1)
    p.show()

#def draw(xpointslist,ypointslist):
#    screen=pygame.display.set_mode((640,480))
#    red=(255,0,0)
#    blue=(0,0,255)
#    screen.fill(blue)
#    pygame.draw.lines(screen,red,xpointslist,1)
#    pygame.display.update()
plot(xpointslist,ypointslist)
#draw(xpointslist,ypointslist)
x=len(xpointslist)
print(x)
print(xpointslist)
print(ypointslist)