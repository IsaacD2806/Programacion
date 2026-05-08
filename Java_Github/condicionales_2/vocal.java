package condicionales_2;
import javax.swing.JOptionPane;
public class vocal {
    public static void main(String[] args) {
        String palabra;
        char primera_letra;
        palabra =JOptionPane.showInputDialog("Escriba una palabra");
        palabra = palabra.toLowerCase();
        primera_letra = Character.toLowerCase(palabra.charAt(0));
        if ("aeiou".indexOf(primera_letra)!=-1) {
            JOptionPane.showMessageDialog(null, "La primera letra es una vocal");
        }
        else {
            JOptionPane.showMessageDialog(null, "La primera letra es una consonate");
        }
    }
}
