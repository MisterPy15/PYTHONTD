import java.sql.ResultSet;
// Pour lees commentaires

public class Operators {
   public static void main(String[] args){
       int result = 10 + 5 ;// Addiions
       System.out.println("10 + 5 =" + " " + result);

       int resultS = result - 3;
       System.out.println(result + " - 3 = " + resultS);

       int resultM = resultS * 2;
       System.out.println(resultS + " * 5 = " + resultM);

       int resultD = resultM / 5;
       System.out.println(resultM + " / 3 = " + resultD);

       int resultMo = resultD % 2;
       System.out.println(resultD + " % 2 = " + resultMo);


       // Incremantions Operators

       result ++ ;
       System.out.println(result);

       result -- ;
       System.out.println(result);

       // result = ressult + 2
       result += 2;
       System.out.println(result);

       // result = ressult - 2
       result -= 2;
       System.out.println(result);

       // result = ressult * 2
       result *= 2;
       System.out.println(result);

       // result = ressult / 2
       result /= 2;
       System.out.println(result);

       // result = ressult % 2
       result %= 2;
       System.out.println(result);



   }
}
