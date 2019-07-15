x=[-100:100];
y=1./(1+exp(-x)); // Evaluating function 
disp(string(x)+" "+string(y));
plot(x,y); // Plotting x vs y
