package Ejercicio_01;

public class Principal {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan", 'M', 30, "Ingeniero");
        Persona persona2 = new Persona("María", "Gómez", "12345678");
        Persona persona3 = new Persona("Pedro", "López", "87654321", 'M', 25, "Estudiante");

        System.out.println("Persona 1: " + persona1.getNombre() + ", " + persona1.getSexo() + ", " + persona1.getEdad() + ", " + persona1.getProfesion());
        System.out.println("Persona 2: " + persona2.getNombre() + " " + persona2.getApellido() + ", Cédula: " + persona2.getNumero_ci());
        System.out.println("Persona 3: " + persona3.getNombre() + " " + persona3.getApellido() + ", Cédula: " + persona3.getNumero_ci() + ", " + persona3.getSexo() + ", " + persona3.getEdad() + ", " + persona3.getProfesion());

        persona1.setNombre("Carlos");
        persona1.setEdad(35);

        System.out.println("Persona 1 (modificada): " + persona1.getNombre() + ", " + persona1.getSexo() + ", " + persona1.getEdad() + ", " + persona1.getProfesion());

        Persona persona4 = new Persona();
        persona4.setNombre("Laura");
        persona4.setApellido("González");
        persona4.setNumero_ci("98765432");
        persona4.setSexo('F');
        persona4.setEdad(28);
        persona4.setProfesion("Doctora");

        System.out.println("Persona 4: " + persona4.getNombre() + " " + persona4.getApellido() + ", Cédula: " + persona4.getNumero_ci() + ", " + persona4.getSexo() + ", " + persona4.getEdad() + ", " + persona4.getProfesion());
    }
}
