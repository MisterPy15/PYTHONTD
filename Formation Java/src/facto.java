import java.util.Scanner;
public class facto {
    public static void main(String[] args){
        int nbr = 4;

        while (nbr < 0){
            System.out.println("Entrez une valeur positive");
            if (nbr > 0){
                break;
            }
        }
        if (nbr == 0){
            System.out.println("La factorielle de"+nbr+"1");
        }
        else{
            int F = 1;
            for(int i=1; i<=nbr; i++){
                F *=i;
            }
            System.out.println("La factorielle de "+nbr+" est: "+F);
        }
    }
}
