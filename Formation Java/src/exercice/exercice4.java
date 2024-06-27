package exercice;
import java.util.Scanner;

public class exercice4 {
    public static void main(String[] args){
        System.out.println("Veuillez Entre un nombre : ");
        Scanner scan = new Scanner(System.in);
        int nbr = scan.nextInt();
        int Parite = nbr % 2;

        if(Parite==0){
            System.out.println("Le nombre saisaie est paire");
        }else{
            System.out.println("Le nombre saisie est impaire");
        }
    }
}
