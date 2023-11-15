import random
from logic import check_winner

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [' '] * 9
        self.current_player = None
        self.players = [player1, player2]

    def print_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-----")

    def is_board_full(self):
        return ' ' not in self.board

    def is_winner(self, player):
        board = [self.board[i:i+3] for i in range(0, 9, 3)]
        winner = check_winner(board)
        return winner == player

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        else:
            return False

    def switch_player(self):
        self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]

    def play_game(self):
        self.current_player = random.choice(self.players)

        while not self.is_board_full():
            self.print_board()
            print(f"\nCurrent player: {self.current_player}")

            if self.current_player == 'bot':
                position = self.bot_move()
            else:
                position = self.get_player_move()

            if not self.make_move(position):
                print("Invalid move. Try again.")
                continue

            if self.is_winner(self.current_player):
                self.print_board()
                print(f"\nCongratulations! {self.current_player} wins!")
                return  # Exit the function early when there's a winner

            self.switch_player()

        print("\nThe game is a tie!")  

    def get_player_move(self):
        while True:
            try:
                position = int(input("Enter your move (1-9): ")) - 1
                if 0 <= position <= 8 and self.board[position] == ' ':
                    return position
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def bot_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ' ']
        return random.choice(available_moves)

if __name__ == "__main__":
    player1 = input("Enter name for Player 1: ")
    player2_choice = input("Enter 'bot' for single player mode or name for Player 2: ")

    if player2_choice.lower() == 'bot':
        player2 = 'bot'
    else:
        player2 = player2_choice

    game = TicTacToe(player1, player2)
    game.play_game()
