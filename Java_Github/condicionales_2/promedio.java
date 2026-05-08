package condicionales_2;
import java.util.Scanner;
public class promedio {
    public static void main(String[] args) {
        double nota1, nota2, nota3, promedio, promedio_redondeado;
        Scanner value = new Scanner(System.in);
        System.out.println("Ingrese la 1 nota");
        nota1 = value.nextDouble();
        System.out.println("Ingrese la 2 nota");
        nota2 = value.nextDouble();
        System.out.println("Ingrese la 3 nota");
        nota3 = value.nextDouble();
        promedio = (nota1+nota2+nota3)/3;
        promedio_redondeado = Math.round(promedio);
        if (promedio_redondeado >= 3) {
            System.out.println("Aprobado "+promedio_redondeado);
        } else {
            System.out.println("Reprobado "+promedio_redondeado);
        }
    }
}
