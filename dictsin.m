clc
clear all
close all
dict=container.Maps({'s1','s2','s3','s4','s5'},{[1,5],[2,5],[5,10],[3,7],[10,12]}
disp(choose:{'s1':[1,5],'s2':[2,5],'s3':[5,10],'s4':[3,7],'s5':[10,12]})
if iskey(dict,k)
    x=dict(k)(1)*sin()2*pi*dict(k)(2)*t
    plot(t,x)
    xlabel('time')
    ylabel('amplitued')
    gridon;
    legend('singnal')
