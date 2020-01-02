LIGHT_GREY = (64, 64, 64)
BLUE = (20, 20, 150)
RED = (150, 20, 20)
WHITE = (255, 255, 255)


class TicTacToeUI:
    def __init__(self, game, tictactoe, window):
        self.game = game
        self.tictactoe = tictactoe
        self.window = window
        self.timer = game.time.Clock()
        self.game.font.init()
        self.font = self.game.font.SysFont("arial", 20)
        self.text = self.font.render("Hello", False, (0, 0, 0))

    def draw_field(self):
        self.game.draw.line(self.window, LIGHT_GREY, (100, 0), (100, 300), 2)
        self.game.draw.line(self.window, LIGHT_GREY, (200, 0), (200, 300), 2)
        self.game.draw.line(self.window, LIGHT_GREY, (0, 100), (300, 100), 2)
        self.game.draw.line(self.window, LIGHT_GREY, (0, 200), (300, 200), 2)
        self.game.draw.line(self.window, LIGHT_GREY, (0, 300), (300, 300), 2)

    def draw_x(self, row, column):
        x = column * 100
        y = row * 100
        self.game.draw.line(self.window, BLUE, (20 + x, 20 + y), (80 + x, 80 + y), 2)
        self.game.draw.line(self.window, BLUE, (20 + x, 80 + y), (80 + x, 20 + y), 2)

    def draw_o(self, row, column):
        x = column * 100
        y = row * 100
        self.game.draw.circle(self.window, RED, (50 + x, 50 + y), 40, 1)

    def draw_gf(self):
        row_num = 0
        for row in self.tictactoe.gf:
            column_num = 0
            for ele in row:
                if ele is "X":
                    self.draw_x(row_num, column_num)
                elif ele is "O":
                    self.draw_o(row_num, column_num)
                column_num += 1
            row_num += 1

    def draw_winner(self, winner):
        text = "{0} has won. 'R' for restart!".format(winner)
        self.text = self.font.render(text, False, (0, 0, 0))

    def draw_draw(self):
        text = "It's a draw. 'R' for restart!".format(self.tictactoe.player)
        self.text = self.font.render(text, False, (0, 0, 0))

    def show_player(self):
        text = "{0}'s turn. 'R' for restart!".format(self.tictactoe.player)
        self.text = self.font.render(text, False, (0, 0, 0))

    def show_text_output(self):
        winner = self.tictactoe.check_player_has_won()
        if winner is not None:
            self.draw_winner(winner)
        elif self.tictactoe.check_draw():
            self.draw_draw()
        else:
            self.show_player()
        self.window.blit(self.text, (5, 305))

    def update(self):
        self.window.fill(WHITE)
        self.draw_field()
        self.draw_gf()
        self.show_text_output()

        self.game.display.update()
        self.timer.tick(30)
