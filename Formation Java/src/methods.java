public class methods {
//    public static void main(String[]  args){
//        //methods
//        String nom = "Mister ";
//        String Prenom = "Py ";
//        UserInformation(nom, Prenom);
//    }
//    public static void UserInformation(String nom, String prenom){
//        System.out.println("Bonsoir " + nom + prenom);
//    }

    //Exercice

    public static void main(String[] args){

        boolean gameOver = true;
        int score = 1000;
        int bonus = 200;
        int ScoreFinal = 0;

        ScoreExact(gameOver, score, bonus, ScoreFinal);
    }

    public static  void ScoreExact(boolean GameOver ,int Score, int bonus, int ScoreFinale){
        if (GameOver){
            ScoreFinale = Score + bonus;
            System.out.println("Le Score final est : " + ScoreFinale);
        }
    }

}
