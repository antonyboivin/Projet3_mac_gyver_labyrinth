#! /usr/bin/env python 3
# coding : utf-8
import random
import dataGame.labyrinth


class Item():
    def __init__(self):
        self.objetbis = ()


    def random_item_position(self, lab, item):
        empty_slot = 0
        possible_slot = []
        n_line = 0 
        for line in lab: 
            n_col = 0 
            for car in line:
                if car == " ":
                    empty_slot += 1
                    possible_slot.append((n_line, n_col))
                n_col += 1
            n_line += 1

        n = 0
        for attr_name in item:
            n += 1
            attr_name = random.sample(possible_slot, 1)

            lab[attr_name[0][0]] = lab[attr_name[0][0]][:attr_name[0][1]] + str(n) + lab[attr_name[0][0]][attr_name[0][1] + 1:]