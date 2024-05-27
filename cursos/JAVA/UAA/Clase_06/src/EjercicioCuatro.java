import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class EjercicioCuatro {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("Ingrese la cédula:");
        String ci = reader.readLine();

        System.out.println("Ingrese los nombres:");
        String first_name = reader.readLine();

        System.out.println("Ingrese los apellidos:");
        String last_name = reader.readLine();

        System.out.println("Ingrese la edad:");
        int age = Integer.parseInt(reader.readLine());

        System.out.println("Ingrese la carrera:");
        String career = reader.readLine();

        System.out.print("\n\nDatos de la persona:\n");
        System.out.printf("Cédula: %s", ci);
        System.out.println("Nombres: " + first_name);
        System.out.println("Apellidos: " + last_name);
        System.out.println("Edad: " + age);
        System.out.println("Carrera: " + career);
    }
}