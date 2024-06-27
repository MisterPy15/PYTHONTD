public class Cour2J_C {
    /*
        ==  égal a
        === égal et de même type que
        !=  différent
        <   strictement inférieur
        >   strictement supérieur
        <=  inférieur ou égal
        >=  supérieur ou égal
        !   inverse de (négatinn)
        &&  Et
        ||  Ou
    */
    public static void main(String[] args){

/*        int value = -6;

        if (value < 0){
            System.out.println("value est < 0");
            if (value == -6){
                System.out.println("value = -6");
            }
        } else if (value > 100) {
            System.out.println("value = 100");
        }        else {
            System.out.println(value);
                    }
 */


        /*
            Pour nous facilité la tache et racourcir notre code ontt peut utiliser le mot clé "switch"
        */

    int option = 120;

    switch(option){
        case 1: //reviens a dire que: if (option == 1)
            System.out.println("option = 1");
            break;
        default: // rviens dire else
            System.out.println("option != 1");
            break;
    }

    }
    }

