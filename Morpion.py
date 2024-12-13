class Morpion:
    def __init__(self):
        # Initialise le plateau de jeu vide
        self.plateau = [' ' for _ in range(9)]
        self.joueur_actuel = 'X'

    def afficher_plateau(self):
        """Affiche le plateau de jeu"""
        print(f" {self.plateau[0]} | {self.plateau[1]} | {self.plateau[2]} ")
        print("---+---+---")
        print(f" {self.plateau[3]} | {self.plateau[4]} | {self.plateau[5]} ")
        print("---+---+---")
        print(f" {self.plateau[6]} | {self.plateau[7]} | {self.plateau[8]} ")
        print("")

    def est_case_libre(self, position):
        """Vérifie si une case est libre"""
        return self.plateau[position] == ' '

    def faire_un_coup(self, position):
        """Joue un coup pour le joueur actuel"""
        if self.est_case_libre(position):
            self.plateau[position] = self.joueur_actuel
            return True
        return False

    def verifier_victoire(self):
        """Vérifie s'il y a un gagnant"""
        # Combinaisons de victoire
        combinaisons = [
            # Lignes
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Colonnes
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonales
            [0, 4, 8], [2, 4, 6]
        ]

        for combinaison in combinaisons:
            if (self.plateau[combinaison[0]] == self.plateau[combinaison[1]] == self.plateau[combinaison[2]] != ' '):
                return True
        return False

    def est_plateau_plein(self):
        """Vérifie si le plateau est plein"""
        return ' ' not in self.plateau

    def changer_joueur(self):
        """Change le joueur actuel"""
        self.joueur_actuel = 'O' if self.joueur_actuel == 'X' else 'X'

def jouer_morpion():
    """Fonction principale pour jouer au morpion"""
    jeu = Morpion()
    gagnant = False

    print("Jouons au Morpion !")
    print("Les cases sont numérotées de 0 à 8, comme ci dessous :")
    print("")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 ")
    print("")

    while not gagnant and not jeu.est_plateau_plein():
        jeu.afficher_plateau()
        print(f"\nC'est au tour du joueur {jeu.joueur_actuel}")

        try:
            coup = int(input("Entrez le numéro de la case (0-8) : "))
            
            # Vérification de la validité du coup
            if coup < 0 or coup > 8:
                print("Erreur 404. TU dois choisir un chiffre entre 0 et 8.")
                continue

            if jeu.faire_un_coup(coup):
                # Vérifier la victoire
                if jeu.verifier_victoire():
                    jeu.afficher_plateau()
                    print(f"\nLe joueur {jeu.joueur_actuel} a gagné ! 🎉")
                    gagnant = True
                # Vérifier le match nul
                elif jeu.est_plateau_plein():
                    jeu.afficher_plateau()
                    print("\nMatch nul ! 🤝")
                    break
                
                # Changer de joueur
                jeu.changer_joueur()
            else:
                print("Case déjà occupée. Choisis une autre case.")

        except ValueError:
            print("Erreur 404. Tu dois choisir un chiffre entre 0 et 8.")

    # Demander si les joueurs veulent rejouer
    rejouer = input("Une Nouvelle partie ? (oui/non) : ").lower()
    if rejouer == 'oui':
        jouer_morpion()

# Lancer le jeu
if __name__ == "__main__":
    jouer_morpion()