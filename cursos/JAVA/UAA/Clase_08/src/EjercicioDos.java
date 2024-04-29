import java.util.Scanner;

public class EjercicioDos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numbers = new int[10];

        for (int i = 0; i < 10; i++) {
            System.out.println("Enter the number " + (i + 1) + ": ");
            numbers[i] = scanner.nextInt();
        }

        System.out.println("Multiple of 2:");
        for (int num : numbers) {
            if (num % 2 == 0) {
                System.out.println(num);
            }
        }
        System.out.println("Not multiple of 2:");
        for (int num : numbers) {
            if (num % 2 != 0) {
                System.out.println(num);
            }
        }
    }
}
