package exercice;

import java.util.Scanner;

public class exercice2 {
    public static void main(String[] agrs){
        System.out.println("Veullez Entrer un nombre : ");
        Scanner scan = new Scanner(System.in);
        int nbr = scan.nextInt();
        int Double = 2 * nbr;
        System.out.println("Le double de " + nbr + " est : "+Double);
    }
}
