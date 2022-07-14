import random

# see the picture of the game to understand these
rules = {
    3:19,
    9:11,
    14:30,
    15:7,
    17:36,
    20:42,
    26:35,
    34:97,
    38:57,
    50:32,
    59:79,
    64:78,
    68:48,
    70:72,
    77:98,
    92:74,
    100:82,
    103:96,
    107:23,
    108:114,
    112:91,
    116:105,
    119:101
};

NO_GAMES = 1_000_000

class Game:
    FINAL_TILE = 120

    def __init__(self):
        # we assume that your meeple/button is on tile no 1
        self.pos = 1
        self.actualMoves = []

    def makeMove(self, noTiles):
        # if we make a move and this move lands pass the final
        # tile with no 120 then we go back as many tiles as it
        # passed the final tile
        if (self.pos + noTiles > Game.FINAL_TILE):
            self.pos = Game.FINAL_TILE - ((self.pos + noTiles) - Game.FINAL_TILE)
        else:
            self.pos = self.pos + noTiles
        
        self.actualMoves.append(noTiles)
        # if we have a jump/fall then we need to execute that
        if self.pos in rules:
            self.pos = rules[self.pos]

    def isGameFinished(self):
        if self.pos == Game.FINAL_TILE:
            return True
        else:
            return False

if __name__ == "__main__":
    noGames = 0

    while(True):
        game = Game()
        noMoves = 1
        while(True):
            n = random.randint(1,6)
            game.makeMove(n)
            noMoves = noMoves + 1
            if game.isGameFinished():
                break

        noGames = noGames + 1
        print(noMoves)
        if noGames >= NO_GAMES:
            break
