import random

class Tile:
    """
    Tile Class
    has a value and a position
    """
    def __init__(self, posX, posY):
        self.value = 2 * random.randint(1,2)
        self.positionX = posX
        self.positionY = posY
        pass

class Board:
    """
    Includes gamemechanics such as moving tiles and priting the play board
    """
    def __init__(self):
        """
        Initalize board
        """
        self.sizeX = 4
        self.sizeY = 4
        self.tiles = [None]*(self.sizeX*self.sizeY)
        self.moveMade = False
        pass

    def start(self):
        """
        Reset board and generate random tile to start with
        """
        self.tiles = [None]*(self.sizeX*self.sizeY)
        self.generateTile()
        board.printBoard()
        pass
    def generateTile(self):
        """
        generate a tile with either value 2 or 4 on empty position
        """
        y = random.randint(0,self.sizeY-1)
        x = random.randint(0,self.sizeX-1)
        while self.tiles[y*(self.sizeY) + x] is not None:
            x = random.randint(0,self.sizeX-1)
            y = random.randint(0,self.sizeY-1)
        tile = Tile(x,y)
        self.tiles[tile.positionY*self.sizeY +  tile.positionX] = tile
        pass
    def moveUp(self):
        for tile in self.tiles:
            if tile is not None:
                if tile.positionY is not 0:
                    tileAbove = self.tiles[(tile.positionY-1)*self.sizeY + tile.positionX]
                    if tileAbove is None:
                        self.tiles[(tile.positionY)*self.sizeY + tile.positionX] = None
                        tile.positionY -= 1
                        self.tiles[(tile.positionY)*self.sizeY + tile.positionX] = tile
                        self.moveMade = True
                        self.moveUp()
                        return
                    if tileAbove.value is tile.value:
                        self.tiles[(tile.positionY)*self.sizeY + tile.positionX] = None
                        tile.positionY -= 1
                        tile.value *= 2
                        self.tiles[(tile.positionY)*self.sizeY + tile.positionX] = tile
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
                    tileLeft = self.tiles[(tile.positionY)*self.sizeY + tile.positionX-1]
                    if tileLeft is None:
                        self.tiles[(tile.positionY)*self.sizeY + tile.positionX] = None
                        tile.positionX -= 1
                        self.tiles[(tile.positionY)*self.sizeY + tile.positionX] = tile
                        self.moveMade = True
                        self.moveLeft()
                        return
                    if tileLeft.value is tile.value:
                        self.tiles[(tile.positionY)*self.sizeY + tile.positionX] = None
                        tile.positionX -= 1
                        tile.value *= 2
                        self.tiles[(tile.positionY)*self.sizeY + tile.positionX] = tile
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
            if newline %self.sizeY is 0:
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
