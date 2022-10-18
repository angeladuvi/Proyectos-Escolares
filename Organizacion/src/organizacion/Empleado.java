/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package organizacion;

/**
 *
 * @author DELL
 */
public class Empleado {
	private String Nombre;
	private int NumeroEmpleado;
	private int Puesto;
	private char Turno;
	private float Salario;
	
	public Empleado(String Nombre, int Puesto, char Turno, float Salario ) {
		this.Nombre = Nombre;
		this.NumeroEmpleado = (int) Math.random() * 10 + 1;
		this.Puesto = Puesto;
		this.Turno = Turno;
		this.Salario = Salario;
	}
	
	





	public String getNombre() {
		return Nombre;
	}
	
	public void setNombre(String nombre) {
		Nombre = nombre;
	}
	
	public int getNumeroEmpleado() {
		return NumeroEmpleado;
	}
	
	public void setNumeroEmpleado(int numeroEmpleado) {
		NumeroEmpleado = numeroEmpleado;
	}
	
	public int getPuesto() {
		return Puesto;
	}
	
	public void setPuesto(int puesto) {
		Puesto = puesto;
	}
	
	public char getTurno() {
		return Turno;
	}
	
	public void setTurno(char turno) {
		Turno = turno;
	}
	
	public float getSalario() {
		return Salario;
	}
	
	public void setSalario(float salario) {
		Salario = salario;
	}

//
//	public void Imprime() {
//		System.out.println("Nombre" + this.Nombre);
//		System.out.println("Numero del empleado:" +this.NumeroEmpleado);
//		System.out.println("Puesto" + this.Puesto);
//		System.out.println("Turno" + this.Turno);
//		System.out.println("salario" + this.Salario);
//	}

}
