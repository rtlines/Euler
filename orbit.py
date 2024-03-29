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
v0=6500.0         # initial velocity in m/s
thetadeg=100   # launch angle in degrees
Rexp=0.007      # expansion coefficient in m/s/m This is really 
              # a type of Hubble constant, but I am not using
              # the right value yet.
##############################################################
## Set up the time steps and number of calcualtions
deltat=1.0        # Time steps of 0.01 seconds
ti=0              # starting at t=0
tf=300000         # final time
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
    
    fx=vx[i]
    gx=-np.cos(theta) * G*M/r**2
    
    
    fy=vy[i]
    gy=-np.sin(theta) * G*M/r**2
    
    x[i+1]=x[i]+deltat*fx
    y[i+1]=y[i]+deltat*fy
    vx[i+1]=vx[i]+deltat*gx
    vy[i+1]=vy[i]+deltat*gy    # once again I have added in the 
                                            # expansion term
    #print(i, theta, x[i],y[i],vx[i],vy[i], gx, gy)

print('done')

#plt.axes('square')
#plt.plot(xe,ye)
plt.plot(x,y)

plt.show()

#xEu=np.copy(x)
#yEu=np.copy(y)
#plt.plot(xEu,yEu, label='expansion2')


###############################################################
##now perform an RK2 Method Calculation
#x[0]=x0                    # initial x position
#y[0]=y0                    # initial y positoin
#vx[0]=vx1                  # inintal x velocity
#vy[0]=vy1+Rexp*y[0]        # initial y velocity, what we give it
#                           # plus the expansion sudo velocity
#for i in range (0,N-1):
#    v=np.sqrt(vx[i]**2+vy[i]**2)
#    # first the Euler step, This is tricky because I want just the x
#    # component and the y component of the drag force, but the drag force
#    # depends on v^2. Remembering that vx=v*cos(theta), we can then multiply
#    # the speed, v, by vx to get v^2*cos(theta). This way we don't have to
#    # calculate theta explicitly
#    Rx=0.5*D*rho*pi*r*r*v*vx[i]
#    Ry=0.5*D*rho*pi*r*r*v*vy[i]
#    fx=vx[i]
#    gx=-Rx/m
#    fy=vy[i]
#    gy=-g-Ry/m
#    kx1=deltat*fx
#    ky1=deltat*fy
#    kvx1=deltat*gx
#    kvy1=deltat*gy
#    #now the RK step, What to do with the v^2? I think we can do the same
#    #thing as above to find the x abd y components of the velocity.
#    v=np.sqrt((vx[i]+kvx1/2)**2+(vy[i]+kvy1/2)**2)
#    Rx2=0.5*D*rho*pi*r*r*v*(vx[i]+kvx1/2)
#    Ry2=0.5*D*rho*pi*r*r*v*(vy[i]+kvy1/2)
#    fx2=vx[i]+kvx1/2
#    gx2=-Rx/m
#    fy2=vy[i]+kvy1/2
#    gy2=-g-Ry/m
#    #finally take the RK step.
#    x[i+1]=x[i]+deltat*fx2
#    y[i+1]=y[i]+deltat*fy2
#    vx[i+1]=vx[i]+deltat*gx2
#    vy[i+1]=vy[i]+deltat*gy2+Rexp*y[i]     # once again I have added in the 
#                                            # expansion term
#    #if y(i+1)<=0.0 , break, end
#    
#xRK=np.copy(x)
#yRK=np.copy(y)
#
#plt.plot(xnd,ynd, label='kinematic')
#plt.plot(xEu,yEu, label='expansion')
#plt.plot(xRK,yRK,label='RK')
#plt.xlabel('x [m]')
#plt.ylabel('y [m]')
#leg=plt.legend();
#plt.show()
