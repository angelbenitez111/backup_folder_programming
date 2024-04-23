package Ejercicio_03;
import java.util.Scanner;

public class Operaciones {
    private double num1, num2, num3, num4;

    public void ingresarNumeros() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el primer número: ");
        num1 = scanner.nextDouble();

        System.out.println("Ingrese el segundo número: ");
        num2 = scanner.nextDouble();

        System.out.println("Ingrese el tercer número: ");
        num3 = scanner.nextDouble();

        System.out.println("Ingrese el cuarto número: ");
        num4 = scanner.nextDouble();

        scanner.close();
    }

    public double suma() {
        return num1 + num2 + num3 + num4;
    }

    public double resta() {
        return num1 - num2 - num3 - num4;
    }

    public double multiplicacion() {
        return num1 * num2 * num3 * num4;
    }

    public double division() {
        if (num2 == 0 || num3 == 0 || num4 == 0) {
            System.out.println("No se puede dividir por cero.");
            return 0;
        }
        return num1 / num2 / num3 / num4;
    }
}
