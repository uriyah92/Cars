
import car


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        board = list()
        for i in range(7):
            board_row = list()
            for j in range(7):
                board_row.append((i, j))
            if i == 3:
                board_row.append((3, 7))

            board.append(board_row)
        cars = list()
        self.cars = cars
        self.board = board

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        gameboard = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                cell = self.cell_content((i, j))
                if cell == None:
                    gameboard += ' _ '
                else:
                    gameboard += (' ' + str(cell)+' ')
            if i == 3:
                gameboard += ' _ '
            gameboard += ' \n'
        return str(gameboard)

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """

        boardlist = list()
        for i in range(7):
            for j in range(7):
                boardlist.append((i, j))
            if i == 3:
                boardlist.append((3, 7))
        return boardlist

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,move_key,description)
                 representing legal moves
        """

        posibilities = list()
        for car in self.cars:
            if car.orientation:
                right = car.movement_requirements('r')[0]
                if right[0] < len(self.board) and right[0] >= 0 and\
                        right[1] < len(self.board[0]) and right[1] >= 0:
                    if self.cell_content(right) == None:
                        posibilities.append(
                            (car.name, 'r', car.possible_moves()['r']))
                if right[0] == 3 and right[1] == 7:
                    posibilities.append(
                        (car.name, 'r', car.possible_moves()['r']))

                left = car.movement_requirements('l')[0]
                if left[0] < len(self.board) and left[0] >= 0 and\
                        left[1] < len(self.board[0]) and left[1] >= 0:
                    if self.cell_content(left) == None:
                        posibilities.append(
                            (car.name, 'l', car.possible_moves()['l']))
            else:
                down = car.movement_requirements('d')[0]
                if down[0] < len(self.board) and down[0] >= 0 and\
                        down[1] < len(self.board[0]) and down[1] >= 0:
                    if self.cell_content(down) == None:
                        posibilities.append(
                            (car.name, 'd', car.possible_moves()['d']))
                up = car.movement_requirements('u')[0]
                if up[0] < len(self.board) and up[0] >= 0 and\
                        up[1] < len(self.board[0]) and up[1] >= 0:
                    if self.cell_content(up) == None:
                        posibilities.append(
                            (car.name, 'u', car.possible_moves()['u']))
        return posibilities

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """

        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """

        for car in self.cars:
            if coordinate in car.car_coordinates():
                return car.name
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """

        for cord in car.car_coordinates():
            if cord[0] < len(self.board) and cord[0] >= 0 and\
                    cord[1] < len(self.board[0]) and cord[1] >= 0:
                if self.cell_content(cord) == None:
                    for cartemp in self.cars:
                        if cartemp.name == car.name:
                            return False
                    self.cars.append(car)
                    return True
        return False

    def move_car(self, name, move_key):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param move_key: Key of move in car to activate
        :return: True upon success, False otherwise
        """

        posibilities = self.possible_moves()
        for car in self.cars:
            if car.name == name:
                dict = car.possible_moves()
                if (name, move_key, dict[move_key]) in posibilities:
                    car.move(move_key)
                    return True
        return False
