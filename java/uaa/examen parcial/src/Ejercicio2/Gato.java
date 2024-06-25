package Ejercicio2;

public class Gato extends Animal {
    private static int idCounter = 1;
    private int idGato;
    private String ronroneo;

    // Vacio
    public Gato() {
        this.idGato = idCounter++;
    }

    // Todos
    public Gato(int edad, String raza, double peso, String color, String ronroneo) {
        super(edad, raza, peso, color);
        this.idGato = idCounter++;
        this.ronroneo = ronroneo;
    }

    // Parcial
    public Gato(int edad, String raza, String ronroneo) {
        super(edad, raza);
        this.idGato = idCounter++;
        this.ronroneo = ronroneo;
    }

    // Metodos GET
    public int getIdGato() {
        return idGato;
    }

    public String getRonroneo() {
        return ronroneo;
    }

    // Metodos SET
    public void setRonroneo(String ronroneo) {
        this.ronroneo = ronroneo;
    }

    @Override
    public String toString() {
        return super.toString() + ", Gato[idGato=" + idGato + ", ronroneo='" + ronroneo +  "]";
    }
}
