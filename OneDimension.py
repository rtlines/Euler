##############################################################
# Euler code with variable acceleration in one dimension    #
##############################################################
# Brother Lines
# 2010 FEB 26
##############################################################
# This code will perform two functions
#  1) It will calculate the exact solution for a projectile
#     system using the theoretical result with no drag
#  2) It will calculate the result using Euler's method
##############################################################
# Load Libraries
import numpy as np
#import matplotlib
#matplotlib.use('tkagg')
import matplotlib.pyplot as plt

##############################################################
# Initial conditions
G=6.67E-11    # N s**2/m**2
a=0.98
m=0.020       # mass of object in kilograms
M=6E24        # mass of earth
g=9.8         # acceleration due to gravity m/s^2
y0=7000000.0       # initial y position in m
v0=0         # initial velocity

##############################################################
## Set up the time steps and number of calcualtions
deltat=1.0        # Time steps of 0.01 seconds
ti=0              # starting at t=0
tf=80000       # final time
N=int((tf-ti)/deltat)  # calcualte how many time steps are in 20 seconds
##############################################################
# Preliminary calculations
pi=np.arccos(-1.0)           # calculate pi to machine percision


##############################################################
# define and zero arrays
t=np.zeros((N))
x=np.zeros((N))
y=np.zeros((N))
z=np.zeros((N))
vx=np.zeros((N))
vy=np.zeros((N))
xnd=np.zeros((N))
ynd=np.zeros((N))


##############################################################
## make an array of times to use
t=np.linspace(0,tf,num=N)



##############################################################
# now perform an Euler's Method Calculation
# now recalling that vx(i) already has a cos(theta) in it,
# we can use this to calculate the x part of the resistive
# force and likewise use vy(i) in calculating the y part of
# the resistive force. No explicit calculation of theta is
# necessary this way, and we save lots of computation time.
y[0]=y0        # initial y positoin
vy[0]=v0
for i in range (0,N-1):
    fx=vx[i]
    if y[i]>=600000 :
       gy = -G*m*M/y[i]**2
    elif y[i]<-600000 :
       gy = G*m*M/y[i]**2
       print("less than zero")
    else:
        gy=0
    fy=vy[i]
    y[i+1]=y[i]+deltat*fy
    vy[i+1]=vy[i]+deltat*gy
    print(y[i], vy[i],gy)
plt.plot(y)

