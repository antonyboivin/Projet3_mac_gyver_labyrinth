#!/usr/bin/python3
# coding : utf-8
from dataGame.labyrinth import *
from tkinter import *
import json

if __name__ == '__main__':
    #start_game = Labyrinth()
    for game_attributes in json.load(open("game_attributes.json")):
        start_game = Labyrinth(**game_attributes)