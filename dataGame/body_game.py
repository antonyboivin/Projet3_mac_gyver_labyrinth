#! /usr/bin/env python 3
# coding : utf-8

import os                   #Allows to interact with the operating system
from tkinter import *
import dataGame.character

class Labyrinth:
    "Class to define the window of the application"
    def __init__(self, window):
        "Constructor of the main window"
        self.window = window 
        self.window.title('Help MacGyver escape !')
        data_labyrinth = self.labyrinth_open('map_one.txt')
        self.avatarMove = dataGame.character.Character()
        self.position = self.avatarMove.position
        self.labyrinth_display(data_labyrinth, self.window, self.position)
        self.avatarMove.eventHandler(self.window, self.labyrinth, data_labyrinth, self.position, self.displayAvatar) 



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


    def labyrinth_display(self, dataLevel, window, position):
        print("labyrinth_display")
        "Load sprites"
        self.wall=PhotoImage(file = "dataGame/sprites/wall.png")
        self.floor=PhotoImage(file = "dataGame/sprites/floor.png")
        self.finish=PhotoImage(file = "dataGame/sprites/finish.png")
        self.start=PhotoImage(file = "dataGame/sprites/start.png")
        self.avatar = PhotoImage(file = "dataGame/sprites/macgyver.png")
        self.guardian = PhotoImage(file = "dataGame/sprites/guardian.png")

        self.size_sprite = 50

        
        

        self.labyrinth = Canvas(window, width = 750, height = 750)
        self.labyrinth.pack(side = TOP, padx = 5, pady = 5)


        for i in range(len(dataLevel)) :
            dataLevel[i] = dataLevel[i].strip()
            print(dataLevel[i])

        n_ligne = 0
        for ligne in dataLevel:
            n_col = 0
            for car in ligne :
                
                # Murs
                if car == "w":
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.wall)
                #sols
                if car == "0":
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.floor)
                #start / Initial position of MacGyver
                if car == "s":
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.start)

                #Finish
                if car == "f":
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.wall)
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.finish)
                # 
                if car == "g":
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.floor)
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.guardian)
        

            
                n_col += self.size_sprite
            n_ligne += self.size_sprite

        # Displays the Hero.
        self.displayAvatar =self.labyrinth.create_image(position[0] + position[0] * self.size_sprite,
                                                 position[1] + position[1] * self.size_sprite,
                                                 anchor=NW, image=self.avatar)


"""
if __name__ == "__main__":
    
    window = Tk()
    labyrinth = Labyrinth(window)
    window.mainloop()
    """