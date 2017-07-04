#! /usr/bin/env python 3
# coding : utf-8

import os                   #Allows to interact with the operating system
from tkinter import *

class Labyrinth:
    "Class to define a window of the application"
    def __init__(self, window):
        "Constructor of the main window"
        self.window = window 
        self.window.title('Help MacGyver escape !')
        data_labyrinth = self.labyrinth_open('map_one.txt')
        self.labyrinth_display(data_labyrinth, self.window)



    def labyrinth_open(self, levelFile):
        print("labyrinth_open")
        """Function that tries to open the name.txt of the level
        Returns a custom error message in case of exeption"""
        directory = os.path.dirname(__file__)
        path_to_file = os.path.join(directory, "sprites", levelFile)

        try:
            with open(path_to_file, "r") as f:
                data = f.readlines()
                 
        except FileNotFoundError as e:
            print("The file was not found !")
            print("Please check that the folder 'sprites' contains 'map_one.txt'")
        except Exception as e:
            raise e

        return data


    def labyrinth_display(self, dataLevel, window):
        print("labyrinth_display")
        "Load sprites"
        self.wall=PhotoImage(file = "sprites/wall.gif")

        self.largeur_block = 50
        self.hauteur_block = 50                                     #un bloc fait 40 px
        self.nb_blocs = 15                                          #succession de 15 blocs cote à cote
        self.centre = self.largeur_block /2                         #le centre se trouve au milieu d'un bloc
        self.ligne = self.nb_blocs * self.largeur_block
        self.colonne = self.nb_blocs * self.hauteur_block
        self.size_sprite = 50

        self.labyrinth = Canvas(window, width = 750, height = 750)
        self.labyrinth.pack(side = TOP, padx = 5, pady = 5)
        #self.labyrinth.create_image(0, 0, anchor=NW, image= self.wall)
        #self.labyrinth.create_image(0, 0, image= self.wall)
        #self.labyrinth.create_image.pack()

        for i in range(len(dataLevel)) :
            dataLevel[i] = dataLevel[i].strip()
            print(dataLevel[i])

        n_ligne = 0
        for ligne in dataLevel:
            n_col = 0
            n_ligne += self.size_sprite
            for car in ligne :
                n_col += self.size_sprite
                # Murs
                if car == "w":
                    self.labyrinth.create_image(n_col-50, n_ligne-50, anchor=NW, image= self.wall)

                    
                    
                    


        self.labyrinth.pack()



if __name__ == "__main__":
    
    window = Tk()
    labyrinth = Labyrinth(window)
    window.mainloop()
