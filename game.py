
import board
import car
import helper
import sys


LEGAL_DIRECTIONS = ['u','U', 'd','D', 'r','R', 'l','L']
LEGAL_NAMES = ['Y', 'B', 'O', 'G', 'W', 'R']


class Game:

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """

        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it.

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """

        inputtemp = input("enter your move ")
        if inputtemp == '!':
            return -1
        inputa, inputb = inputtemp.split(',')

        if inputa in LEGAL_NAMES and inputb in LEGAL_DIRECTIONS:
            name = inputa
            move_key = inputb
        else:
            print("illegal move, try again! ")
            return 0
        if self.board.move_car(name, move_key):
            return 1
        else:
            print("invalid input! ")
            return 0

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """

        while (1):
            print(self.board)
            if self.board.cell_content(self.board
                                       .target_location()) != None:
                print('congrats!')
                return
            current_turn = self.__single_turn()
            if current_turn == 0:
                continue
            if current_turn == -1:
                return
            print(self.board)


if __name__ == "__main__":
    board = board.Board()
    game = Game(board)
    args = sys.argv
    dict = {}
    dict = helper.load_json(args[1])
    cars = list()
    for char in dict:
        car_temp = car.Car(char, dict[char][0], dict[char][1],
                           dict[char][2])
        board.add_car(car_temp)
    game.play()
