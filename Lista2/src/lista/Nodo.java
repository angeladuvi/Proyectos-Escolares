
package lista;

public class Nodo {

    public int dato;
    public Nodo siguiente;
///constructor al final
    public Nodo(int d) {
        this.dato = d;
        this.siguiente = null;
    }
//constructor  insertar al inicio
    public Nodo(int d, Nodo n) {
        dato = d;
        siguiente = n;
    }
}
