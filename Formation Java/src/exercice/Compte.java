package exercice;

public class Compte {
    public Double Solde;
    public Compte(Double s){
        this.Solde = s;
    }

    public void deposer(Double d){
        this.Solde += d;
    }
}