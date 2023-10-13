import copy
import math

class TicTacToe():
    def __init__(self, state=[[0,0,0],[0,0,0],[0,0,0]]):
        self.state = state
        self.isMaxPlayer = True

    def make_move(self, row, col, val):
        if (isinstance(row, int)) and (row>=0) and (row<=2):
            if (isinstance(col, int)) and (col>=0) and (col<=2):
                if self.state[row][col] == 0:
                    if (val == -1) or (val == 1):
                        self.state[row][col] = val
                        return True
        return False
    
    def try_move(state, row, col, val):
        if (isinstance(row, int)) and (row>=0) and (row<=2):
            if (isinstance(col, int)) and (col>=0) and (col<=2):
                if state[row][col] == 0:
                    if (val == -1) or (val == 1):
                        state[row][col] = val

        return state
    
    def minimax(self, state, depth, isMaxPlayer): 
        if depth == 0 or self.terminal_node(state)["gameover"]:
            return self.terminal_node(state)["result"]
        
        if isMaxPlayer:
            maxEval = -math.inf
            for pos in self.expand_state(state):
                state[pos[0]][pos[1]] = 1
                eval = self.minimax(state, depth-1, False)
                state[pos[0]][pos[1]] = 0  # undo the move
                maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = math.inf
            for pos in self.expand_state(state):
                state[pos[0]][pos[1]] = -1
                eval = self.minimax(state, depth-1, True)
                state[pos[0]][pos[1]] = 0
                minEval = min(minEval, eval)
            return minEval

    def terminal_node(self, state):
        result = 0
        isGameOver = False
    
        emptyCells = False
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    emptyCells = True

        isWinner = False
        for i in range(3):
            sum_p1 = 0
            sum_p2 = 0
            for j in range(3):
                if state[i][j] == 1:
                    sum_p1 += 1
                if state[i][j] == -1:
                    sum_p2 += -1
            if (sum_p1 == 3) or (sum_p2 == -3):
                isWinner = True 
                if (sum_p1 == 3):
                    result = 10
                if (sum_p2 == -3):
                    result = -10

        for j in range(3):
            sum_p1 = 0
            sum_p2 = 0
            for i in range(3):
                if state[i][j] == 1:
                    sum_p1 += 1
                if state[i][j] == -1:
                    sum_p2 += -1
            if (sum_p1 == 3) or (sum_p2 == -3):
                isWinner = True 
                if (sum_p1 == 3):
                    result = 10
                if (sum_p2 == -3):
                    result = -10

        sum_p1 = 0
        sum_p2 = 0
        for i in range(3):
            if state[i][i] == 1:
                sum_p1 += 1
            if state[i][i] == -1:
                sum_p2 += -1
        if (sum_p1 == 3) or (sum_p2 == -3):
            isWinner = True 
            if (sum_p1 == 3):
               result = 10
            if (sum_p2 == -3):
               result = -10
            
        sum_p1 = 0
        sum_p2 = 0
        for i in range(3):
            if state[i][2-i] == 1:
                sum_p1 += 1
            if state[i][2-i] == -1:
                sum_p2 += -1
        if (sum_p1 == 3) or (sum_p2 == -3):
            isWinner = True 
            if (sum_p1 == 3):
               result = 10
            if (sum_p2 == -3):
               result = -10

        isGameOver = isWinner or not emptyCells
        return {"gameover": isGameOver, "result": result}
    
    def expand_state(self, state):
        positions = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    positions.append((i, j))
        return positions

    
    def computer_move(self):
        best_move = None
        best_value = -math.inf
        depth = len(self.expand_state(self.state))  
        
        for pos in self.expand_state(self.state):
            temp_state = copy.deepcopy(self.state)
            temp_state[pos[0]][pos[1]] = 1
            move_value = self.minimax(temp_state, depth, False)
            
            if move_value > best_value:
                best_value = move_value
                best_move = pos
                
        self.state[best_move[0]][best_move[1]] = 1

    def display_board(self):
        for row in self.state:
            print(row)

    def play_game(self):
        while not self.terminal_node(self.state)["gameover"]:
            self.display_board()
            if self.isMaxPlayer: 
                print("Computer's move:")
                self.computer_move()
                self.isMaxPlayer = not self.isMaxPlayer 
            else:
                move_made = False
                while not move_made:
                    row = input("Enter row (0, 1, or 2): ")
                    col = input("Enter col (0, 1, or 2): ")
                    if row.isdigit() and col.isdigit():  
                        move_made = self.make_move(int(row), int(col), -1)
                        if move_made:
                            self.isMaxPlayer = not self.isMaxPlayer  
                    if not move_made:
                        print("Invalid move. Please try again.")
                    
        self.display_board()
        result = self.terminal_node(self.state)["result"]
        if result == 10:
            print("Computer wins!")
        elif result == -10:
            print("You win!")
        else:
            print("It's a tie!")

game = TicTacToe()
game.play_game()

    



