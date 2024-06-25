package Ejercicio2;

public class Perro extends Animal {
    private static int idCounter = 1;
    private int idPerro;
    private String ladrido;

    // Vacio
    public Perro() {
        this.idPerro = idCounter++;
    }

    // Todos los atributos
    public Perro(int edad, String raza, double peso, String color, String ladrido) {
        super(edad, raza, peso, color);
        this.idPerro = idCounter++;
        this.ladrido = ladrido;
    }

    // Parcial
    public Perro(int edad, String raza, String ladrido) {
        super(edad, raza);
        this.idPerro = idCounter++;
        this.ladrido = ladrido;
    }

    // Metodos GET
    public int getIdPerro() {
        return idPerro;
    }

    public String getLadrido() {
        return ladrido;
    }

    // Metodos SET
    public void setLadrido(String ladrido) {
        this.ladrido = ladrido;
    }

    @Override
    public String toString() {
        return super.toString() + ", Perro[idPerro=" + idPerro + ", ladrido=" + ladrido + "]";
    }
}
