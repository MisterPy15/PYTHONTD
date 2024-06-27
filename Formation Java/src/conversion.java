import java.util.Scanner;


public class conversion {
    public static void main(String[] args){
        System.out.println("Veuillez entre un nombre entre 6, 4, 8, 2 : h");
        Scanner sc = new Scanner(System.in);
        int nbr = sc.nextInt();

        switch (nbr){
            case 6:
                System.out.println("Le personnage va a droite ");
                break;
            case 4:
                System.out.println("Le personnage va gauche ");
                break;
            case 8:
                System.out.println("Le personnage va en haut");
                break;
            case 2:
                System.out.println("Le personnage va en bas");
                break;
            default:
                System.out.println("Erreur de saisie, le personnage ne bouge pas ");
        }


    }
}
