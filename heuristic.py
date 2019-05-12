import numpy as np

class Heuristic:

    def get_score(self, game):
        '''
        Estimates the utility of the board.
        Return infity if player wins and -infinity if player loses.

        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.

        Returns
        -------
        float
            The utility for the given board.
        '''

        self.board = game.state
        self.h = game.h
        self.w = game.w
        winner = game.get_score()
        player = game.player

        if winner == -1:
            return float("-inf")

        if winner == 1:
            return float("inf")

        own_moves = self.calc_score(player)
        opp_moves = self.calc_score(player * -1)
        return(float(own_moves - 3 * opp_moves))

    def find_pieces(self, player):
        '''
        Finds the pieces for the given player.

        Parameters
        ----------
        player : The player to find the pieces of.
        '''

        self.pieces = []
        p_x, p_y = np.where(self.board == player)
        for p in zip(p_x, p_y):
            self.pieces.append(p)

    def score_rows(self, player):
        '''
        Scores the rows of the board for the given player.
        2 pieces in a row of the given player that can become 4-in-a-row is worth 1pt.
        3 pieces in a row of the given player that can become 4-in-a-row is worth 2pts.
        3 pieces in a row that can become 4 in both directions is worth infite pts.

        Parameters
        ----------
        player : The player to use for scoring the board.

        Returns
        -------
        float
            The total score calculated for all the pieces of the given players in all the rows.
        '''

        score = 0
        for piece in self.pieces:
            x = piece[0]
            y = piece[1]

        # checking rows from left to right.
            if x + 3 < self.w:
                if self.board[x + 1][y] == player:
                    if self.board[x + 2][y] == 0:
                        score += 1
                    elif self.board[x + 2][y] == player:
                        if x - 1 > 0:
                            if self.board[x - 1][y] == 0 and self.board[x + 3][y] == 0:
                                return float("inf")
                        elif self.board[x + 3][y] == 0:
                            score += 10

        # checking rows from right to left
            if x - 3 > 0:
                if self.board[x - 1][y] == player:
                    if self.board[x - 2][y] == 0:
                        score += 1
                    elif self.board[x - 2][y] == player:
                        if x + 1 < self.w:
                            if self.board[x + 1][y] == 0 and self.board[x - 3][y] == 0:
                                return float("inf")
                        elif self.board[x - 3][y] == 0:
                            score += 10
        return score

    def score_cols(self, player):
        '''
        Scores the columns of the board for the given player.
        2 pieces in a column of the given player that can become 4-in-a-row is worth 1pt.
        3 pieces in a column of the given player that can become 4-in-a-row is worth 2pts.

        Parameters
        ----------
        player : The player to use for scoring the board.

        Returns
        -------
        float
            The total score calculated for all the pieces of the given players in all the columns.
        '''

        score = 0
        for piece in self.pieces:
            x = piece[0]
            y = piece[1]

            if y + 3 < self.h:
                if self.board[x][y + 1] == player:
                    if self.board[x][y + 2] == 0:
                        score += 1
                    elif self.board[x][y + 2] == 1 and self.board[x][y + 3] == 0:
                        score += 10
        return score

    def score_diag(self, player):
        '''
        Scores the diagonals of the board for the given player.
        2 pieces in a diagonal of the given player that can become 4-in-a-row is worth 1pt.
        3 pieces in a diagonal of the given player that can become 4-in-a-row is worth 2pts.

        Parameters
        ----------
        player : The player to use for scoring the board.

        Returns
        -------
        float
            The total score calculated for all the pieces of the given players in all the diagonals.
        '''

        score = 0
        for piece in self.pieces:
            x = piece[0]
            y = piece[1]
            
            if x + 3 < self.w and x - 3 > 0 and y + 3 < self.h:
                # checking diagonals of posite slope.
                if self.board[x + 1][y + 1] == player:
                    if self.board[x + 2][y + 2] == 0:
                        score += 1
                    elif self.board[x + 2][y + 2] == player and self.board[x + 3][y + 3] == 0:
                        score += 10

                # checking diagonals of negative slope.
                elif self.board[x - 1][y + 1] == player:
                    if self.board[x - 2][y + 2] == 0:
                        score += 1
                    elif self.board[x - 2][y + 2] == player and self.board[x - 3][y + 3] == 0:
                        score += 10
        return score

    def calc_score(self, player):
        '''
        Scores the board based on the given player.

        Parameters
        ----------
        player : The player to use for scoring the board.

        Returns
        -------
        float
            The score given to the board for the given player.
        '''

        self.find_pieces(player)
        score = 0
        score += self.score_rows(player)
        score += self.score_cols(player)
        score += self.score_diag(player)
        return score