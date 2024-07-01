public class Main {
    public static void main(String[] args) {
        Mensaje[] mensajes = new Mensaje[5];

        mensajes[0] = new MensajeHijo1();
        mensajes[1] = new MensajeHijo2();
        mensajes[2] = new MensajeHijo3();
        mensajes[3] = new MensajeHijo4();
        mensajes[4] = new MensajeHijo5();

        for (Mensaje mensaje : mensajes) {
            mensaje.imprimirMensaje();
        }
    }
}