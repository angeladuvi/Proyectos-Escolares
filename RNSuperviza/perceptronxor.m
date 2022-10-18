clear all; clc;
disp('DATOS DE ENTRADA')
p1=[0,0]; t1=0; 
p2=[0,1]; t2=1; 
p3=[1,0]; t3=1;
p4=[1,1]; t4=0;

P=[p1 p2 p3 p4]
T=[t1 t2 t3 t4]

disp('Valores Iniciales')
w=[-0.7 0.2];
b=0.5;
pp = [ p1 t1;
    p2 t2;
    p3 t3; 
    p4 t4];
comp = 1;
wk = w;
bk = b; 
cont = 1;
j = 1;
w = {wk};
b = {bk};
it = 1;
disp('Iteracion 0')
    fprintf('Ganancia: %f\n',bk);
    fprintf('Peso: [%f %f]\n', wk);
    x = -bk / wk(1);
    y = -bk / wk(2);
    fprintf('X(%d)= %f ,Y(%d)=%f\n',i,x,i,y);
while( comp < 4)
    disp('________________________________________________')
    comp = 0;    
    cont = cont + 1;
    fprintf('Iteracion %d\n',it);
    it = it + 1;    
    for i = 1: length(pp) 
        fprintf('Patron %d\n',i);
        %%%%%%%%%%%%%%%%%%%%%%%% ai
        pi = [pp(i,1), pp(i,2)];
        ti = pp(i, 3);
        ai = hardlim(wk * pi' + bk);
        fprintf('a(%d)= %f\n',i,ai);   
        %%%%%%%%%%%%%%%%%%%%%% ei
        ei = ti - ai;
        fprintf('e(%d) = %f\n',i,ei);
        %%%%%%%%%%%%%%%%% ajustar
        if ei == 0
            comp = comp + 1;
        else
            disp('Ajuste:');
            wk = wk + ei*pi;
            fprintf('w(%d) = [%f %f] \n',i,wk);
            bk = bk + ei;
            fprintf('b(%d)= %f\n',i,bk);
            j = j + 1;
            w{j} = wk;
            b{j} = bk;
        end
        
        if j == 1
        end 
        disp('------------------')
    end
    fprintf('Ganancia: %f\n',bk);
    fprintf('Peso: [%f %f]\n',wk);
    x = -bk / wk(1);
    y = -bk / wk(2);
    fprintf('X(%d)= %f ,Y(%d)=%f\n',i,x,i,y);
end
