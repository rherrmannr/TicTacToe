class TicTacToe:
    def __init__(self, beginner):
        self.player = beginner
        self.gf = [[None, None, None],
                   [None, None, None],
                   [None, None, None]]

    def swap_player(self):
        if self.player is "X":
            self.player = "O"
        elif self.player is "O":
            self.player = "X"

    def set_obj(self, row, column):
        if self.gf[row][column] is None and self.check_player_has_won() is None:
            self.gf[row][column] = self.player
            self.swap_player()
            return True
        return False

    def check_player_has_won(self):
        # check rows
        for row in self.gf:
            if row[0] is row[1] and row[0] is row[2] and row[0] is not None:
                return row[0]

        # check columns
        for i in range(3):
            if self.gf[0][i] is self.gf[1][i] and self.gf[0][i] is self.gf[2][i] and self.gf[0][i] is not None:
                return self.gf[0][i]

        # check top left to bottom right
        if self.gf[0][0] is self.gf[1][1] and self.gf[0][0] is self.gf[2][2] and self.gf[0][0] is not None:
            return self.gf[0][0]

        # check bottom left to top right
        if self.gf[2][0] is self.gf[1][1] and self.gf [2][0] is self.gf[0][2] and self.gf[2][0] is not None:
            return self.gf[2][0]

        # return None if no one has won
        return None

    def check_draw(self):
        for row in self.gf:
            if row[0] is None or row[1] is None or row[2] is None:
                return False
        return True

    def restart(self):
        self.swap_player()
        self.__init__(self.player)

    def set_player(self, player):
        self.player = player
