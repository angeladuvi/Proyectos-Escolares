package lista;
import java.util.Scanner;
import javax.swing.JOptionPane;

public class Lista {

    public static void main(String[] args) {
       /// Thash T = null;
        
        Listas listita = new Listas();
        int opcion = 0, el;
        do {
            try {
                opcion = Integer.parseInt(JOptionPane.showInputDialog(null,
                        "1.Agregar elemento al inicio de la lista\n2.Agregar un elemento al final de la lista"
                        + "\n3.Buscar un elemento de la lista\n4.Eliminar un  elemento a la lista\n5.Imprimir\n6.Salir", "Menu de opciones ", 3));
                switch (opcion) {
                    
                    case 1:///agregar al inicio
                        try {
                            el = Integer.parseInt(JOptionPane.showInputDialog(null,
                                    "Inserte los elementos", "Insertando al inicio", 3));
                           /// agregando al elemento
                            listita.agregarInicio(el);
                        } catch (NumberFormatException n) {
                            JOptionPane.showInputDialog(null, "Error" + n.getMessage());
                        }
                        
                        break;
                    case 2://agregar al final ////2.Agregar un elemento al final de la lista\n"
                        try {
                            el = Integer.parseInt(JOptionPane.showInputDialog(null,
                                    "Inserte los elementos", "Insertando al inicio", 3));
                            //agregando al elemento
                            listita.agregarFinal(el);
                        } catch (NumberFormatException n) {
                            JOptionPane.showInputDialog(null, "Error" + n.getMessage());
                        }
                        break;
                    case 3:///BUSCAR
                        el = Integer.parseInt(JOptionPane.showInputDialog(null,
                                "Ingresa el nodo a buscar: ", " Buscando en la lista", JOptionPane.INFORMATION_MESSAGE));
                        if (listita.Buscar(el) == true) {
                            JOptionPane.showMessageDialog(null, "El elemento: " + el
                                    + " Si esta en la lista", " Nodo no encontrado", JOptionPane.INFORMATION_MESSAGE);
                        } else {
                            JOptionPane.showMessageDialog(null, "El elemento: " + el
                                    + " No  esta en la lista", " Nodo no encontrado", JOptionPane.INFORMATION_MESSAGE);
                        }
                        break;
                    case 4:///ELIMINAR lista ligada

                        el = Integer.parseInt(JOptionPane.showInputDialog(null,
                                "Ingresa el nodo a eliminar", "Nodo eliminado", JOptionPane.INFORMATION_MESSAGE));
                        if (listita.Buscar(el) == true) {
                            listita.eliminar(el);
                            JOptionPane.showMessageDialog(null, "El elemento : " + el
                                    + " Si esta en la lista", " Nodo no encontrado", JOptionPane.INFORMATION_MESSAGE);
                        } else {
                            JOptionPane.showMessageDialog(null, "El elemento: " + el
                                    + "No  esta en la lista", " Nodo no encontrado", JOptionPane.INFORMATION_MESSAGE);
                        }
                       break;
                    case 5:///IMPRIMIR
                        listita.mostrar();
//                        T.imprime();
                        break;
                    case 6:
                        JOptionPane.showMessageDialog(null, "Programa Finalizado");
                        break;
                    default:
                        JOptionPane.showMessageDialog(null, "opción incorecta");
                        break;
                }

            } catch (Exception e) {
                JOptionPane.showInputDialog(null, "Error " + e.getMessage());

            }
        } while (opcion != 6);

    }

}
