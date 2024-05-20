import java.util.Scanner;

public class EjercicioTres {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Ingrese la cédula:");
        String ci = scanner.nextLine();
        
        System.out.println("Ingrese los nombres:");
        String first_name = scanner.nextLine();
        
        System.out.println("Ingrese los apellidos:");
        String last_name = scanner.nextLine();
        
        System.out.println("Ingrese la edad:");
        int age = scanner.nextInt();

        scanner.nextLine(); // Consume pending line break

        System.out.println("Ingrese la carrera:");
        String career = scanner.nextLine();
        
        System.out.print("\n\nDatos de la persona:\n");
        System.out.printf("Cédula: %s", ci);
        System.out.println("Nombres: " + first_name);
        System.out.println("Apellidos: " + last_name);
        System.out.println("Edad: " + age);
        System.out.println("Carrera: " + career);
    }
}