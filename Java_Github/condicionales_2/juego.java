package condicionales_2;
import javax.swing.JOptionPane;

public class juego {
    public static void main(String[] args) {
        int num_aleatorio, num;
        num_aleatorio = (int) (Math.random() * 5) + 1;
        JOptionPane.showMessageDialog(null, "Tienes 3 intentos para adivinar un número del 1 al 5");
        for (int i = 3; i > 0; i--) {
            num = Integer.parseInt(JOptionPane.showInputDialog("Adivine el numero del 1 al 5"));
            if (num > 5 || num < 1) {
                JOptionPane.showMessageDialog(null, "ERROR: el numero esta fuera del rango");
                i++;
            } 
            else if (num == num_aleatorio) {
                JOptionPane.showMessageDialog(null, "¡Ganaste! El numero era " + num_aleatorio);
                break;
            } 
            else {
                if (i - 1 > 0) {
                    JOptionPane.showMessageDialog(null, "Fallaste. Te quedan " + (i - 1) + " intentos.");
                } else {
                    JOptionPane.showMessageDialog(null, "Perdiste todas tus vidas. El número correcto era " + num_aleatorio);
                }
            }
        }
    }
}