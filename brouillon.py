#! /usr/bin/env python 3
# coding : utf-8

import os                   #Allows to interact with the operating system
from tkinter import *
##################################################################################################
class Application:
    "Class to define the window of the application"
    def __init__(self):
        "Constructor of the main window"
        self.window = window 
        self.window.title('Help MacGyver escape !')
        


class Labyrinth:
    "A completer"
    def __init__(self):
        dataLevel = self.labyrinth_open('map_one.txt')
        Application.__init__(self)
        Display.__init__(self, dataLevel)



        

    def labyrinth_open(self, levelFile):
        print("labyrinth_open") ###### Debogage ######
        """Function that tries to open the name.txt of the level
        Returns a custom error message in case of exeption"""
        directory = os.path.dirname(__file__)
        path_to_file = os.path.join(directory, "sprites", levelFile)

        try:
            with open(path_to_file, "r") as f:
                dataLevel = f.readlines()
                 
        except FileNotFoundError as e:
            print("The file was not found !")
            print("Please check that the folder 'sprites' contains 'map_one.txt'")
        except Exception as e:
            raise e

        return dataLevel

class Display:
    def __init__(self, dataLevel):
        dataLevel = Labyrinth.labyrinth_open(self, 'map_one.txt')
        #dataLevel = self.labyrinth_open('map_one.txt')
        print(dataLevel) ###### Debogage ######
        self.labyrinth_display(self, dataLevel)

    def labyrinth_display(self, dataLevel):
        """Fonction that displays the graphic version with the sprites"""
        print("labyrinth_display") ###### Debogage ######
        "Load sprites"
        self.wall=PhotoImage(file = "sprites/wall.png")
        self.floor=PhotoImage(file = "sprites/floor.png")
        self.finish=PhotoImage(file = "sprites/finish.png")
        self.start=PhotoImage(file = "sprites/start.png")
        self.avatar = PhotoImage(file = "sprites/macgyver.png")
        self.guardian = PhotoImage(file = "sprites/guardian.png")

        self.size_sprite = 50

        self.labyrinth = Canvas(window, width = 750, height = 750)
        self.labyrinth.pack(side = TOP, padx = 5, pady = 5)
        

        for i in range(len(dataLevel)) :
            dataLevel[i] = dataLevel[i].strip()
            print(dataLevel[i]) ###### Debogage ######

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
                #start
                if car == "s":
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.start)
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.avatar)
                #Finish
                if car == "f":
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.wall)
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.finish)
                # Initial position MacGyver
                if car == "g":
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.floor)
                    self.labyrinth.create_image(n_col, n_ligne, anchor=NW, image= self.guardian)



                n_col += self.size_sprite
            n_ligne += self.size_sprite
        
    


class MainCharacter:
    "Class to define the MacGyver initial position and move"
    print("MainCharacter") ###### Debogage ######
    def __init__(self, dataLevel):
        pass
        

        
        
        

class Items:
    "Class to define the items"
    def __init__(self):
        # sprite
        # random position
        pass







if __name__ == "__main__":
    window = Tk()
    labyrinth = Labyrinth()
    window.mainloop()