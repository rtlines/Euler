#variagles
vi=30.0
xi=0.0
yi=8.0
theta=45
pi=3.14159
theta=theta*pi/180.0
g=9.8
ax=0
ay=-g
t=0.0
deltat=0.1
xt=xi
yt=yi
vxt=vi*cos(theta)
vyt=vi*sin(theta)

#lists
time=[0.0]
yk=[0.0]
xk=[0.0]
xe=[0.0]
ye=[0.0]
vxe=[0.0]
vye=[0.0]

xe.append(xt)
ye.append(yt)
vxe.append(vxt)
vye.append(vyt)

#functions
def kinematic_step(xi, yi, theta, t, ay):
    yf=yi+vi*sin(theta)*t+0.5*ay*t^2
    xf=xi+vi*cos(theta)*t
    return xf, yf

def euler_step(x,y,vx,vy,ax, ay, dt):
    x2=x + dt*vx;
    y2=y + dt*vy;
    vx2=vx + dt*ax;
    vy2=vy + dt*ay;
    return x2,y2,vx2,vy2


# now calculate
while t<9.0:
    time.append(t)
    xkt,ykt = kinematic_step(xi, yi, theta, t, ay)
    xk.append(xkt)
    yk.append(ykt)
    xt,yt,vxt,vyt = euler_step(xt,yt,vxt,vyt,ax, ay, deltat)
    xe.append(xt)
    ye.append(yt)
    vxe.append(vxt)
    vye.append(vyt)
    if ykt<0.0:
        break
    t=t+deltat
points = zip(xk,yk)  # combine x and y in a way that list_plot can understand
plotk=list_plot(points, plotjoined = True)  # graph the points
points = zip(xe,ye)  # combine x and y in a way that list_plot can understand
plote=list_plot(points, plotjoined = True)  # graph the points
plotk+plote