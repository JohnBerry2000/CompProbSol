from numpy import array,arange
from pylab import plot,xlabel,ylabel,show,figure,legend
# This file contains two functions. f(r,t) defines the lokta-volterra model and predatorprey solves the model using a 4th order runge-kutta method

#These parameters produce a periodic rabbit/fox populations
alpha = 2
beta = 0.01
gamma = 1
delta = 0.01

def f(r,t):
    x = r[0]
    y = r[1]
    fx = alpha*x - beta*x*y
    fy = delta*x*y - gamma*y
    return array([fx,fy],float)

def predatorprey(r0,f0,tf=10,N=1000):
    # specify initial time and step size
    t0 = 0.0
    h = (tf-t0)/N
    tpoints = arange(t0,tf,h)
    # create solution arrays
    rabbits = []
    foxes = []

    r = array([r0,f0],float)
    for t in tpoints:
        rabbits.append(r[0])
        foxes.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
    figure(1)
    plot(tpoints,rabbits,'b-',tpoints,foxes,'g-')
    plot(tpoints,foxes)
    xlabel("t")
    ylabel("populations")
    legend(("rabbits","foxes"))
    figure(2)
    plot(rabbits,foxes)
    xlabel("rabbits")
    ylabel("foxes")
    show()
    return tpoints, rabbits, foxes