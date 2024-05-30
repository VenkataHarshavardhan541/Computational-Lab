clc
clear all
close all
duration=1;
t=linspace(0,duration,duration*100);
freq=10;
sin1=sin(2*pi*freq1*t);
freq2=15;
sin2=sin(2*pi*freq2*t);
x=sin1+sin2;
lw=input('Ente the length of the winow');
y=zeros(size(t)):
  for n=1:length(t)
    y(n)=sum(x(max(1,n-(w+1):n)));
  end
 plot(t,y,'displayname','y[n]')
 hold on
 plot(t,sin1)
 holdoff;


