#!/usr/bin/python3
# coding : utf-8
from dataGame.labyrinth import *
from tkinter import *
import json

"""
    Program entry point.

    This code allows to instantiate the labyrinth 
    according to variables specific to each level.
"""

if __name__ == '__main__':
    for game_attributes in json.load(open("game_attributes.json")):
        start_game = Labyrinth(**game_attributes)