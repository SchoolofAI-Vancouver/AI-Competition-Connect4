import numpy as np
import random
from copy import copy
from utils import *        

class Connect4:

    def __init__(self, size=(7, 6), N=4):
        self.size = size
        self.w, self.h = size
        self.N = N

        # make sure game is well defined
        if self.w < 0 or self.h < 0 or self.N < 2 or (self.N > self.w and self.N > self.h):
            raise ValueError('Game cannot initialize with a {0:d}x{1:d} grid, and winning condition {2:d} in a row'.format(self.w, self.h, self.N))
 
        self.score = None
        self.state = np.zeros(size, dtype = np.float)
        self.openCells = [0]*self.w
        self.available_moves = list(range(self.w))  # array of possible moves.
        self.player = 1
        self.last_move = None
        self.n_moves = 0


    # fast deepcopy
    def __copy__(self):
        cls = self.__class__
        new_game = cls.__new__(cls)
        new_game.__dict__.update(self.__dict__)

        new_game.N = self.N
        new_game.score = self.score
        new_game.state = self.state.copy()
        new_game.openCells = copy(self.openCells)
        new_game.available_moves = copy(self.available_moves)
        new_game.n_moves = self.n_moves
        new_game.last_move = self.last_move
        new_game.player = self.player
        
        return new_game
    
    def sim_move(self, move):
        new_game = self.__copy__()
        new_game.move(move)
        
        return new_game

    # check victory condition
    # fast version
    def get_score(self):

        # game cannot end beca
        if self.n_moves < 2 * self.N-1:
            return None

        i, j = self.last_move
        hor, ver, diag_right, diag_left = get_lines(self.state, (i, j))

        # loop over each possibility
        for line in [ver, hor, diag_right, diag_left]:
            if in_a_row(line, self.N, self.player):
                return self.player
                    
        # no more moves
        if np.all(self.state != 0):
            return 0

        return None

    # for rendering
    # output a list of location for the winning line
    def get_winning_loc(self):
        
        if self.n_moves<2*self.N-1:
            return []

          
        loc = self.last_move
        hor, ver, diag_right, diag_left = get_lines(self.state, loc)
        ind = np.indices(self.state.shape)
        ind = np.moveaxis(ind, 0, -1)
        hor_ind, ver_ind, diag_right_ind, diag_left_ind = get_lines(ind, loc)
        # loop over each possibility
        
        pieces = [hor, ver, diag_right, diag_left]
        indices = [hor_ind, ver_ind, diag_right_ind, diag_left_ind]
        
        for line, index in zip(pieces, indices):
            starts, ends, runs = get_runs(line, self.player)

            # get the start and end location
            winning = (runs >= self.N)
            if not np.any(winning):
                continue
            
            starts_ind = starts[winning][0]
            ends_ind = ends[winning][0]
            indices = index[starts_ind:ends_ind]
            return indices
            
        return []
    
    
    def move(self, col):
        x = col if col > -1 else self.available_moves[col]
        success = False
        if x in self.available_moves:
            # make a move
            y = self.openCells[x]
            self.openCells[x] += 1
            self.state[x,y]=self.player
            success = True
               
            if self.openCells[x] > 5:
                self.available_moves.pop(self.available_moves.index(x))
               

        if success:
            self.n_moves += 1
            self.last_move = tuple((x,y))
            self.score = self.get_score()

            # if game is not over, switch player
            if self.score is None:
                self.player *= -1
               
            return True

        return False
    

    def available_mask(self):
        return (np.abs(self.state) != 1).astype(np.uint8)