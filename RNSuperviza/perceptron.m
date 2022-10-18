clear all; clc;

disp('Entrenamiento de neurona Perceptron')

disp('CASO PRUEBA')


disp('DATOS DE ENTRADA')
p1=[2,1]'; t1=1; w=[-0.7 0.2];
p2=[0,-1]'; t2=1; b=0.5;
p3=[-2,1]'; t3=-1;
p4=[0,2]'; t4=-1;

P=[p1 p2 p3 p4]
T=[t1 t2 t3 t4]

cont=0;
% while cont==4
for i=1:4
a1=hardlims((w*P(:,i))+b)

% if a1<0
%     a1=-1;
% else
%     a1=1;
% end
e=T(i)-a1


if e==0
    w1=w
else 
    w1=w+e*P(:,i)'
    b1=b+e
end
    cont=cont+1
    x=3.3
    y=1.8
end


% end

plot(P(1,1),P(2,1),'*r')
grid on
% axis([-2.5 2.5 -1.5 2.5])
xlabel('P1')
ylabel('P2')
hold on
plot(P(1,2),P(2,2),'*r')
plot(P(1,3),P(2,3),'ob')
plot(P(1,4),P(2,4),'ob')
plot(x,0,'+g')
plot(0,y,'+g')

