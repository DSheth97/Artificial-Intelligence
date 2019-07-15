function yprim=f(t,y)     //declaring the ode as given in a function 
yprim(1)=y(2);
yprim(2)=-4*y(1) ;
endfunction
t0=0; tmax=5;           //defining initial conditions
t=t0:0.05:tmax;         //getting t from initial conditions with interval of 0.05
y0=3; yprim0=0;
c10=1; c1prim0=1;       //Case A
c20=4; c2prim0=1;       //Case B
y=ode([y0;yprim0],t0,t,f);
c1=ode([c10;c1prim0],t0,t,f);       //executing ODE using inbuilt ode function
c2=ode([c20;c2prim0],t0,t,f);
clf;
plot(t,y(1,:),"b");            //plotting the curve
plot(t,c1(1,:),"r");
plot(t,c2(1,:),"g");
