#conding utf-8

class Humain:
    def __init__(self, C_nom, C_age1=17, C_age2=19):
      
       self.Nom = C_nom
       self.age1 = C_age1
       self.age2 = C_age2

print("Lancement du programme")

<<<<<<< HEAD

=======
>>>>>>> c739d220f8696e11e0686d52345056f08433c336
c1 = Humain("Agoh")
print("le Nom de c1 est: {}".format(c1.Nom))
print("l'age de c1 est : {} ans".format(c1.age1))

c2 = Humain("Chris")
print("le prenom de c2 est : {}".format(c2.Nom))
print("l'age de c2 est : {} ans".format(c2.age2))