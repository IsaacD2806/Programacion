package condicionales_2;
import java.util.Scanner;
public class contraseña {
    public static void main(String[] args) {
        String password, saved_password;
        Scanner value = new Scanner(System.in);
        saved_password = "Cecar2026";
        saved_password = saved_password.toLowerCase();
        System.out.println("Escriba su contraseña");
        password = value.nextLine();
        password = password.toLowerCase();
        if (password.length() >= 8 && saved_password.equals(password)) {
            System.out.println("Acceso concedido");
        }else {
            System.out.println("Acceso denegado");
        }
    }
}
