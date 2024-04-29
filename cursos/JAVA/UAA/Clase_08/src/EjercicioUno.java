import java.util.Scanner;

public class EjercicioUno {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int watermelon_weight;

        do {
            System.out.println("Enter the weight of the watermelon (between 1 and 2000)");
            watermelon_weight = scanner.nextInt();
        } while (watermelon_weight <= 1 || watermelon_weight >= 2000);

        if (watermelon_weight % 2 == 0 && watermelon_weight > 2) {
            System.out.println("Can be divided equally.");
        } else {
            System.out.println("Cannot be divide equally");
        }
    }
}
