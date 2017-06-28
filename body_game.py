#! /usr/bin/env python 3
# coding : utf-8

import os					#Allows to interact with the operating system
from tkinter import *

class Labyrinth(object):
    "Class to define a window of the application"
    

    def labyrinth_open(levelFile):
        """Function that tries to open the name.txt of the level
        Returns a custom error message in case of exeption"""
        directory = os.path.dirname(__file__)
        path_to_file = os.path.join(directory,"sprites", levelFile)
        try:
            with open(path_to_file, "r") as f:
                data = f.readlines()
                print(data)	
        except FileNotFoundError as e:
            print("The file was not found !")
            print("Please check that the folder 'sprites' contains 'map_one.txt'")
        except Exception as e:
            raise e
        for i in range(len(data)) :
            data[i] = data[i].strip()
            return data

    def __init__(self,master):
        "Constructor of the main window"
        self.root = master
        self.root.title('Help MacGyver escape !')
        self.labyrinth = Canvas(self.root, width = 1000, height = 1000, bg = 'gray' )
        self.labyrinth.pack(side = TOP, padx = 5, pady = 5)

        "Load sprites"
        self.wall=PhotoImage(file = os.path.join(directory,"sprites", wall.png))
    

if __name__ == "__main__":
    #labyrinth_open('map_one.txt')
    root = Tk()
    labyrinth = Labyrinth(root)
    root.mainloop()

