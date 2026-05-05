package fundamentos_java;
import java.util.Stack;
public class estructura_de_datos {
    public static void main(String[] args) {

        Stack<String> pila_de_libros = new Stack<>();
        pila_de_libros.push("libro de programacion");
        pila_de_libros.push("libro de lenguaje");
        pila_de_libros.push("libro de ingles");
        System.out.println(pila_de_libros);
        String libro_sacado = pila_de_libros.pop();
        System.out.println(libro_sacado);
        System.out.println(pila_de_libros);
    }
}