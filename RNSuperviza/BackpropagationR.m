clear all; clc;

disp(' ')
disp('            Practica Backpropagation')
disp(' ')
disp('***********************************')
disp(' ')
disp('Entrada de datos')
disp(' ')

p = [-2 -1.2 -0.4 0.4 1.2 2];
t = [-1 -0.809 -0.309 0.309 0.809 1];

disp('***********************************')
disp(' ')
disp('Entrada de pesos y ganancia')
disp(' ')

alfa = 0.1;
ws = [0.1 0.3];     
bs = 0.8; 

%neurona 1
wn1 = [-0.2 0.5];
bn1 = [0.7 -0.2];

%neurons 2
wn2 = [-0.2 0.5];
bn2 = [0.7 -0.2];

arregloE = 0;
ceros = 0;
iteracion = 0;
errorAnt = 0;
Paro = .01;
restaError = 1;

doc = fopen('Backpropagation.doc','w');
fprintf( doc,'Practica  "Neurona Backpropagation"\n');

while ceros < size(p,2) | restaError < Paro
    
    iteracion = iteracion + 1
    fprintf( doc,'\nIteracion %i\n',iteracion);
    
    for i = 1 : size(p,2)
        
        % Neurona 1
        a = wn1 * p (i) + bn1;
        aN1 = [(exp(a(1)) - exp(-a(1))) / (exp(a(1)) + exp(-a(1))) (exp(a(2)) - exp(-a(2))) / (exp(a(2)) + exp(-a(2)))]
        
        % Neurona 2
        a = (wn2 * p(i) + bn2);
        aN2 = [1/(1 + exp(-a(1))) 1/(1+exp(-a(2)))]
        
        % Neurona de salida
        as = (ws * (aN1' + aN2') + bs);
        
        % error
        e = t(i) - as
        arregloE(end + 1) = e
        
        %%%%  derivadas
        
        % purelin
        fs = 1;
        
        %tansig
        fn1 = [(1 - aN1(1)^2)  (1 - aN1(2)^2)]
        fn2 = [(aN2(1) * (1 - aN2(1)))  (aN2(2) * ( 1 - aN2(2)))]
                
        %Sensitividad
        ss = -2 * fs * e
        sN1 = [fn1(1) * ws(1) * ss  fn1(2) * ws(2) * ss]
        sN2 = [fn2(1) * ws(1) * ss  fn2(2) * ws(2) * ss]
        
        %Ajustes
        ws = ws - alfa * (ss * aN1 + ss * aN2)
        bs = bs - alfa * ss
                
        wn1 = wn1 - alfa * sN1 * p(i)
        bn1 = bn1 - alfa * sN1
        
        wn2 = wn2 - alfa * sN2 * p(i)
        bn2 = bn2 - alfa * sN2
        
        fprintf( doc,'\nPatron de entrada %i\n',i);
        fprintf( doc,'an1 = [ %10.4f  %10.4f ]\n',aN1);
        fprintf( doc,'an2 = [ %10.4f  %10.4f ]\n',aN2);
        fprintf( doc,'as = [ %10.4f  %10.4f ]\n',as);
        fprintf( doc,'e = [%10.4f]\n',e);
        fprintf( doc,'f(ns) = %10.4f\n',fs);
        fprintf( doc,'f(n1) = %10.4f\n',fn1);
        fprintf( doc,'f(n2) = %10.4f\n',fn2);
        fprintf( doc,'Ss = %10.4f\n',ss);
        fprintf( doc,'S(n1) = [ %10.4f  %10.4f ]\n',sN1);
        fprintf( doc,'S(n2) = [ %10.4f  %f ]\n',sN2);
        fprintf( doc,'Ws = [ %10.4f  %10.4f ]\n',ws);
        fprintf( doc,'Bs = %10.4f\n',bs);
        fprintf( doc,'Wn1 = [ %10.4f  %10.4f ]\n',wn1);
        fprintf( doc,'bn1 = [ %10.4f  %10.4f ]\n',bn2);
        fprintf( doc,'Wn1 = [ %10.4f  %10.4f ]\n',wn2);
        fprintf( doc,'bn1 = [ %10.4f  %10.4f ]\n',bn2);
        
    end
    
    if iteracion == 1
        errorAnt = arregloE(end)
        
    else
        restaError = arregloE(end) - errorAnt;
        restaError = abs(restaError)
        errorAnt = arregloE(end);
    end
    
    ceros = sum(arregloE == 0);
    
    x1 = -bs / ws(1)
    y1 = -bs / ws(2)
    
    plot(p(1), t(1), 'or');
    hold on;
    grid on;
    plot(p(2), t(2), 'or');
    plot(p(3), t(3), 'or');
    plot(p(4), t(4), 'ob');
    plot(p(5), t(5), 'ob');
    plot(p(6), t(6), 'ob');
    plot([x1,0],[0,y1])
    axis([-4 4 -4 4])
        
    x = linspace(-3,3,50); 
    y = sin(x * pi / 4);
    plot(x,y);
    
    fprintf( doc,'\nRecta solucion %i\n',iteracion);
    fprintf( doc,'coordenada x = %f\n',x1);
    fprintf( doc,'coordenada y = %f\n',y1);
    
end
fclose(doc);