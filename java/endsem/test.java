// public class test {
//     public static void main(String[] args) {
//         int[] array = {1,2,3,4,5,6,7};
//         String str = new String("bionic_beaver");
//         System.out.println(str.length());
//         System.out.print("| ");
//         for (int x : array) {
//             System.out.print(Integer.toString(x)+"  |  ");
//         }
//         System.out.println();
//         System.out.print("| ");
//         for (int x : array) {
//             System.out.print(Integer.toString(x)+"  |  ");
//         }
//         System.out.println();
//     }
// }
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class test extends JFrame {
    JFrame frame = new JFrame();
    Button 

    test() {
        super("test");
        frame.setResizable(true);
        frame.setSize(400, 400);
        frame.defaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
    public static void main(String[] args) {
        new test();
    }
}
