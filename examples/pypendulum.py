# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:27:58 2018

@author: Tom K
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as pyl
g=9.81

# function that returns dy/dt
def pendulum(l=0.5,theta0=np.pi/2,thetad0=0):
    # time points you control the steps in this case 
    t=np.linspace(0,20,1000)
    # initial conditions together
    initial = [theta0,thetad0]
    # pendulum length will be a extra argument
    # extra argument(s) must be in a tuple
    l = (l,)
    #solve ode
    sol = odeint(model, initial, t,l)

    ind = []
    for k in range(0,len(t)-1):
        if sol[k,0]*sol[k+1,0]<0:
            ind.append(k)
    per = []    
    for k in range(1,len(ind)):
        per.append(2*(t[ind[k]]-t[ind[k-1]]))
    
        period = np.average(per)
    
    pyl.plot(t,sol[:,1],'k.')
    pyl.plot(t,sol[:,0],'b-')
    pyl.xlabel('t')
    pyl.ylabel('theta')
    pyl.show()
    return period

def model(r,t,l):
    theta = r[0]
    omega = r[1]
    dtheta = omega
    domega = -g/l*np.sin(theta)
    return np.array([dtheta, domega])