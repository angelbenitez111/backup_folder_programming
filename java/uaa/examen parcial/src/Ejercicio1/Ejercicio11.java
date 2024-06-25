package Ejercicio1;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Ejercicio11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> strings = new ArrayList<>();
        int numStrings;
        int contador = 0;

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
                    System.out.println("El texto esta compuesto solo por espacios. Por favor reingrese.");
                } else {
                    break;
                }
            } while (true);

            strings.add(input);
        }


        ArrayList<String> palindromos = new ArrayList<>();
        for (String str : strings) {
            if (esPalindromo(str)) {
                palindromos.add(str);
                contador++;
            }
        }

        // Filtrar elementos
        palindromos = (ArrayList<String>) palindromos.stream().distinct().collect(Collectors.toList());

        System.out.println("Cantidad de palindromos: " + contador);
        impresion(palindromos);

    }

    public static void impresion(ArrayList<String> palindromos) {
        if (palindromos.isEmpty()) {
            System.out.println("No se encontro ninguna palabra palindroma.");
        } else {
            System.out.println("Palabras palndromas encontradas:");
            for (String palindro : palindromos) {
                System.out.println(palindro);
            }
        }
    }


    // Metodo para verificar que es un palindromo
    public static boolean esPalindromo(String str) {
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

