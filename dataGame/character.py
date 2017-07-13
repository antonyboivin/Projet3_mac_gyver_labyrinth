
class Character:
    def __init__(self):
        self.position = [2, 1]
        

    """def move(self, event, can, level, position, avatar, move):
        print("def move")
        n_cols = len(level[0])
        n_lignes = len(level)
        self.pos_col, self.pos_ligne = [self.position[0], self.position[1]]
        # Right move
        if move == "right":
            self.pos_col += 1
        # left move
        elif move == "left":
            self.pos_col -= 1
        # up move
        elif move == "up":
            self.pos_ligne -= 1
        # down move
        elif move == "down":
            self.pos_ligne += 1
        # test sortie de plateau
        if self.pos_ligne < 0 or self.pos_col < 0 or self.pos_ligne > (n_lignes - 1) or self.pos_col > (n_cols - 1):
            return None
        # test presence objet


        # test si deplacement possible sur une case vide
        elif level[self.pos_ligne][self.pos_col] == "0":
            can.coords(avatar, self.pos_col + self.pos_col * 50, self.pos_ligne + self.pos_ligne * 50)
            del self.pos_hero[0]
            del self.pos_hero[0]
            pos_hero.append(self.pos_col)
            pos_hero.append(self.pos_ligne)

            level[self.pos_ligne] = level[self.pos_ligne][:self.pos_col] + "0" + level[self.pos_ligne][self.pos_col + 1:]

            return [self.pos_col, self.pos_ligne]"""



    def eventHandler(self, event, window, position, avatar, level):
        print("def eventHandler")
        window.bind("<Right>",
                    lambda event, can=window, l=level, pos=position, p=avatar: self.move(event, can, "right",
                                                                                          l,
                                                                                          pos, p)) #, game_treasures, game))
        window.bind("<Left>",
                    lambda event, can=window, l=level, pos=position, p=avatar: self.move(event, can, "left",
                                                                                          l,
                                                                                          pos, p)) #, game_treasures, game))
        window.bind("<Up>",
                    lambda event, can=window, l=level, pos=position, p=avatar: self.move(event, can, "up", l,
                                                                                          pos,
                                                                                          p)) #, game_treasures, game))
        window.bind("<Down>",
                    lambda event, can=window, l=level, pos=position, p=avatar: self.move(event, can, "down",
                                                                                          l,
                                                                                          pos, p)) #, game_treasures, game))
        window.bind("<Escape>", lambda event, fen=window: self.destroy(event, fen))

    