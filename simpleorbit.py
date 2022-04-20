##############################################################
# second order Runga Cutta for a projectile with expansion   #
##############################################################
# Todd Lines
# 2020 08 14
##############################################################
# This code will perform two functions
#  1) It will calculate the exact solution for a projectile
#     system using the theoretical result with no drag
#  2) It will calculate the result using Euler's method with 
#     drag (because I used an old code as a base) and with a 
#     ondimensional space expansion in the y-direction
##############################################################
# Load Libraries
import numpy as np
#import matplotlib
#matplotlib.use('tkagg')
import matplotlib.pyplot as plt

##############################################################
# Initial conditions and physial setup constants
R=6371E3      # radius of Earth in m
M=5.9E24       # Mass of plannet in Kg
m=0.020       # mass of sattelite in kilograms
G=5.11E-11    # N*m**2/kg**2
x0=2*R          # initial x position in m
y0=0.5*R       # initial y position in m
v0=6000.0         # initial velocity in m/s
thetadeg=100   # launch angle in degrees
Rexp=0.007      # expansion coefficient in m/s/m This is really 
              # a type of Hubble constant, but I am not using
              # the right value yet.
##############################################################
## Set up the time steps and number of calcualtions
deltat=1.0        # Time steps of 0.01 seconds
ti=0              # starting at t=0
tf=400000          # final time
N=int((tf-ti)/deltat)  # calcualte how many time steps are in 20 seconds
##############################################################
# Preliminary calculations
pi=np.arccos(-1.0)           # calculate pi to machine percision
theta=thetadeg*pi/180   # calcualte theta in radians
vx1=v0*np.cos(theta)       # calculte the x component of the initial velocity
vy1=v0*np.sin(theta)       # calculte the y component of the initial velocity

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
xE=np.zeros((N))
yE=np.zeros((N))


##############################################################
## make an array of times to use
t=np.linspace(0,tf,num=N);
##############################################################
# Draw The Earth
r=R      # distance from center in m
ThetaE0=0.00      # initial angle in degrees
delta_ThetaE=5  # change in angle in degrees
Ne= int(360/delta_ThetaE)+1       # number of points
ye=np.zeros((Ne))
xe=np.zeros((Ne))
##############################################################
# Draw Circle
ye[0]=0        # initial y positoin
xe[0]=r
thetaE=ThetaE0
for i in range (0,Ne):
    thetaE=thetaE+delta_ThetaE
    xe[i]=r*np.cos(thetaE*pi/180)
    ye[i]=r*np.sin(thetaE*pi/180)

##############################################################
# now perform an Euler's Method Calculation
# now recalling that vx(i) already has a cos(theta) in it,
# we can use this to calculate the x part of the resistive
# force and likewise use vy(i) in calculating the y part of
# the resistive force. No explicit calculation of theta is
# necessary this way, and we save lots of computation time.
x=np.zeros((N))
y=np.zeros((N))
vx=np.zeros((N))
vy=np.zeros((N))
x[0]=x0                        # initial x position
y[0]=y0                        # initial y positoin
vx[0]=vx1                      # initial x velocity
vy[0]=vy1            # initial y velocity, what we give it

                               # plus the expansion sudo velocity
print('working')
for i in range (0,N-1):
    r=np.sqrt(x[i]**2+y[i]**2)
  
    if r<R:
       print("hit surface")
       break   #hit surface
    
    fx=vx[i]
    gx=-G*M*x[i]/r**3
    fy=vy[i]
    gy=-G*M*y[i]/r**3
    
    
    v=np.sqrt(vx[i]**2+vy[i]**2)
    
    if (t[i]>50000) and (t[i]<50100):
        tx=5.0*vx[i]/v
        ty=5.0*vy[i]/v
        ax=gx+tx
        ay=gy+ty
    else:
        ax=gx
        ay=gy
        
    x[i+1]=x[i]+deltat*fx
    y[i+1]=y[i]+deltat*fy
    vx[i+1]=vx[i]+deltat*ax
    vy[i+1]=vy[i]+deltat*ay    
                                           
    #print(i, theta, ax, ay, gx, gy)

print('done')

#plt.axes('square')

plt.plot(xe,ye)

plt.plot(x,y)

plt.show()




