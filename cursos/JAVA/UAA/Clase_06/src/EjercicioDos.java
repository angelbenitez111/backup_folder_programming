import java.util.Scanner;

public class EjercicioDos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Inserted and printed five words
        System.out.println("Ingrese 5 palabras: ");
        for (int i = 0; i < 5; i++) {
            String word = scanner.next();
            System.out.printf("Palabra %d: %s\n", (i+1), word);
        }

        // Inserted and printed five integer numbers
        System.out.println("Ingrese 5 numeros enteros: ");
        for (int i = 0; i < 5; i++) {
            int number = scanner.nextInt();
            System.out.printf("Número entero %d: %d\n", (i+1), number);
        }

        // Inserted and printed five float numbers
        System.out.println("Ingrese 5 numeros flotantes:");
        for (int i=0; i < 5; i++) {
            float number = scanner.nextFloat();
            System.out.printf("Número flotante %d: %f\n", (i+1), number);
        }
    }
}
/*
%d: integer.
%f: float.
%s: string.
%.nf: Float with n number of decimal. (example: %.2f)
%c: Character.
%b: Boolean.
%t: Date/time (requires a specialized required)
 */
