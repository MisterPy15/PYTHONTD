package Encapsulation;

public class SoftWareRegistration {

    public SoftWareRegistration(int expiration){
        this.mExperationYear = expiration;
        System.out.println("Enregistrement du produit, Valide jusqu'en " + this.mExperationYear);
    }

    private int mExperationYear;
}
