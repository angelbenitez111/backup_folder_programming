package Ejercicio1;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Ejercicio12 {
    public static void main(String[] args) {
        Ejercicio12 ejercicio = new Ejercicio12();
        int contador = 0;
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> strings = new ArrayList<>();
        int numStrings;

        System.out.println("Ingrese la cantidad de strings:");
        numStrings = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < numStrings; i++) {
            String input;
            do {
                System.out.println("Ingrese el string en la posicion " + (i + 1) + ":");
                input = scanner.nextLine();

                if (input.length() > 10) {
                    System.out.println("El texto supera los 10 caracteres. Por favor reingrese");
                } else if (input.trim().isEmpty()) {
                    System.out.println("El texto est compuesto solo por espacios. Por favor reingrese.");
                } else {
                    break;
                }
            } while (true);

            strings.add(input);
        }

        ArrayList<String> palindromos = new ArrayList<>();
        for (String str : strings) {
            if (ejercicio.esPalindromo(str)) {
                palindromos.add(str);
                contador++;
            }
        }

        // Filtrar elementos
        palindromos = (ArrayList<String>) palindromos.stream().distinct().collect(Collectors.toList());

        System.out.println("Cantidad de palindromos: " + contador);
        ejercicio.impresion(palindromos);

    }

    public void impresion(ArrayList<String> palindromos) {
        if (palindromos.isEmpty()) {
            System.out.println("No se encontro ninguna palabra palindroma.");
        } else {
            System.out.println("Palabras palindromas encontradas:");
            for (String palindromo : palindromos) {
                System.out.println(palindromo);
            }
        }
    }

    // Metodo para verificar que es un palindromo
    public boolean esPalindromo(String str) {
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
