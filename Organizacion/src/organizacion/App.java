
package organizacion;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        int opc, elem, posicion, elemento = 0;
        Empleado E= null;

	do {
            opc = Menu();
		switch(opc) {
                    case 0: 
                        System.out.println("Hasta pronto usuario");
                    break;
		    case 1: 
                        E=IngresaDatos();
		    break;
		    case 2: 
                        ImprimeEmpleado(E);
		    break;
		    default:
		    System.out.println(":::Opcion incorrecta, vuelva a intentar\n\n");
		    break;
                }
        } while(opc!=0);
		
    }
    public static int Menu(){
        int opcion = 0;
        do {
            System.out.println("---------- Registro de empleados -------------\n");
	    System.out.println("Elija una de las siguientes opciones: \n");
            System.out.println("\b 1) Insertar empleado");
	    System.out.println("\b 2) imprime empleado");
	    System.out.println("\b 0) Salir\n");
	    System.out.print("::: ");
	    Scanner scan = new Scanner(System.in);
	    opcion = scan.nextInt();        
        } while (opcion < 0 && opcion > 2);
        return opcion;
    } 
    public static Empleado IngresaDatos() {
        Scanner scan = new Scanner(System.in);
	String auxNombreCompleto;
        int auxPuesto;
	char auxTurno;
        float auxSalario;
	System.out.print("ingrese el nombre: ");
	auxNombreCompleto = scan.nextLine();
	System.out.println(MenuPuesto());
	auxPuesto = scan.nextInt();
	System.out.print("ingrese el turno que ocupa:\n");
	System.out.println("\b M) M: Matutino");
        System.out.println("\b V) V: Vespertino");
        System.out.println("\b N) N: Nocturno\n");
        System.out.print("::: ");
        auxTurno = scan.next().charAt(0);
	System.out.print("ingrese el salario que gana: ");
	auxSalario = scan.nextFloat();
	Empleado E = new Empleado (auxNombreCompleto, auxPuesto, auxTurno, auxSalario);
         return E;
    }
    public static String MenuPuesto() {
         System.out.println("ingrese el puesto que ocupa: \n");
         System.out.println("\b 1) Intendente");
         System.out.println("\b 2) Subdireccion de area");
         System.out.println("\b 3) Gerente");
         System.out.println("\b 4) Cordinador");
         System.out.println("::: ");
         
         return " ";
    }
    public static void ImprimeEmpleado(Empleado em ) {
        System.out.println("Nombre: " + em.getNombre());
        System.out.println("Numero de empleado: " + em.getNumeroEmpleado());
        System.out.println("Puesto: " +  em.getPuesto());
        System.out.println("Turno: " + em.getTurno());
        System.out.println("Salario: " + em.getSalario());

        try
        {    
            String filePath = "C:\\Users\\DELL\\Pictures\\inf.txt";
            FileWriter fw = new FileWriter(filePath, true); 
            try (BufferedWriter bw = new BufferedWriter(fw)) {
                
                bw.write("nombre:"+em.getNombre()+"   Numero: "+em.getNumeroEmpleado()+"   Puesto: "+em.getPuesto()+
                        "   Salario: "+em.getSalario()+"   Turno: "+em.getTurno());
            }
        }
        catch(IOException e)
        {
            System.out.println(e);
        } 
        
       
    }

}


