import javax.swing.JOptionPane;

public class ejercicios {
    public static void main(String[] args) {
        String dato = JOptionPane.showInputDialog("Digite un numero");
        int num1 = Integer.parseInt(dato);
        if (num1 > 0) {
            JOptionPane.showInputDialog("Es positivo");
        } else if (num1 < 0) {
            JOptionPane.showInputDialog("Es negativo");
        } else {
            JOptionPane.showInputDialog("Es " + num1);
        }
    }
}
