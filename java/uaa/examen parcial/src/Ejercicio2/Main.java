package Ejercicio2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Perro[] perros = new Perro[3];
        Gato[] gatos = new Gato[3];
        Conejo[] conejos = new Conejo[3];

        // Perros
        for (int i = 0; i < 3; i++) {
            int edad;
            do {
                System.out.print("Ingrese la edad del Perro " + (i + 1) + " (menor o igual a 30):");
                edad = scanner.nextInt();
                scanner.nextLine();
                if (edad > 30) {
                    System.out.println("La edad debe ser menor o igual a 30. Por favor, reingrese.");
                }
            } while (edad > 30);

            System.out.print("Raza: ");
            String raza = scanner.nextLine();
            System.out.print("Peso: ");
            double peso = scanner.nextDouble();
            scanner.nextLine();
            System.out.print("Color: ");
            String color = scanner.nextLine();
            System.out.print("Ladrido: ");
            String ladrido = scanner.nextLine();

            perros[i] = new Perro(edad, raza, peso, color, ladrido);
        }

        // Gatos
        for (int i = 0; i < 3; i++) {
            int edad;
            do {
                System.out.print("Ingrese la edad del Gato " + (i + 1) + " (menor o igual a 30):");
                edad = scanner.nextInt();
                scanner.nextLine();
                if (edad > 30) {
                    System.out.println("La edad debe ser menor o igual a 30. Por favor, reingrese.");
                }
            } while (edad > 30);

            System.out.print("Raza: ");
            String raza = scanner.nextLine();
            System.out.print("Peso: ");
            double peso = scanner.nextDouble();
            scanner.nextLine();
            System.out.print("Color: ");
            String color = scanner.nextLine();
            System.out.print("Ronroneo: ");
            String ronroneo = scanner.nextLine();

            gatos[i] = new Gato(edad, raza, peso, color, ronroneo);
        }

        // Conejos
        for (int i = 0; i < 3; i++) {
            int edad;
            do {
                System.out.print("Ingrese la edad del Conejo " + (i + 1) + " (menor o igual a 30):");
                edad = scanner.nextInt();
                scanner.nextLine();
                if (edad > 30) {
                    System.out.println("La edad debe ser menor o igual a 30. Por favor, reingrese.");
                }
            } while (edad > 30);

            System.out.print("Raza: ");
            String raza = scanner.nextLine();
            System.out.print("Peso: ");
            double peso = scanner.nextDouble();
            scanner.nextLine();
            System.out.print("Color: ");
            String color = scanner.nextLine();
            System.out.print("Salto: ");
            String salto = scanner.nextLine();

            conejos[i] = new Conejo(edad, raza, peso, color, salto);
        }

        // Imprimir datos
        System.out.println("\nDatos de los Perros:");
        for (Perro perro : perros) {
            System.out.println(perro);
        }

        System.out.println("\nDatos de los Gatos:");
        for (Gato gato : gatos) {
            System.out.println(gato);
        }

        System.out.println("\nDatos de los Conejos:");
        for (Conejo conejo : conejos) {
            System.out.println(conejo);
        }
    }
}
