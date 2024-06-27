import java.awt.*;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;



 public class interface1 {
     public static void main(String[] args){

         JFrame fenetre = new JFrame();
         fenetre.setTitle("My First Interface");
         fenetre.setSize(400, 250);
         fenetre.setLocationRelativeTo(null);
         boolean b1 = false;
         boolean b2 = true;
         fenetre.setResizable(b1);
         fenetre.setAlwaysOnTop(b2);


         fenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

         fenetre.setVisible(true);
     }
 }

