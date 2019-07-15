function [B]=Map_Matrix(A);
    B=[0,0,0;0,0,0;0,0,0];
    u=unique(A);    //calculating unique integers
    for i=1:9
        m=min(A);       //getting maximum
        in=find(A==m);
        B(in)=i;
        A(in)=9999;     
    end
    disp(B);
endfunction

disp(Map_Matrix([7,13,25;123,233,254;169,207,50]));
A = imread('LenaGrey.jpeg');      //reading the image using inbuilt imread function
disp(A);                        //displays the pixels in the form of matrix having 
int v                                   // values
imshow(A);                      //displayign the image
map = Map_Matrix(A);            //mapping the image to obtain the result
disp(map);
imshow(int8(map));                  //int8 to convert to 8 bit signed integer
