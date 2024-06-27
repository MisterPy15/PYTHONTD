public class Boucle {
// break pour intérrompre une boucle;
// continue;
// on a la boucle while et do-while => faire { instruction } tantque(condition);
// on a la boucle for et for each
    public static void main(String[] args){
//        int i = 0;
//
//        do{
////            if (i == 5){
////                continue; //Il ne va pas afficher 5 par contre il va sauter le chiffre 5 et aficher ce qui revies après
////            }
//            i++;
//
//            switch (i){
//                case 5:
//                    continue;
//            }
//            System.out.println(i);
//        }while (i != 10);

        //La boucle for
//        int i;
//         for (i =0; i != 10; i++){
//             System.out.println(i);

        // Outer loop
        for (int i = 1; i <= 2; i++) {
            System.out.println("Outer: " + i); // Executes 2 times

            // Inner loop
            for (int j = 1; j <= 3; j++) {
                System.out.println(" Inner: " + j); // Executes 6 times (2 * 3)

                for (int e = 1; e <= 4; e++){
                    System.out.println("Bonjour" + e);
                }
            }
        }
    }

    }

