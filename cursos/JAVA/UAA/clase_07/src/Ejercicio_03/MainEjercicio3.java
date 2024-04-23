package Ejercicio_03;
public class MainEjercicio3 {
    public static void main(String[] args) {
        Operaciones operaciones = new Operaciones();

        operaciones.ingresarNumeros();

        System.out.println("La suma de los cuatro números es: " + operaciones.suma());
        System.out.println("La resta de los cuatro números es: " + operaciones.resta());
        System.out.println("La multiplicación de los cuatro números es: " + operaciones.multiplicacion());
        System.out.println("La división de los cuatro números es: " + operaciones.division());
    }
}
