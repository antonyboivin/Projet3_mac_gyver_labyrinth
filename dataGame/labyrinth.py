#! /usr/bin/env python 3
# coding : utf-8
import os
import random
from tkinter import *
import dataGame.character
import dataGame.items


class Labyrinth:
    def __init__(self):
        # Initializing the graphic display
        self.window = Tk()
        self.window.title("Help MacGyver to escape !")
        self.size_sprite = 50
        self.introduction = Label(self.window, text="Good Luck !",
                                 font='Arial 20').pack()

        # Instantiation of the Item class
        self.itemInGame = dataGame.items.Item()

        # Initialization of character data
        self.characPosition = [1,1]
        self.characData = self.characData ### debug ###
        self.carac_data = Label(self.window, text="item1 : {}   item2 : {:}  item3 : {:}".
                                        format(self.characData["item1"], 
                                        self.characData["item2"], self.characData["item3"]),
                                        font='Arial 20').pack(side = LEFT)

        # Instantiation of the Character class
        self.moveInGame = dataGame.character.Character()

        

        # Launch of the game
        self.level = self.load_labyrinth("level_1")
        (self.canvas, self.sprite_perso, self.pictures) = self.display_labyrinth(self.level, self.window,\
                                                 self.size_sprite, self.characPosition)
        self.moveInGame.key_init(self.window, self.canvas, self.level, self.characPosition, self.sprite_perso, self)
        
        # Event loop
        self.window.mainloop()



    def load_labyrinth(self, name):
        """
            Charge le labyrinthe depuis le fichier name.txt

            name : name du fichier contenant le labyrinthe (sans l'extension .txt)

            Valeur de retour : Une liste contenant les données du labyrinthe
        """
        # Reading the data in the file
        directory = os.path.dirname(__file__)
        path_to_file = os.path.join(directory, "../dataGame", name)
        
        try:
            fil = open(path_to_file +".txt", "r")
            self.dataFile = fil.readlines()
            fil.close()
        except FileNotFoundError as e:
            print("The file was not found !")
            print("Please check that the folder /dataGame contains {}.txt ".format(name))
            os._exit(1)
        except Exception as e:
            raise e
            os._exit(1)

        # Browse the list to remove invisible characters
        for i in range(len(self.dataFile)):
            self.dataFile[i] = self.dataFile[i].strip()
        return self.dataFile




    def display_labyrinth(self, lab, window, size_sprite, characPosition):
        """
            Affichage d'un labyrinthe

            lab : Variable contenant le labyrinthe
            window : Fenêtre graphique
            size_sprite : Taille des sprites en pixels
            characPosition : liste contenant la position du personnage
                        [colonne, ligne]

            Valeur de retour :
                Tuple contenant le canevas, le sprite du personnage et
                un dictionnaire des images utilisées pour les sprites
        """
        self.can = Canvas(window, width = 764, height = 764)
        
        self.picture_wall=PhotoImage(file = "sprites/wall.png")
        self.picture_floor=PhotoImage(file = "sprites/floor.png")
        self.picture_exit=PhotoImage(file = "sprites/exit.png")
        self.picture_start=PhotoImage(file = "sprites/start.png") #manque
        self.picture_hero = PhotoImage(file = "sprites/macgyver.png")
        self.picture_guardian = PhotoImage(file = "sprites/guardian.png")
        self.picture_item = PhotoImage(file = "sprites/item.png")

        # Calling the class method that indicates the position of the items
        self.itemInGame.random_item_position(self.level)
        
        n_line = 0
        for line in lab:
            n_cols = 0
            for car in line :
                # Floor display
                if car == " ":
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_floor)
                # Wall display
                elif car == "+" or car == "-" or car == "|":
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_wall)
                
                # Items display
                elif car == "1" : 
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_floor)
                    self.item1 = self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_item)

                elif car == "2" : 
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_floor)
                    self.item2 = self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_item)

                elif car == "3" : 
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_floor)
                    self.item3 = self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_item)
                # Guardian display
                elif car == "$":
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_floor)
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_guardian)
                # Exit display
                elif car == "O":
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_floor)
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                    n_line + n_line*self.size_sprite, anchor = NW,
                                    image = self.picture_exit)
                n_cols += 1
            n_line += 1

         # Character display
        self.sprite_hero = self.can.create_image(characPosition[0] + characPosition[0] * self.size_sprite,
                                        characPosition[1] + characPosition[1] * self.size_sprite,
                                        anchor=NW, image=self.picture_hero)
        self.can.pack()


        return (self.can, self.sprite_hero, {
            "hero"  : self.picture_hero,
            "wall"  : self.picture_wall,
            "floor" : self.picture_floor,
            "item": self.picture_item,
            "ennemy"  : self.picture_guardian,
            "exit"    : self.picture_exit})