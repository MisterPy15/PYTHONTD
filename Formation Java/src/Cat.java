public class Cat {
    public Cat(String name, int age){
        System.out.println("Je suis un Développeur full-stack : " + this);

        this.m_Name = name;
        this.m_Age = age;

        System.out.println("Son nom est " + this.m_Name + " et il à " + this.m_Age + " Ans");
    }
    private String m_Name;
    private int m_Age;
}