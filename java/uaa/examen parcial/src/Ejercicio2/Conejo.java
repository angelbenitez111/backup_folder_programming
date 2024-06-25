package Ejercicio2;

public class Conejo extends Animal {
    private static int idCounter = 1;
    private int idConejo;
    private String salto;

    // Vacio
    public Conejo() {
        this.idConejo = idCounter++;
    }

    // Todos
    public Conejo(int edad, String raza, double peso, String color, String salto) {
        super(edad, raza, peso, color);
        this.idConejo = idCounter++;
        this.salto = salto;
    }

    // Parcial
    public Conejo(int edad, String raza, String salto) {
        super(edad, raza);
        this.idConejo = idCounter++;
        this.salto = salto;
    }

    // Metodos Get
    public int getIdConejo() {
        return idConejo;
    }

    public String getSalto() {
        return salto;
    }

    // Metodos set
    public void setSalto(String salto) {
        this.salto = salto;
    }

    @Override
    public String toString() {
        return super.toString() + ", Conejo[idConejo=" + idConejo + ", salto=" + salto + "]";
    }
}
