#! /usr/bin/env python 3
# coding : utf-8
import dataGame.items

class Character:
    def __init__(self):
        # Instantiation of the Item class
        self.itemInGame = dataGame.items.Item()

    def key_init(self, window, canvas, lab, characPosition, character, start_game):
        """
            Initialisation du comportement des touches du clavier

            canvas  : canevas où afficher les sprites
            lab     : liste contenant le labyrinthe
            characPosition : position courante du personnage
            perso   : sprite représentant le personnage

            Pas de valeur de retour
        """
        window.bind("<Right>", lambda event, can = canvas, l = lab,
                    pos = characPosition,
                    p = character : self.game_move(event, can, "right", l, pos, p, start_game))

        window.bind("<Left>", lambda event, can = canvas, l = lab,
                    pos = characPosition,
                    p = character : self.game_move(event, can, "left", l, pos, p, start_game))

        window.bind("<Up>", lambda event, can = canvas, l = lab,
                    pos = characPosition,
                    p = character : self.game_move(event, can, "up", l, pos, p, start_game))

        window.bind("<Down>", lambda event, can = canvas, l = lab,
                    pos = characPosition,
                    p = character : self.game_move(event, can, "down", l, pos, p, start_game))


        window.bind("<Escape>", lambda event, fen = window : self.destroy(event, fen))



    def game_move(self, event, can, move, lab, characPosition, character, start_game):
        """
            deplacement du personnage

            event   : objet décrivant l'événement ayant déclenché
                                        l'appel à cette fonction
            can     : canevas où afficher les sprites
            move     : type de déplacemnt ("up", "down", "right" ou "left") #dep
            lab     : liste contenant le labyrinthe
            characPosition : position courante du personnage
            perso   : sprite représentant le personnage

            Pas de valeur de retour
        """
        # Calculation of the size of the labyrinth
        n_col = len(lab[0])
        n_line = len(lab)
        self.pos_col, self.pos_line = [characPosition[0], characPosition[1]]
        # Moving to the right
        if move == "right":
            self.pos_col += 1
        # Moving to the left :
        elif move == "left":
            self.pos_col -= 1
        # Moving to the top  :
        elif move == "up":
            self.pos_line -= 1
        # Moving to the bottom :
        elif move == "down":
            self.pos_line += 1

        # Tests if moving leads outside the playing area
        if self.pos_line < 0 or self.pos_col < 0 or self.pos_line > (n_line -1) or self.pos_col > (n_col -1):
            return None

            # Une position hors labyrinthe indique la victoire
        if lab[self.pos_line][self.pos_col] == "O":
                return [-1,-1]
###############################################################################
        elif lab[self.pos_line][self.pos_col] == "1" or lab[self.pos_line][self.pos_col] == "2" or lab[self.pos_line][self.pos_col] == "3":
            if lab[self.pos_line][self.pos_col] == "1":
               can.delete(start_game.item1)
            elif lab[self.pos_line][self.pos_col] == "2":
               can.delete(start_game.item2)
            elif lab[self.pos_line][self.pos_col] == "3":
               can.delete(start_game.item3) 
                

        # Teste si le personnage se déplace sur un trésor
    # Découverte d'un trésor
    # Fonction qui calcul le montant d'un butin
        
    # On supprime le trésor découvert
            lab[self.pos_line] = lab[self.pos_line][:self.pos_col] + " " + lab[self.pos_line][self.pos_col +1:]
            can.coords(character, self.pos_col + self.pos_col * 50, self.pos_line + self.pos_line * 50)

            
        ######################################################################################

        # Test if movement is possible on an empty square
        if lab[self.pos_line][self.pos_col] == " ":
            can.coords(character, self.pos_col + self.pos_col * 50, self.pos_line + self.pos_line * 50)

            del characPosition[0]
            del characPosition[0]
            characPosition.append(self.pos_col)
            characPosition.append(self.pos_line)

    def destroy(self, event, window):
        """
            Fermeture de la window graphique

            event    : objet décrivant l'événement ayant déclenché
                                        l'appel à cette fonction
            window : Fenêtre graphique

            Pas de valeur de retour
        """
        window.destroy()