import javax.swing.*;
import java.awt.*;



public class window {
    public static void main(String[] arg){
        JFrame cadre = new JFrame("Mon interface");
        cadre.setSize(300, 200);
        cadre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JButton boutton = new JButton("Cliquez");
        cadre.add(boutton);
        cadre.setVisible(true);

    }
}
