import java.util.Scanner;

public class EjercicioUno {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int watermelonWeight;

        do {
            System.out.println("Enter the weight of the watermelon (between 1 and 2000):");
            watermelonWeight = scanner.nextInt();
        } while (watermelonWeight <= 1 || watermelonWeight >= 2000);

        if (watermelonWeight % 2 == 0 && watermelonWeight > 2) {
            System.out.println("Can be divided.");
        } else {
            System.out.println("Cannot be divide");
        }
    }
}
