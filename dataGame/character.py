#! /usr/bin/env python 3
# coding : utf-8
import dataGame.items

"""
    The class Character manages the movements of the character,
    the positional interactions as well as the initialization of the keys.
"""

class Character:
    """
        Initializes interactions related to the position of the character 
        in the labyrinth.
    """    
    def __init__(self, *game_attributes):
        """
            Initializes the attributes of the game :
            self.item1 = "needle", self.item2 = "small plastic tube"...

        """
        self.game_attributes = game_attributes[0]
        n = 0
        self.listItem = []
        for attr_value in self.game_attributes:
            n += 1
            attr_name = "item"
            attr_name = attr_name + str(n)
            self.listItem.append(attr_value)
            setattr(self, attr_name, attr_value)
        self.PickUpItem = []


    def inventory(self, ind, start_game):
        """
            Returns the composition of the inventory 
            according to the objects picked up.

            ind : Index of the picked-up object
            start_game : instance of the game
        """
        self.ind = ind
        self.PickUpItem.append(self.listItem[ind])
        start_game.inventory_List.set(self.PickUpItem)

        
        
    def key_init(self, window, canvas, labyrinth, 
                    characPosition, character, start_game):
        """
            Initializing keyboard behavior

            canvas  : Canvas where to display sprites
            labyrinth     : List containing the labyrinth
            characPosition : Current position of the character
            character   : Sprite representing the character
        """
        window.bind("<Right>", lambda event, can = canvas, l = labyrinth,
                    pos = characPosition, p = character : self.game_move(
                        event, can, "right", l, pos, p, start_game))

        window.bind("<Left>", lambda event, can = canvas, l = labyrinth,
                    pos = characPosition, p = character : self.game_move(
                        event, can, "left", l, pos, p, start_game))

        window.bind("<Up>", lambda event, can = canvas, l = labyrinth,
                    pos = characPosition, p = character : self.game_move(
                        event, can, "up", l, pos, p, start_game))

        window.bind("<Down>", lambda event, can = canvas, l = labyrinth,
                    pos = characPosition, p = character : self.game_move(
                        event, can, "down", l, pos, p, start_game))


        window.bind("<Escape>", lambda event, 
                    fen = window : self.destroy(event, fen))



    def game_move(self, event, can, move, labyrinth, characPosition,
                    character, start_game):
        """
            Moving the Character

            event   : Object describing the event that triggered
                     the call to this function
            can     : Canvas where to display sprites
            move     : Type of movement ("up", "down", "right" or "left")
            labyrinth     : List containing the labyrinth
            characPosition : Current position of the character
            character   : Sprite representing the character
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
        if self.pos_line < 0 or self.pos_col < 0 or self.pos_line > (
                n_line -1) or self.pos_col > (n_col -1):
            return None

        # Management of the guardian's position
        if labyrinth[self.pos_line][self.pos_col] == "$":
                if len(self.PickUpItem) < len(self.listItem):
                    can.delete(start_game.sprite_hero)
                else:
                    can.delete(start_game.guardian)
        
    # Management of the position of objects        
        else:
            i = 0           
            for objet in self.game_attributes:
                #Test if the character moves on an item
                if labyrinth[self.pos_line][self.pos_col] == str(i+1):
                    # Pickup of the item
                    Character.inventory(self, i, start_game)
                    # remove the item discovered
                    can.delete(start_game.item[i])
                    # The position of the item becomes an emplty square
                    labyrinth[self.pos_line] = labyrinth[
                            self.pos_line][:self.pos_col] + " " + labyrinth[
                            self.pos_line][self.pos_col +1:]
                    # The position becomes legal for the move
                    can.coords(character, self.pos_col + self.pos_col * 50,
                            self.pos_line + self.pos_line * 50)
                i += 1

        # Test if movement is possible on an empty square
        if labyrinth[self.pos_line][self.pos_col] == " " or labyrinth[
                    self.pos_line][self.pos_col] == "$":
            can.coords(character, self.pos_col + self.pos_col * 50,
                    self.pos_line + self.pos_line * 50)

            del characPosition[0]
            del characPosition[0]
            characPosition.append(self.pos_col)
            characPosition.append(self.pos_line)

    def destroy(self, event, window):
        """
            Closing the graphic window
            event   : Object describing the event that triggered
                     the call to this function
            window : Graphic window
        """
        window.destroy()