%Neurona backpropagation tipo tansig y pureline
clear all;clc;
disp('Backpropagation');
disp('Valores iniciales');
%Declaracion de patrones
P=[-2 -0.5 -1.5 -1 1 1.5 0.5 2]
t=[0 -0.7 -0.7 -1 1 0.7 0.7 0]
%calculo de los estados finales
% for i=1:8
% t(i) = sin(pi/4*P(i));
% end
% t
%valores iniciales
sigma=0.5;
Ws=[0.1 0.3];
Bs=0.8; 
Wo=[-0.2 0.5];   
Bo=[0.7 -0.2];
fprintf('sigma = %f\n',sigma);
fprintf('Ws = %f %f\n',Ws);  
fprintf('Bs = %f\n',Bs);
fprintf('Wo = %f %f\n',Wo);
fprintf('Bo = %f %f\n\n',Bo);
% procedimiento
E=0; 
ite=1; 
aux=0; 
v=0;
% proceso
while (aux<=8) || (v<=8) %  condiciones por que son 8 patrones presentados
    disp('________________________________________________');
    fprintf('Iteración %d\n',ite);
    for i=1:8
    fprintf('Patrón %d\n',i);
    disp('Capa Oculta')
  % Capa oculta
    Ao=(Wo*P(i))+Bo; 
    Ao=[(exp(Ao(1))-exp(-Ao(1)))/(exp(Ao(1))+exp(-Ao(1))) (exp(Ao(2))-exp(-Ao(2)))/(exp(Ao(2))+exp(-Ao(2)))];
    fprintf('a(%d)n2= [%f %f]\n',i,Ao); 
    disp('Capa Salida')
  %  Capa de salida 
    As=(Ws*Ao')+Bs;
    fprintf('as(%d)= %f\n',i,As);
  %calculo del error
    e=t(i)-As;
    fprintf('e(%d) = %f\n',i,e);
%   if(e<=-0.100000 || e>=0.100000) 
  if (-0.010000<= e >= 0.010000) 
  %Sensitividades
    %pureline
    fs = 1;
    fprintf('f(pureline) = %f\n',fs);
    %tansig
    fo=[(1-Ao(1)^2)  (1-Ao(2)^2)];
    fprintf('f(tansig) = %f %f\n',fo);
  %Sensitividades
    Ss=-2*fs*e;
    fprintf('Ss = %f\n',Ss);
    So=[fo(1)*Ws(1)*Ss  fo(2)*Ws(2)*Ss];
    fprintf('So(n1) = %f %f\n',So);
  %Ajuste pesos y ganancias
    Ws=Ws-sigma*Ss*Ao;
    fprintf('Ws = %f %f\n',Ws);  
    Bs=Bs-sigma*Ss;
    fprintf('Bs = %f\n',Bs);
    Wo=Wo-sigma*So*P(i);
    fprintf('Wo = %f %f\n',Wo);
    Bo=Bo-sigma*So;
    fprintf('Bo(n2)= %f %f\n',Bo);
    v=0;
    disp('------------------');
  else 
    v=v+1;%condicion para cuanando error es pequeño
    disp('------------------');
  end
  if i==8 
    ite=ite+1; % numero de iteraciones para cada patron 
%     v=0;
    c = abs(abs(E)- abs(e)); % diferencia entre errores
    if c <= .02 % rango para de tolerancia para el error
      aux = aux+1;
    else aux = 0;
      E=e; 
    end
  end
  end
end
