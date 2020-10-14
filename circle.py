##############################################################
# Euler code with variable acceleration in one dimension    #
##############################################################
# Brother Lines
# 2010 FEB 26
##############################################################
# This code will draw a circle
#  
##############################################################
# Load Libraries
import numpy as np
#import matplotlib
#matplotlib.use('tkagg')
import matplotlib.pyplot as plt

##############################################################
# Initial conditions

r=50.0       # distance from center in m
Theta0=0.00      # initial angle in degrees
delta_Theta=5  # change in angle in degrees

N= int(360/delta_Theta)+1       # number of points

pi=np.arccos(-1.0)           # calculate pi to machine percision
##############################################################
# define and zero arrays
x=np.zeros((N))
y=np.zeros((N))

##############################################################
# Draw Circle
y[0]=0        # initial y positoin
x[0]=r
theta=Theta0
for i in range (0,N):
    theta=theta+delta_Theta
    x[i]=np.cos(theta*pi/180)
    y[i]=np.sin(theta*pi/180)
   
    if x[i] != 0:
        theta_calc=np.arctan(y[i]/x[i])
    else:
        theta_calc=pi/2
    if y[i]>0 and x[i]>0:
        print("first quandrent")
    if y[i]>0 and x[i]<0:
        theta_calc=pi+theta_calc
        print("second quandrent")
    if y[i]<0 and x[i]>0:
        theta_calc=2*pi+theta_calc
        print("fourth quandrent")
    if y[i]<0 and x[i]<=0:
       theta_calc=theta_calc+pi
       print("third quandrent")

    print(theta,theta_calc*180/pi)
plt.plot(x,y)
