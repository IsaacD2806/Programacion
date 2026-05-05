package fundamentos_java;
import java.util.Scanner;
public class condicionales {
    public static void main(String[] args) {
        Scanner var1 = new Scanner(System.in);
        int edad;
        edad = var1.nextInt();
        if (edad >= 18) {
            System.out.println("mayor de edad");
        }
        else {
            System.out.println("menor de edad ");
        }
    }
}
