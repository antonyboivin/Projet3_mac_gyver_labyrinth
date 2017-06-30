#! /usr/bin/env python 3
# coding : utf-8

import os					#Allows to interact with the operating system
from tkinter import *

class Labyrinth(object):
    "Class to define a window of the application"
    def __init__(self,master):
        "Constructor of the main window"
        self.root = master
        self.root.title('Help MacGyver escape !')
        self.laby = Canvas(self.root, width = 500, height = 500, bg = 'gray' )
        self.laby.pack(side = TOP, padx = 5, pady = 5)
    
        data=[]
        f = open("sprites/map_one.txt")
        data = f.readlines()
        f.close()
        for i in range(len(data)):
            data[i] = data[i].strip()

        print(data)
        

    

if __name__ == "__main__":
    root = Tk()
    laby = Labyrinth(root)
    root.mainloop()
