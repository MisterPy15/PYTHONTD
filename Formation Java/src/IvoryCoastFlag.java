import javax.swing.*;
import java.awt.*;

public class IvoryCoastFlag extends JFrame {

    public IvoryCoastFlag() {
        setTitle("Côte d'Ivoire Flag");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        add(new FlagPanel());
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new IvoryCoastFlag().setVisible(true);
        });
    }
}

class FlagPanel extends JPanel {

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Bande orange
        g.setColor(new Color(247, 127, 0));
        g.fillRect(50, 50, 50, 200);

        // Bande blanche
        g.setColor(new Color(255, 255, 255));
        g.fillRect(100, 50, 50, 200);



        // Bande verte
        g.setColor(new Color(0, 151, 57));
        g.fillRect(150, 50, 50, 200);

        // Écrire "Mister Py"
        g.setColor(Color.BLACK);
        Font font = new Font("Arial", Font.PLAIN, 12);
        g.setFont(font);
        g.drawString("By Mister Py", 150, 220);
    }
}