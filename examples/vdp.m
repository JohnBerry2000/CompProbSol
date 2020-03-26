function sol = vdp(mu,y0)
tspan = [0,10];
opts = odeset('refine',6);
[t,w] = ode45(@func,tspan,y0,opts,mu);

sol = [t,w];


end



function dsol = func(t,y,mu)
dsol = [ y(2)   , mu*(1-y(1)^2)*y(2)-y(1)  ]; 

end
