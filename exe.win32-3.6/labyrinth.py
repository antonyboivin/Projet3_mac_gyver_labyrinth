#! /usr/bin/env python 3
# coding : utf-8

"""
    The Labyrinth class will load the provided level as a
     parameter, and then manage its display throughout the game.
"""

import os
import random
from tkinter import *
import dataGame.character
import dataGame.items



class Labyrinth:
    """
        This class allows you to instantiate objects of other classes.
        It manages the graphical display of the window containing the game.
        It manages the graphical display of the game.
    """
    def __init__(self, **game_attributes):
        """
            Display :
                -window : titre, instruction
                -required items
                -Inventory
            Define :
                -data level : characteristic of the level
                            (required item, initial position, current level)
            Instantiate : Instantiates an object of the Item and Character class
        """

        # Initializing the graphical display of the window
        self.window = Tk()
        self.window.title("Help MacGyver to escape !")
        self.size_sprite = 50
        self.introduction = Label(self.window,
                                  text="Help Mac escape from the labyrinth !",
                                  font='Arial 20', fg="red").grid(
                                      row=0, column=1, columnspan=3)

        # Initialization of level data
        for attr_name, attr_value in game_attributes.items():
            setattr(self, attr_name, attr_value)

        # Display the required item
        self.required_Item = Label(self.window, text="To escape, Mac must find \n\
all of the following objects : \n {}".format(self.item[0:]),
                                   font='Arial 12', bg="black",
                                   fg="white").grid(row=4, sticky='n')

        # Instantiation of the Item class
        self.itemInGame = dataGame.items.Item()

        # Display the inventory
        self.inventoryList = StringVar()
        self.label1 = Label(self.window, text="This your inventory :\n",
                            font='Arial 12',
                            fg="brown").grid(row=5, sticky='s')
        self.label2 = Label(self.window, textvariable=self.inventoryList,
                            font='Arial 10',
                            fg="black").grid(row=5, sticky='s')
        self.inventoryList.set("Empty for the moment")


        # Instantiation of the Character class
        self.moveInGame = dataGame.character.Character(game_attributes["item"])

        # Launch of the game
        self.level = self.load_labyrinth(self.current_level)
        (self.canvas, self.sprite_perso, self.pictures) = self.display_labyrinth(
            self.level, self.window,
            self.size_sprite, self.characPosition)
        self.moveInGame.key_init(self.window, self.canvas, self.level,
                                 self.characPosition, self.sprite_perso, self)

        # Event loop
        self.window.mainloop()

    def load_labyrinth(self, name):
        """
            Loads the labyrinth from file name.txt
            Name: name of the file containing the labyrinth
                    (without the extension .txt)
            Return value: A list containing the labyrinth data
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
            print("Please check that the folder /dataGame contains {}.txt ".
                  format(name))
            os._exit(1)
        except Exception as e:
            raise e
            os._exit(1)

        # Browse the list to remove invisible characters
        for i in range(len(self.dataFile)):
            self.dataFile[i] = self.dataFile[i].strip()
        return self.dataFile

    def display_labyrinth(self, labyrinth, window, size_sprite, characPosition):
        """
            Viewing a labyrinth
            Lab: Variable containing the labyrinth
            Window: Graphic window
            Size_sprite: Size of sprites in pixels
            CharacPosition: list containing the position of the character
                        [Column, line]
            Return Value:
                Tuple containing the canvas, the sprite of the character and
                a dictionary of images used for sprites
        """
        self.can = Canvas(window, width=764, height=764)
        self.picture_wall = PhotoImage(file="sprites/wall.png")
        self.picture_floor = PhotoImage(file="sprites/floor.png")
        self.picture_exit = PhotoImage(file="sprites/exit.png")
        self.picture_hero = PhotoImage(file="sprites/macgyver.png")
        self.picture_guardian = PhotoImage(file="sprites/guardian.png")
        self.picture_item = PhotoImage(file="sprites/item.png")

        # Calling the class method that indicates the position of the items
        self.itemInGame.random_item_position(self.level, self.item)

        n_line = 0
        for line in labyrinth:
            n_cols = 0
            for car in line:
                # Floor display
                if car == " ":
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                          n_line + n_line*self.size_sprite,
                                          anchor=NW, image=self.picture_floor)
                # Wall display
                elif car == "+" or car == "-" or car == "|":
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                          n_line + n_line*self.size_sprite,
                                          anchor=NW, image=self.picture_wall)
                # Guardian display
                elif car == "$":
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                          n_line + n_line*self.size_sprite,
                                          anchor=NW, image=self.picture_floor)
                    self.guardian = self.can.create_image(
                        n_cols + n_cols*self.size_sprite,
                        n_line + n_line*self.size_sprite, anchor=NW,
                        image=self.picture_guardian)
                # Exit display
                elif car == "O":
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                          n_line + n_line*self.size_sprite,
                                          anchor=NW, image=self.picture_floor)
                    self.can.create_image(n_cols + n_cols*self.size_sprite,
                                          n_line + n_line*self.size_sprite,
                                          anchor=NW, image=self.picture_exit)
                # Display items
                else:
                    i = 0
                    for objet in self.item:
                        if car == str(i+1):
                            self.can.create_image(
                                n_cols + n_cols*self.size_sprite,
                                n_line + n_line*self.size_sprite,
                                anchor=NW, image=self.picture_floor)
                            self.item[i] = self.can.create_image(
                                n_cols + n_cols*self.size_sprite,
                                n_line + n_line*self.size_sprite,
                                anchor=NW, image=self.picture_item)
                        i += 1

                n_cols += 1
            n_line += 1

         # Character display
        self.sprite_hero = self.can.create_image(
            characPosition[0] + characPosition[0] * self.size_sprite,
            characPosition[1] + characPosition[1] * self.size_sprite,
            anchor=NW, image=self.picture_hero)

        self.can.grid(row=1, column=2, columnspan=2, rowspan=15)

        return (self.can, self.sprite_hero, {
            "hero"  : self.picture_hero,
            "wall"  : self.picture_wall,
            "floor" : self.picture_floor,
            "item": self.picture_item,
            "ennemy"  : self.picture_guardian,
            "exit"    : self.picture_exit})
