clc;
clear;
ac=0;
m=csvRead('C:\Users\alay.sict16\Desktop\AI003\Irisdataset.csv');
disp(m)
train=cat(1,m(1:35,1:4),m(51:85,1:4),m(101:135,1:4));
test=cat(1,m(36:50,1:4),m(86:100,1:4),m(136:150,1:4));
N=[4,16,3];
for i=1:105
    if (i<=35) then
        t(i,1:3)=[1,0,0];
    elseif (i>=71) then
        t(i,1:3)=[0,0,1];
    else
        t(i,1:3)=[0,1,0];
    end   
end
lp=[0.25,0];
W=ann_FF_init(N);
T=400;
train_ann=ann_FF_Std_online(train',t',N,W,lp,T);
test_ann=ann_FF_run(test',N,train_ann);
test_ann=test_ann';
disp(test_ann);
rt=round(test_ann);
disp(rt);
for i=1:45
    if (i<=15) then
        if (rt(i,1:3)==[1,0,0]) then
            ac=ac+1;
        end
    elseif (i>=31) then
        if (rt(i,1:3)==[0,0,1]) then
            ac=ac+1;
        end
    else
        if (rt(i,1:3)==[0,1,0]) then
            ac=ac+1;
        end
    end   
end
disp((ac/45)*100);
