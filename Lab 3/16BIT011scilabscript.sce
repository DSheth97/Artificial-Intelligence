//creating the function of rosenbrock function
function y= f(x)
    y=(100*((x(2)-(x(1)^2)))^2)+((1-x(1))^2); //eq of rosenbrock function
endfunction
//y=(100*((x2-(x1^2)))^2)+((1-x1)^2);
function a=g(x1,y1)
    a=f([x1 y1]);
endfunction
x1=linspace(-2,15,200);
x2=linspace(-2,15,200);
//feval(x,y,f)returns the m×n matrix whose ij element is f(xi,yj)which will be transposed by using the single quote symbol “'“
z= feval(x1,x2,g)';
clf;
//to plot a surface 'surf' is used
surf(x1,x2,z);
//evaluating the function at given points
xa=[-1.2,1];
xb=[1,1];
//passing values in function
f0=f(xa);
f1=f(xb);
disp("At x0"+string(f0));
disp("At xs"+string(f1));
x=[-1.2,1];
//f0=f(xm,xn);
//disp("At xs"+string(f0));
//generating derivative and hessian using numderivative
[J,H] = numderivative(f, x);
disp(J);
disp(H);
