%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Euler for a mass-spring system                             %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Lab 8 
% PH150
% Brother Lines
% 2010 February 22
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This code will perform two calculations
%  1) It will calculate the exact solution for a mass-sring
%     system using the theoretical result (damping, no forcing)
%  2) It will calculate the result using Euler's method  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Initial conditions and physial setup constants
b=0.05;  %damping coefficient
m=0.2;   % mass in kilograms
k=0.500; % spring constant in N/m
A=15;    % amplitude in meters
phi=0;   % phase2
v0=0.0;  %initial velocity
x0=A;    %initial poistion

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Set up the time steps and number of calcualtions
deltat=0.01; %Time steps of 0.01 seconds
ti=0;        %starting at ti=0
tf=20;       %final time
N=(tf-ti)/deltat; % calcualte how many time steps are in 20 seconds

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Preliminary calculations
pi=acos(-1.0);   %calculate pi to machine percision
omega=sqrt(k/m); %calculate the angular frequency, omega

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Now lets perform do the claculation for the exact solution
% first zero arrays
t=zeros(1,N+1);
x=zeros(1,N+1);
y=zeros(1,N+1);
z=zeros(1,N+1);

% calcuate the postion of the mass using our known solution
t=(0:deltat:tf); % fill in the array of time values
z=A.*exp(-b.*t./(2.*m)).*cos(omega.*t+phi); %exact solution

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%now perform an Euler's Method Calculation
y(1)=v0;  % initial velocity goes in y(1)
x(1)=x0;  % initial position goes in x(1)
for i=1:N
    f=y(i);                         % our f(x,v,t)
    g=-(k/m)*x(i)-(b/m)*y(i);       % our g(x,v,t)
    x(i+1)=x(i)+deltat*f;           % general x step equation
    y(i+1)=y(i)+deltat*g;           % general y (v for us) step
end;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% plot the resuts
plot(t,z,t,x,'+');



