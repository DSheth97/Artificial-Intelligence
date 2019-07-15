clear;
x=1+int(rand()*50); //Generating random number
//c=1;
for i=1:10
    //disp(x);
    y=int(input("Guess the number"));
    A(i)=i;         //Storing attempt
    B(i)=y;         //Storing guess
    //c=c+1;
    if x==y then
        disp("Correct guess");      
        break;
    elseif x>y then
        disp("Too low guess");
    else disp("Too high guess");
    end
end
plot(A,B); // Plotting attempt vs guess
