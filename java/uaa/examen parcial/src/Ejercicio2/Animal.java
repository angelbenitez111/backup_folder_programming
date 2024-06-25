package Ejercicio2;

public class Animal {
    protected  int edad;
    protected String raza;
    protected double peso;
    protected String color;

    // Vacio
    public Animal() {}

    // Todos los atributos
    public Animal(int edad, String raza, double peso, String color) {
        this.edad = edad;
        this.raza = raza;
        this.peso = peso;
        this.color = color;
    }

    // Parcial
    public Animal(int edad, String raza) {
        this.edad = edad;
        this.raza = raza;
    }


    // Metodos GET
    public int getEdad() {
        return edad;
    }

    public String getRaza() {
        return raza;
    }

    public double getPeso() {
        return peso;
    }

    public String getColor() {
        return color;
    }

    // Metodos SET
    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setRaza(String raza) {
        this.raza = raza;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        return "Animal [Edad=" + edad + ", Raza=" + raza + ", Peso=" + peso +", Color=" + color + "]";
    }
}
