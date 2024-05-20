package Ejercicio_01;

public class Persona {
    //definición de los atributos de la clase
    private String nombre;
    private String apellido;
    private String numero_ci;
    private char sexo;
    private int edad;
    private String profesion;

    public Persona(String nombre, String apellido, String numero_ci, char sexo, int edad, String profesion){
        this.nombre = nombre;
        this.apellido = apellido;
        this.numero_ci = numero_ci;
        this.sexo = sexo;
        this.edad = edad;
        this.profesion = profesion;
    }

    public Persona(String nombre, String apellido, String numero_ci) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.numero_ci = numero_ci;
    }

    public Persona(String nombre, char sexo, int edad, String profesion){
        this.nombre = nombre;
        this.sexo = sexo;
        this.edad = edad;
        this.profesion = profesion;
    }

    //Constructor vacío sin parámetros
    public Persona(){

    }

    //Métodos GETs
    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public String getNumero_ci() {
        return numero_ci;
    }

    public char getSexo() {
        return sexo;
    }

    public int getEdad() {
        return edad;
    }

    public String getProfesion() {
        return profesion;
    }

    //METODOS SETs
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public void setNumero_ci(String numero_ci) {
        this.numero_ci = numero_ci;
    }

    public void setSexo(char sexo) {
        this.sexo = sexo;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setProfesion(String profesion) {
        this.profesion = profesion;
    }

}
