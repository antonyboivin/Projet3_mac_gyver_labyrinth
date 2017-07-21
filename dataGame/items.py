#! /usr/bin/env python 3
# coding : utf-8
import random

class Item():
    def __init__(self):
        self.itemList = [0, 0, 0]

    def random_item_position(self, lab):
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

        item1, item2, item3 = random.sample(possible_slot, 3)

        lab[item1[0]] = lab[item1[0]][:item1[1]] + "1" + lab[item1[0]][item1[1] + 1:]
        lab[item2[0]] = lab[item2[0]][:item2[1]] + "2" + lab[item2[0]][item2[1] + 1:]
        lab[item3[0]] = lab[item3[0]][:item3[1]] + "3" + lab[item3[0]][item3[1] + 1:]
    
    def inventory(self, item_name, start_game):
        
        self.characData = {
            "item1" : 0,
            "pv" : 25,
            "level" : None
        }
        self.inventory={
            "item1" : 0,
            "item2" : 0,
            "item3" : 0
        }
        if item_name == start_game.item1:
            self.itemList[0] = 1
            self.inventory["item1"] = "needle"
            start_game.characData(self.inventory)
            
        elif item_name == start_game.item2:
            self.itemList[1] = 2
            self.inventory["item2"] = "small plastic tube"
        else :
            self.itemList[2] = 3
            self.inventory["item2"] = "ether"