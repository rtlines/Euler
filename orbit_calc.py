##############################################################
# Euler code to calculate a satellite orbit                  #
##############################################################
# Todd Lines
# 2022 04 19
##############################################################
# This code will calculate the path of an orbit given a 
#  specific velocity of the object and it's direction. 
#  It would probably be be better to have the whole calcuation 
#  go in reverse. But I didn't do that on purpose since we are
#  verifying that an elipse comes from a distance squared law
#  with this code.
##############################################################
# Load Libraries
import numpy as np                 # Numerical calculation library
import matplotlib.pyplot as plt    # Data plotting libary

##############################################################
# Initial conditions and physial setup constants
R=6371E3       # Radius of Earth in m
M=5.9E24       # Mass of plannet in Kg
m=0.020        # mass of our sattelite in kilograms
G=5.11E-11     # N*m**2/kg**2 Gravitational Constant
x0=2*R         # Initial x position in m (The Earth is at x = 0)
y0=0.5*R       # Initial y position in m (The Earth is at y = 0)
v0=6000.0       # Initial satellite velocity in m/s
thetadeg=100   # Satellite launch angle in degrees
             
##############################################################
## Set up the time steps and number of calcualtions
deltat=1.0        # Time steps of 0.01 seconds
ti=0              # starting at t=0
tf=300000         # final time in seconds
N=int((tf-ti)/deltat)  # calcualte how many time steps are in tf-ti seconds

##############################################################
# Preliminary calculations
pi=np.arccos(-1.0)         # calculate pi to machine percision
theta=thetadeg*pi/180      # calcualte theta in radians
vx1=v0*np.cos(theta)       # calculte the x component of the initial velocity
vy1=v0*np.sin(theta)       # calculte the y component of the initial velocity

##############################################################
# define and zero arrays
t=np.zeros((N))
x=np.zeros((N))
y=np.zeros((N))
vx=np.zeros((N))
vy=np.zeros((N))


##############################################################
## make an array of times to use
t=np.linspace(0,tf,num=N);
##############################################################
# Draw The Earth
r=R                               # distance from center in m
ThetaE0=0.00                      # initial angle in degrees
delta_ThetaE=5                    # change in angle in degrees
# calculate the number of points to use in our Earth drawing
Ne= int(360/delta_ThetaE)+1       # number of points
ye=np.zeros((Ne))
xe=np.zeros((Ne))
# Draw Circle to represent the Earth
ye[0]=0        # initial y positoin
xe[0]=r
thetaE=ThetaE0
for i in range (0,Ne):
    thetaE=thetaE+delta_ThetaE
    xe[i]=r*np.cos(thetaE*pi/180)
    ye[i]=r*np.sin(thetaE*pi/180)
plt.plot(xe, ye)

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

# Put the starting point in the arrays
x[0]=x0                        # initial x position
y[0]=y0                        # initial y positoin
vx[0]=vx1                      # initial x velocity
vy[0]=vy1                      # initial y velocity, what we give it

# Now calculate all the other points of the satellite path
print('working')
for i in range (0,N-1):
    r=np.sqrt(x[i]**2+y[i]**2)
    if x[i] != 0:
        theta=np.arctan(y[i]/x[i])
    else:
        theta=pi/2
        
    if y[i]>0 and x[i]<0:
       theta=pi+theta
    if y[i]<0 and x[i]<=0:
       theta=theta+pi
    if y[i]<0 and x[i]>0:
       theta=2*pi+theta
    if r<R:
       print("hit surface")
       break   #hit surface

    # Calculate the velocity and acceleration terms   
    fx=vx[i]
    gx=-np.cos(theta) * G*M/r**2
    fy=vy[i]
    gy=-np.sin(theta) * G*M/r**2
    
    # Take an Euler step
    x[i+1]=x[i]+deltat*fx
    y[i+1]=y[i]+deltat*fy
    vx[i+1]=vx[i]+deltat*gx
    vy[i+1]=vy[i]+deltat*gy   
print('done')

# Now plot our satellite path 
plt.plot(x[:i],y[:i])
plt.show()

# And that is the end of the program

###############################################################
##now perform an RK2 Method Calculation
# Put the starting point in the arrays
x[0]=x0                        # initial x position
y[0]=y0                        # initial y positoin
vx[0]=vx1                      # initial x velocity
vy[0]=vy1                      # initial y velocity, what we give it

for i in range (0,N-1):
    # Check to see if we hit the Earth
    r=np.sqrt(x[i]**2+y[i]**2)
    if x[i] != 0:
        theta=np.arctan(y[i]/x[i])
    else:
        theta=pi/2
        
    if y[i]>0 and x[i]<0:
       theta=pi+theta
    if y[i]<0 and x[i]<=0:
       theta=theta+pi
    if y[i]<0 and x[i]>0:
       theta=2*pi+theta
    if r<R:
       print("hit surface")
       break   #hit surface

    #calculate the velocity and acceleration terms
    fx=vx[i]
    gx=-np.cos(theta) * G*M/r**2
    fy=vy[i]
    gy=-np.sin(theta) * G*M/r**2
   
    #Start the RK2 step by calculating k values
    kx1=deltat*fx
    ky1=deltat*fy
    kvx1=deltat*gx
    kvy1=deltat*gy
    #now the RK step, 
    #thing as above to find the x abd y components of the velocity.
    
    fx2=vx[i]+kvx1/2
    gx2=-Rx/m
    fy2=vy[i]+kvy1/2
    gy2=-g-Ry/m
    #finally take the RK step.
    x[i+1]=x[i]+deltat*fx2
    y[i+1]=y[i]+deltat*fy2
    vx[i+1]=vx[i]+deltat*gx2
    vy[i+1]=vy[i]+deltat*gy2+Rexp*y[i]     # once again I have added in the 
                                            # expansion term
    #if y(i+1)<=0.0 , break, end
    
xRK=np.copy(x)
yRK=np.copy(y)

plt.plot(xnd,ynd, label='kinematic')
plt.plot(xEu,yEu, label='expansion')
plt.plot(xRK,yRK,label='RK')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
leg=plt.legend();
