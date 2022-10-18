
package lista;

public class Listas {

    protected Nodo inicio, fin;//puntero al inicio y al final 

    public Listas() {
        inicio = null;
        fin = null;

    }

    public boolean estaVacia() {
        if (inicio == null) {
            return true;
        } else {
            return false;
        }
    }

    public void agregarInicio(int elemento) {
        inicio = new Nodo(elemento, inicio);
        if (fin == null) {
            fin = inicio;
        }
    }
////metodo para incertar al final de la lista

    public void agregarFinal(int elemento) {
        if (!estaVacia()) {
            fin.siguiente = new Nodo(elemento);
            fin = fin.siguiente;
        } else {
            inicio = fin = new Nodo(elemento);
        }

    }

    public void mostrar() {
        Nodo recorrer = inicio;
        System.out.println(" ");
        while (recorrer != null) {
            System.out.print("[" + recorrer.dato + "]-->");
            recorrer = recorrer.siguiente;

        }
    }

    public boolean Buscar(int elemento) {
        Nodo temporal = inicio;
        while (temporal != null && temporal.dato != elemento) {
            temporal = temporal.siguiente;
        }
        return temporal != null;

    }

    ///borrar un nodo especifico
    public void eliminar(int elemento) {
        if (!estaVacia()) {
            if (inicio == fin && elemento == inicio.dato) {
                inicio = fin = null;
            } else if (elemento == inicio.dato) {
                inicio = inicio.siguiente;
            } else {
                Nodo anterior, temporal;
                anterior = inicio;
                temporal = inicio.siguiente;
                while (temporal != null && temporal.dato != elemento) {
                    anterior = anterior.siguiente;
                    temporal = temporal.siguiente;
                }
                if (temporal != null) {
                    anterior.siguiente = temporal.siguiente;
                    if (temporal == fin) {
                        fin = anterior;
                    }

                }
            }

        }
    }

    
}
