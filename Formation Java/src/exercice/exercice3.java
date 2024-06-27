package exercice;
import java.util.Scanner;

public class exercice3 {
    public static void main(String[] args){
        System.out.println("Entrez Le nombre 1 : ");
        Scanner nbr1 = new Scanner(System.in);
        int Vnombe1 = nbr1.nextInt();

        Scanner nbr2 = new Scanner(System.in);
        System.out.println("Entrez la nombre 2 : ");
        int Vnombre2 = nbr2.nextInt();


        if (Vnombe1 > Vnombre2){
            System.out.println("Le maximum est : " + Vnombe1);
        } else if (Vnombre2 > Vnombe1) {
            System.out.println("Le maximum est : " + Vnombre2);
        } else{
            System.out.println("Les nombres saisi sont égaux.");
        }
    }
}
