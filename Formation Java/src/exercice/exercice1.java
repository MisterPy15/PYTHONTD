package exercice;

import java.util.Scanner;

public class exercice1 {
    public static void main(String[] args){
        System.out.println("Veuillez entrer votre nom : ");
        Scanner scan = new Scanner(System.in);
        String nom = scan.nextLine();
        System.out.println("Bienvenue " + nom);
    }
}
