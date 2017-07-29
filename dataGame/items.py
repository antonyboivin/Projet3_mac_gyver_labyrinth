#! /usr/bin/env python 3
# coding : utf-8
import random
import dataGame.labyrinth

"""
    The class Item manages the position of each objects.
"""

class Item():
    """
        The Class manages the alleged position of the objects.
    """
    def __init__(self):
        self.possible_slot = []
        self.empty_slot = 0

    def random_item_position(self, labyrinth, item):
        """
            Determines a random position.

            labyrinth : Variable containing the labyrinth
            item : item of the level attributes
        """
        n_line = 0 
        for line in labyrinth: 
            n_col = 0 
            for car in line:
                if car == " ":
                    self.empty_slot += 1
                    self.possible_slot.append((n_line, n_col))
                n_col += 1
            n_line += 1

        n = 0
        for attr_name in item:
            n += 1
            attr_name = random.sample(self.possible_slot, 1)

            labyrinth[attr_name[0][0]] = labyrinth[attr_name[
                    0][0]][:attr_name[0][1]] + str(n) + labyrinth[
                    attr_name[0][0]][attr_name[0][1] + 1:]