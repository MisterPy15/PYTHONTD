import java.util.Scanner;

public class discrminant {
    public static void main(String[] args){
        System.out.println("Entrez la valeur de a : ");
        Scanner scanA = new Scanner(System.in);
        int a = scanA.nextInt();

        

        System.out.println("Entrez la valeur de b : ");
        Scanner scanB = new Scanner(System.in);
        int b = scanB.nextInt();

        System.out.println("Entrez la valeur de c : ");
        Scanner scanC = new Scanner(System.in);
        int c = scanC.nextInt();

        int delta = (b*b) - 4 * a * c;
        System.out.println("Delta = " + delta);

        if (delta < 0){
            System.out.println("Il n'y a pa des solution");
        }else if (delta == 0){
            int X = (-b)/(2*a);
            System.out.println("Il n'y a qu'une soltion : "+X);
        }else{
            double X1 = ((-b) - Math.sqrt(delta))/ 2 * a;
            double X2 = ((-b) + Math.sqrt(delta))/ 2 * a;
        System.out.println("Il existe deux solutions X1 et X2");
            System.out.println("X1 = " + X1);
            System.out.println("X2 = " + X2);
        }



    }
}
