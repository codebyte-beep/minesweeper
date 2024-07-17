import random
class Board:
    def __init__ (self, dimSize, numBombs):
        self.dim = dimSize
        self.numBombs = numBombs
        self.board = self.create_board(dimSize)
        # for i in self.board:
        #     print(i)
        self.set_blocks_value(dimSize)
# this is simply planting the bombs
    def create_board(self, dimSize):
        list = [[None for i in range(dimSize)] for i in range(dimSize)]
        bombs_planted = 0
        while bombs_planted < self.numBombs:
            random_list = [i for i in range(dimSize**2)]
            site = random.choice(random_list)
            random_list.remove(site)
            list[site//dimSize][site%dimSize] = "*"
            bombs_planted+=1
        return list
# this function will assign the required numeric value to each block by simply counting the number of bombs in its neighbour 
    def set_blocks_value(self, dimSize):
        for row in range(dimSize):
            for col in range(dimSize):
                bombs = 0
                if self.board[row][col] == "*":
                    continue
                # max min ka locha is to prevent row or column from becoming -1 or 10 i.e going out of bounds
                for i in range(max(row-1, 0), min(row+1, self.dim-1)+1):
                    for j in range(max(col-1, 0), min(col+1, self.dim-1)+1):
                        if i == row and j == col:
                            continue 
                        if self.board[i][j] == "*":
                            bombs+=1
                self.board[row][col] = bombs

    def dig(self, row, col, lis):
        if self.board[row][col] == "*":
            lis[row][col] = self.board[row][col]
            return False
        elif self.board[row][col] > 0:
            lis[row][col] = self.board[row][col]
            return True
        
        lis[row][col] = 0
        for i in range(max(row-1, 0), min(row+1, self.dim-1)+1):
            for j in range(max(col-1, 0), min(col+1, self.dim-1)+1):
                if i == row and j == col:
                    continue
                # the below statement is crucial if you don't want to dug the already dug up block, without this statement you might run into an infinite recursion or the no. of recursive steps will increase manifolds unnecessarily and python will throw error: RecursionError: maximum recursion depth exceeded in comparison
                # this statement is similar to line 107 of main.py 
                if lis[i][j] == None:
                    self.dig(i, j, lis)
        return True

    def printBoard(self, lis):
        visible_board = [[None for _ in range(self.dim)] for _ in range(self.dim)]
        for row in range(self.dim):
            for col in range(self.dim):
                if lis[row][col] != None:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        for i in visible_board:
            print(i)
# made another function cuz (other than printBoard) we want to show the whole board in the end if the person loses the game
    def printBoardWhenDefeated(self):
        visible_board = [[None for _ in range(self.dim)] for _ in range(self.dim)]
        for row in range(self.dim):
            for col in range(self.dim):
                    visible_board[row][col] = str(self.board[row][col])
        for i in visible_board:
            print(i)

def play(dimSize, numBombs):
    board = Board(dimSize, numBombs)
    # for i in board.board:
    #     print(i)
    lis = [[None for i in range(dimSize)] for i in range(10)]
    board.printBoard(lis)
    val = True
    while(val):
        ct = 0
        row = int(input("enter row no.: "))
        col = int(input("enter column no.: "))
        if not board.dig(row, col, lis):
            print("GAME OVER :(")
            board.printBoardWhenDefeated()
            break
        else:
            # for i in lis:
            #     print(i)
            board.printBoard(lis)
        # if no. of None in lis = the no. of bombs planted that means congrats you won the game otherwise run the loop again for the next chance
        for i in lis:
            for j in i:
                if j == None:
                    ct+=1
        toggle = lambda x: x > board.dim
        val = toggle(ct)
    if(ct == 10):
        print("CONGRATULATIONS!! MF")
        board.printBoard(lis)
        # for i in board.board:
        #         print(i)
    

if __name__ == "__main__":
    play(10, 10)
    
