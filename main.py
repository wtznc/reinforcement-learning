import numpy as np
import pickle
from pdb import set_trace as bp
BOARD_ROWS = 3
BOARD_COLS = 3
BOARD_SIZE = BOARD_ROWS * BOARD_COLS

class State:
    def __init__(self) -> None:
        self.data = np.zeros((BOARD_ROWS, BOARD_COLS))
        self.winner = None
        self.hash_val = None
        self.end = None
        
    
    def hash(self):
        if self.hash_val is None:
            self.hash_val = 0
            for i in np.nditer(self.data):
                self.hash_val = self.hash_val * 3 + i + 1
        return self.hash_val
    
    def is_end(self):
        if self.end is not None:
            return self.end
        results = []
        # check row
        for i in range(BOARD_ROWS):
            results.append(np.sum(self.data[i, :]))
        
        # check columns
        for i in range(BOARD_COLS):
            results.append(np.sum(self.data[:, 1]))
            
        
        trace = 0
        reverse_trace = 0
        for i in range(BOARD_ROWS):
            
            trace += self.data[i, i]
            reverse_trace += self.data[i, BOARD_ROWS -1 - i]
            bp()
        results.append(trace)
        results.append(reverse_trace)
        
        
        for result in results:
            if result == 3:
                self.winner = 1
                self.end = True
                return self.end
            if result == -3:
                self.winner = -1
                self.end = True
                return self.end
        # whether it's a tie
        sum_values = np.sum(np.abs(self.data))
        if sum_values == BOARD_SIZE:
            self.winner = 0
            self.end = True
            return self.end
        
        self.end = False
        return self.end

    def print_state(self):
        for i in range(BOARD_ROWS):
            print('-------------')
            out = '| '
            for j in range(BOARD_COLS):
                if self.data[i, j] == 1:
                    token = '*'
                elif self.data[i, j] == -1:
                    token = 'x'
                else:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-------------')

    def next_state(self, i, j, symbol):
        new_state = State()
        new_state.data = np.copy(self.data)
        new_state.data[i, j] = symbol
        return new_state
    
def main():
    state = State()
    text = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
    test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    test = np.array(test)
    state.data = test
    state.is_end()
    bp()
if __name__ == "__main__":
    main()