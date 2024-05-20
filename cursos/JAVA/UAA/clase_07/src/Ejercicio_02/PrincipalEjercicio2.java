package Ejercicio_02;

import java.util.Scanner;

public class PrincipalEjercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el nombre: ");
        String nombre = scanner.nextLine();

        System.out.println("Ingrese el apellido: ");
        String apellido = scanner.nextLine();

        System.out.println("Ingrese el número de cédula: ");
        String numero_ci = scanner.nextLine();

        System.out.println("Ingrese el sexo (M/F): ");
        char sexo = scanner.next().charAt(0);

        System.out.println("Ingrese la edad: ");
        int edad = scanner.nextInt();
        scanner.nextLine();

        System.out.println("Ingrese la profesión: ");
        String profesion = scanner.nextLine();

        Persona persona = new Persona(nombre, apellido, numero_ci, sexo, edad, profesion);

        // Imprimir los datos de la persona
        System.out.println("Datos de la persona:");
        System.out.println("Nombre: " + persona.getNombre());
        System.out.println("Apellido: " + persona.getApellido());
        System.out.println("Número de cédula: " + persona.getNumero_ci());
        System.out.println("Sexo: " + persona.getSexo());
        System.out.println("Edad: " + persona.getEdad());
        System.out.println("Profesión: " + persona.getProfesion());

        scanner.close();
    }
}
