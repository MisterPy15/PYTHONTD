package exercice;
import java.util.Scanner;

public class exercice6 {
    public static void main(String[] args){
        System.out.println("Entrez le nombre : ");
        Scanner nbrScan = new Scanner(System.in);
        int NbrRecup = nbrScan.nextInt();
        int i = 0;
        int j = -1;

        while (j < NbrRecup){
            j++;
            i += j;
        }
        System.out.println("Le somme est : " + i);
    }
}
