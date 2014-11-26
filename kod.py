import random

class Tile:
    def __init__(self, posX, posY):
        self.value = 2 * random.randint(1,2)
        self.positionX = posX
        self.positionY = posY
        pass

class Board:
    def __init__(self):
        self.size = (3,3)
        self.tiles = [None]*9
        self.moveMade = False
        pass
    def start(self):
        self.tiles = [None]*9
        self.generateTile()
        board.printBoard()
        pass
    def generateTile(self):
        x = random.randint(0,2)
        y = random.randint(0,2)
        while self.tiles[x*3 + y] is not None:
            x = random.randint(0,2)
            y = random.randint(0,2)
        tile = Tile(x,y)
        self.tiles[tile.positionY*3 + tile.positionX] = tile
        pass
    def moveUp(self):
        for tile in self.tiles:
            if tile is not None:
                if tile.positionY is not 0:
                    tileAbove = self.tiles[(tile.positionY-1)*3 + tile.positionX]
                    if tileAbove is None:
                        self.tiles[(tile.positionY)*3 + tile.positionX] = None
                        tile.positionY -= 1
                        self.tiles[(tile.positionY)*3 + tile.positionX] = tile
                        self.moveMade = True
                        self.moveUp()
                        return
                    if tileAbove.value is tile.value:
                        self.tiles[(tile.positionY)*3 + tile.positionX] = None
                        tile.positionY -= 1
                        tile.value *= 2
                        self.tiles[(tile.positionY)*3 + tile.positionX] = tile
                        self.moveMade = True
                        self.moveUp()
                        return
        if self.moveMade:
            self.generateTile()
            self.moveMade = False
        print 'up'
        board.printBoard()
        pass
    def moveRight(self):

        pass
    def moveDown(self):
        pass
    def moveLeft(self):
        for tile in self.tiles:
            if tile is not None:
                if tile.positionX is not 0:
                    tileLeft = self.tiles[(tile.positionY)*3 + tile.positionX-1]
                    if tileLeft is None:
                        self.tiles[(tile.positionY)*3 + tile.positionX] = None
                        tile.positionX -= 1
                        self.tiles[(tile.positionY)*3 + tile.positionX] = tile
                        self.moveMade = True
                        self.moveLeft()
                        return
                    if tileLeft.value is tile.value:
                        self.tiles[(tile.positionY)*3 + tile.positionX] = None
                        tile.positionX -= 1
                        tile.value *= 2
                        self.tiles[(tile.positionY)*3 + tile.positionX] = tile
                        self.moveMade = True
                        self.moveLeft()
                        return
        if self.moveMade:
            self.generateTile()
            self.moveMade = False
        print 'left'
        board.printBoard()
        pass
    def printBoard(self):
        newline = 0
        for tile in self.tiles:
            if newline %3 is 0:
                print ''
            newline += 1
            if tile is None:
                print "0",
            else:
                print tile.value,
        print
        print '-------------'



board = Board()
print 'start'
board.start()

board.moveLeft()
board.moveUp()
board.moveLeft()
board.moveUp()
board.moveLeft()
board.moveUp()
