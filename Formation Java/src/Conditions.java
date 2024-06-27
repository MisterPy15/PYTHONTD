public class Conditions {

    public static void main(String[] args){
        int age = 19;

        if (age >= 18){
            System.out.println("Vous avez " + age + " Ans, Vous êtes mineur");
        } else if (age == 18) {
            System.out.println("Vous Avez " + age + " Ans");
        }else{
            System.out.println("Cette Option n'eciste pas ");
        }
    }
}
