#! /usr/bin/env python 3
# coding : utf-8
import dataGame.items


class Character:
    def __init__(self, *game_attributes):
        self.game_attributes = game_attributes[0]
        n = 0
        self.listItem = []
        for attr_value in self.game_attributes:
            n += 1
            attr_name = "item"
            attr_name = attr_name + str(n)
            self.listItem.append(attr_value)
            setattr(self, attr_name, attr_value)
        print(self.item1,self.item2,self.item3)
        self.PickUpItem = []
        print(self.PickUpItem)

        #self.item1 = "needle"
        #self.item2 = "small plastic tube"
        #self.item3 = "ether"

    def inventory(self, ind, start_game):
        self.ind = ind
        #self.PickUpItem = "item" + str(ind +1)
        self.PickUpItem.append(self.listItem[ind])
        start_game.inventory_List.set(self.PickUpItem)

        
        
    

    def key_init(self, window, canvas, labyrinth, characPosition, character, start_game):
        """
            Initialisation du comportement des touches du clavier

            canvas  : canevas où afficher les sprites
            lab     : liste contenant le labyrinthe
            characPosition : position courante du personnage
            perso   : sprite représentant le personnage

            Pas de valeur de retour
        """
        window.bind("<Right>", lambda event, can = canvas, l = labyrinth,
                    pos = characPosition,
                    p = character : self.game_move(event, can, "right", l, pos, p, start_game))

        window.bind("<Left>", lambda event, can = canvas, l = labyrinth,
                    pos = characPosition,
                    p = character : self.game_move(event, can, "left", l, pos, p, start_game))

        window.bind("<Up>", lambda event, can = canvas, l = labyrinth,
                    pos = characPosition,
                    p = character : self.game_move(event, can, "up", l, pos, p, start_game))

        window.bind("<Down>", lambda event, can = canvas, l = labyrinth,
                    pos = characPosition,
                    p = character : self.game_move(event, can, "down", l, pos, p, start_game))


        window.bind("<Escape>", lambda event, fen = window : self.destroy(event, fen))



    def game_move(self, event, can, move, labyrinth, characPosition, character, start_game):
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
        n_col = len(labyrinth[0])
        n_line = len(labyrinth)
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

            # Gestion du gardien
        if labyrinth[self.pos_line][self.pos_col] == "$":
                if len(self.PickUpItem) < len(self.listItem):
                    print("perdu")
                    can.delete(start_game.sprite_hero)
                else:
                    print("gagné")
                    can.delete(start_game.guardian)
        
    # gestion des objets
    # Test si le personnage se déplace sur un trésor
    # Découverte d'un trésor        
    # On supprime le trésor découvert
        else:
            i = 0           
            for objet in self.game_attributes:
                if labyrinth[self.pos_line][self.pos_col] == str(i+1):
                    Character.inventory(self, i, start_game)
                    can.delete(start_game.item[i])

                    labyrinth[self.pos_line] = labyrinth[self.pos_line][:self.pos_col] + " " + labyrinth[self.pos_line][self.pos_col +1:]
                    can.coords(character, self.pos_col + self.pos_col * 50, self.pos_line + self.pos_line * 50)
                i += 1

        # Test if movement is possible on an empty square
        if labyrinth[self.pos_line][self.pos_col] == " " or labyrinth[self.pos_line][self.pos_col] == "$":
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