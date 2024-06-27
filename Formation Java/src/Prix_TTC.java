import java.util.Scanner;

public class Prix_TTC {
    public static void main(String[] args){
        double A = 0.07;
        double B = 0.20;
        double C = 0.25;

        System.out.println("Entrez le PHT : ");
        Scanner sc = new Scanner(System.in);
        double PHT = sc.nextDouble();
        System.out.println("Entrez la catégorie : ");
        Scanner catSc = new Scanner(System.in);
        String Cat = catSc.nextLine();



        switch (Cat){
            case "A":
                double PTTCA = PHT + PHT * A;
                System.out.println("Le prix TTC de A est : "+PTTCA);
                break;

            case "B":
                double PTTCB = PHT + PHT * B;
                System.out.println("Le prix TTC de B est : "+ PTTCB);
                break;

            case "C":
                double PTTCC = PHT + PHT * C;
                System.out.println("Le prix TTC de C est : "+PTTCC);
                break;

            default:
                System.out.println("Catégorie non prise en charge.");
        }

    }
}
