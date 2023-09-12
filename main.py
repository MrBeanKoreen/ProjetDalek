import random
# TEST UN DEUD TRI
class Jeu():
    def __init__(self):
        self.partie = None
        self.nom_joueur = None

    def jouer_coup(self, rep):
        self.partie.jouer_coup(rep)

    def creer_partie(self):
        self.partie = Partie()

class Partie():
    def __init__(self):
        self.airdejeu = AiredeJeu(12, 6)
        self.docteur = Docteur(random.randrange(self.airdejeu.largeur), random.randrange(self.airdejeu.hauteur), self)
        self.daleks = []
        self.niveau = 0
        self.dalek_par_niveau = 5
        self.creer_niveau()

    def jouer_coup(self,rep):
        if self.docteur.changer_position(rep):
            pass
        return True

    def creer_niveau(self):
        self.niveau += 1
        nb_daleks = self.niveau * self.dalek_par_niveau
        for i in range(nb_daleks):
            while True:
                x = random.randrange(self.airdejeu.largeur)
                y = random.randrange(self.airdejeu.hauteur)
                if(x,y) != (self.docteur.x, self.docteur.y) and all((x,y) != (dalek.x, dalek.y) for dalek in self.daleks):
                    dalek = Dalek(x,y)
                    self.daleks.append(dalek)
                    break

class AiredeJeu():
    def __init__(self, largeur: int, hauteur: int):
        self.largeur = largeur
        self.hauteur = hauteur

class Ferraille():
    def __init__(self, x, y):
        self.x = None
        self.y = None

class Docteur():
    def __init__(self, x, y, partie):
        self.x = x
        self.y = y
        self.partie = partie

    def changer_position(self, pos_relative):
        """ tester les limite avant """
        rel_x, rel_y = pos_relative
        if self.x + rel_x < 0 or self.y + rel_y < 0 or self.x + rel_x > (self.partie.airdejeu.largeur - 1) or self.y + rel_y > (self.partie.airdejeu.hauteur - 1):
            return False
        else:
            self.x += rel_x
            self.y += rel_y
            return True
class Dalek():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer(self, docteur):
        doc_x = docteur.x
        doc_y = docteur.y

        if self.x < doc_x:
            self.x += 1
        elif self.x > doc_x:
            self.x -= 1

        if self.y < doc_y:
            self.y += 1
        elif self.y > doc_y:
            self.y -= 1

class Vue():
    def __init__(self):
        self.pos_poss = rep_possible = {"1": [-1, 1], "2": [0, 1], "3": [1, 1], "4": [-1, 0], "5": [0, 0], "6": [1, 0], "7": [-1, -1], "8": [0, -1], "9": [1, -1]}

    def cree_tableau(self, partie):
        tableau = []
        for i in range(partie.airdejeu.hauteur):
            ligne = []
            for j in range(partie.airdejeu.largeur):
                ligne.append('-')
            tableau.append(ligne)
        return tableau

    def afficher_aire_jeu(self, partie):
        tableau = self.cree_tableau(partie)
        for i in partie.daleks:
            tableau[i.y][i.x] = "W"
        tableau[partie.docteur.y][partie.docteur.x] = "D"
        for i in tableau:
            print(i)
        return self.jouer_coup()

    def jouer_coup(self):
        print("\n1: \u2199 | 2: \u2193 | 3: \u2198 | 4: \u2190 | 5: Stay | 6: \u2192 | 7: \u2196 | 8: \u2191 | 9: \u2197 | Z: Zap | T: Teleport:")
        rep = input("choice: ")
        vrai_rep = self.pos_poss[rep]
        print(rep,vrai_rep)
        return vrai_rep

    def afficher_menu_ini(self):
        print("========================================================")
        print("                      Dalek Game                        ")
        print("========================================================")
        print("1. Start")
        print("2. Quit")
        print("3. LeaderBoard")
        rep = input("votre choix: ")
        return rep

class Controlleur():
    def __init__(self):
        self.partie_en_cours = False
        self.modele = Jeu()
        self.vue = Vue()
        rep = self.vue.afficher_menu_ini()
        rep2 = self.option_partie()
        rep3 = self.difficulte_partie()
        rep4 = self.dimension_partie_x()
        rep5 = self.dimension_partie_y()
        if rep == "1":
            self.modele.creer_partie()
            self.partie_en_cours = True
            if rep2 == "1":
                self.modele.creer_partie()
                self.partie_en_cours = True
                if rep3 == "1":
                    self.modele.creer_partie()
                    self.partie_en_cours = True
                    self.jouer_partie()
            if rep2 == "2":
                self.modele.creer_partie()
                self.partie_en_cours = True
                self.jouer_partie()
        if rep == "2":
            self.partie_en_cours = False


    def option_partie(self):
        print("\n\n\n\n\n\n\n\n========================================================")
        print("                      Dalek Game                        ")
        print("========================================================")
        print("option de la partie")
        print("1. run")
        print("2. run 2")
        rep = input("votre choix: ")
        return rep

    def difficulte_partie(self):
        print("\n\n\n\n\n\n\n\n========================================================")
        print("                      Dalek Game                        ")
        print("========================================================")
        print("Difficulte de la partie")
        print("1. facile")
        print("2. normal")
        print("3. difficile")
        rep = input("votre choix: ")
        return rep

    def dimension_partie_x (self):
        print("\n\n\n\n\n\n\n\n========================================================")
        print("                      Dalek Game                        ")
        print("========================================================")
        print("La hauteur de votre partie")
        rep = input("votre choix: ")
        return rep

    def dimension_partie_y(self):
        print("\nLa largeur de votre partie")
        rep = input("votre choix: ")

    def jouer_partie(self):
        while self.partie_en_cours:
            print('\n')
            print("========================================================")
            print("                      Dalek Game                        ")
            print("========================================================")
            rep = self.vue.afficher_aire_jeu(self.modele.partie)
            self.modele.jouer_coup(rep)


        rep_coup = self.modele.jouer_coup(rep)


if __name__ == "__main__":
    c = Controlleur()






