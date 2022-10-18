
package TablasH;
import lista.Listas;
//import lista.Nodo;
///package lista;

/**
 *las tablas hash son nobles par hacer las busquedas
 */
public class Thash {
    private int fGlobal;
    private int tamaño;
    private Listas TH[];

    public Thash(int tamaño) {
        this.fGlobal=0;
        int i;
        this.tamaño = tamaño;
        this.TH = new Listas[tamaño];
        for (i = 0; i < this.tamaño; i++) 
            this.TH[i]= new Listas();
            
        }

    public int getfGlobal() {
        return fGlobal;
    }

    public int getTamaño() {
        return tamaño;
    }

    public Listas[] getTH() {
        return TH;
    }

    public void setTamaño(int tamaño) {
        this.tamaño = tamaño;
    }

    public void setfGlobal(int fGlobal) {
        this.fGlobal = fGlobal;
    }

    public void setTH(Listas[] TH) {
        this.TH = TH;
    
    }
        public int funModulo(int k){
        return (k % tamaño);

    }
        
    public void Inserta(int nuevo){
    int indice;
    indice =funModulo(nuevo);
    this.TH[indice].agregarFinal(nuevo);
    this.fGlobal ++;
    
    }

    public void imprime() {
        int i;
        for (i = 0; i < this.tamaño; i++) {
            System.out.print("F.L::" + this.TH[i].getClass() + "[" + i + "]-->");
            this.TH[i].mostrar();
        }

    }
}



  
    
    
    

