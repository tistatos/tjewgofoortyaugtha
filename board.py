import random


class Tile:
    """
    Tile Class
    has a value and a position
    """
    def __init__(self, posX, posY):
        self.value = 2 if random.random() < 0.9 else 4
        self.positionX = posX
        self.positionY = posY
        self.merged = False
        pass


class Board:
    """
    Includes game mechanics such as moving tiles and printing the play board
    """
    def __init__(self):
        """
        Initalize board
        """
        self.sizeX = 4
        self.sizeY = 4
        self.tiles = self._createTiles()
        self.moveMade = False
        self.availableTiles = self.sizeX*self.sizeY
        self.running = True
        pass

    def _createTiles(self):
        board = []
        for i in range(self.sizeY):
            a_list = []
            for i in range(self.sizeX):
                a_list.append(None)
            board.append(a_list)
        return board

    def start(self):
        """
        Reset board and generate random tile to start with
        """
        del self.tiles
        self.tiles = self._createTiles()
        self.generateTile()
        # self.printBoard()
        pass

    def generateTile(self):
        """
        generate a tile with either value 2 or 4 on empty position
        """

        y = random.randint(0, self.sizeY-1)
        x = random.randint(0, self.sizeX-1)
        while self.tiles[x][y] is not None:
            x = random.randint(0, self.sizeX-1)
            y = random.randint(0, self.sizeY-1)
        tile = Tile(x, y)
        self.tiles[tile.positionX][tile.positionY] = tile
        self.availableTiles -= 1
        print 'new tile generated at X:', tile.positionX, " Y:", tile.positionY, " Value: " , tile.value
        print 'Available tiles: ', self.availableTiles
        moves = self.availableMoves()
        if moves == 0 and self.availableTiles == 0:
            print 'Game over!'
            self.running = False
        else:
            print 'available moves: ', moves
        pass

    def availableMoves(self):
        moves = 0
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                tile = self.tiles[x][y]
                if tile is None:
                    continue
                else:
                    if x > 1:
                        left = self.tiles[x-1][y]
                        if left is None or left.value == tile.value:
                            moves += 1
                    if x < self.sizeX-1:
                        right = self.tiles[x+1][y]
                        if right is None or right.value == tile.value:
                            moves += 1
                    if y > 1:
                        above = self.tiles[x][y-1]
                        if above is None or above.value == tile.value:
                            moves += 1
                    if y < self.sizeY-1:
                        down = self.tiles[x][y+1]
                        if down is None or down.value == tile.value:
                            moves += 1
        return moves
    def moveUp(self):
        """
        move all tiles upwards
        """
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                tile = self.tiles[x][y]
                if tile is not None:
                    if tile.positionY is not 0:
                        tileAbove = self.tiles[tile.positionX][tile.positionY-1]
                        if tileAbove is None:
                            self.tiles[tile.positionX][tile.positionY] = None
                            tile.positionY -= 1
                            self.tiles[tile.positionX][tile.positionY] = tile
                            self.moveMade = True
                            self.moveUp()
                            return
                        if tileAbove.value == tile.value and not tile.merged:
                            self.tiles[tile.positionX][tile.positionY] = None
                            tile.positionY -= 1
                            tile.value *= 2
                            tile.merged = True
                            self.tiles[tile.positionX][tile.positionY] = tile
                            self.moveMade = True
                            self.availableTiles +=1
                            self.moveUp()
                            return


        self._finishMove(self.moveMade)
        pass

    def moveRight(self):
        for x in reversed(range(self.sizeX)):
            for y in range(self.sizeY):
                tile = self.tiles[x][y]
                if tile is not None:
                    if tile.positionX is not self.sizeX-1:
                        tileRight = self.tiles[tile.positionX+1][tile.positionY]
                        if tileRight is None:
                            self.tiles[tile.positionX][tile.positionY] = None
                            tile.positionX +=1
                            self.tiles[tile.positionX][tile.positionY] = tile
                            self.moveMade = True
                            self.moveRight()
                            return
                        if tileRight.value == tile.value and not tile.merged:
                            self.tiles[tile.positionX][tile.positionY] = None
                            tile.positionX += 1
                            tile.value *= 2
                            tile.merged = True
                            self.tiles[tile.positionX][tile.positionY] = tile
                            self.moveMade = True
                            self.availableTiles +=1
                            self.moveRight()
                            return


        self._finishMove(self.moveMade)
        pass

    def moveDown(self):
        for x in range(self.sizeX):
            for y in reversed(range(self.sizeY)):
                tile = self.tiles[x][y]
                if tile is not None:
                    if tile.positionY is not self.sizeY-1:
                        tileBelow = self.tiles[tile.positionX][tile.positionY+1]
                        if tileBelow is None:
                            self.tiles[tile.positionX][tile.positionY] = None
                            tile.positionY += 1
                            self.tiles[tile.positionX][tile.positionY] = tile
                            self.moveMade = True
                            self.moveDown()
                            return
                        if tileBelow.value == tile.value and not tile.merged:
                            self.tiles[tile.positionX][tile.positionY] = None
                            tile.positionY += 1
                            tile.value *= 2
                            tile.merged = True
                            self.tiles[tile.positionX][tile.positionY] = tile
                            self.moveMade = True
                            self.availableTiles += 1
                            self.moveDown()
                            return

        self._finishMove(self.moveMade)
        pass

    def moveLeft(self):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                tile = self.tiles[x][y]
                if tile is not None:
                    if tile.positionX is not 0:
                        tileLeft = self.tiles[tile.positionX-1][tile.positionY]
                        if tileLeft is None:
                            self.tiles[tile.positionX][tile.positionY] = None
                            tile.positionX -= 1
                            self.tiles[tile.positionX][tile.positionY] = tile
                            self.moveMade = True
                            self.moveLeft()
                            return
                        if tileLeft.value == tile.value and not tile.merged:
                            self.tiles[tile.positionX][tile.positionY] = None
                            tile.positionX -= 1
                            tile.value *= 2
                            tile.merged = True
                            self.tiles[tile.positionX][tile.positionY] = tile
                            self.moveMade = True
                            self.availableTiles +=1
                            self.moveLeft()
                            return

        self._finishMove(self.moveMade)
        pass

    def _finishMove(self, status):
        if status:
            self.moveMade = False
            self.generateTile()
            # self.printBoard()
            for y in range(self.sizeY):
                for x in range(self.sizeX):
                    tile = self.tiles[x][y]
                    if tile is not None:
                        tile.merged = False
        pass
    def printBoard(self):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                val = self.tiles[x][y]
                if val is None:
                    print '0\t',
                else:
                    print val.value, '\t',
            print
        print '-------------'
