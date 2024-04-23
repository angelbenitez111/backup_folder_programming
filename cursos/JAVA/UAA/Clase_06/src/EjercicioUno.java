import java.util.Scanner;

public class EjercicioUno {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Inserted and printed five words
        System.out.println("Ingrese 5 palabras: ");
        for (int i = 0; i < 5; i++) {
            String word = scanner.next();
            System.out.println("Palabra " + (i+1) + ": " + word);
        }

        // Inserted and printed five integer numbers
        System.out.println("Ingrese 5 numeros enteros: ");
        for (int i = 0; i < 5; i++) {
            int number = scanner.nextInt();
            System.out.println("Numero " + (i+1) + ": " + number);
        }

        // Inserted and printed five float numbers
        System.out.println("Ingrese 5 numeros flotantes:");
        for (int i=0; i < 5; i++) {
            float number = scanner.nextFloat();
            System.out.println("Numero flotante " + (i+1) + ": " + number);
        }
    }
}