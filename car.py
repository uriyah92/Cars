class Car:

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        cordinats = list()
        if self.orientation:
            for i in range(self.length):
                cordinats.append((self.location[0], self.location[1]+i))
        else:
            length = self.length-1
            for i in range(self.length):
                cordinats.append((self.location[0]+length-i,
                                  self.location[1]))

        return cordinats

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.orientation == 1:
            result = {'l': 'move one cell to the left',
                      'r': 'move one cell to the rigth'}
        else:
            result = {'u': 'move one cell up', 'd': 'move one cell down'}
        return result

    def movement_requirements(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        if move_key in self.possible_moves():
            if move_key == 'u':
                return [(self.location[0]-1, self.location[1])]
            if move_key == 'd':
                return [(self.car_coordinates()[0][0]+1,
                         self.car_coordinates()[0][1])]
            if move_key == 'l':
                return [(self.location[0], self.location[1]-1)]
            if move_key == 'r':
                return [(self.car_coordinates()[-1][0],
                         self.car_coordinates()[-1][1]+1)]
        else:
            return None

    def move(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """

        target = self.movement_requirements(move_key)[0]
        if target != None:
            if move_key == 'u' or move_key == 'l':
                self.location = target
                return True
            if move_key == 'd':
                self.location = (self.location[0]+1, self.location[1])
                return True
            if move_key == 'r':
                self.location = (self.location[0], self.location[1]+1)
                return True

        return False

    def get_name(self):
        """
        :return: The name of this car.
        """

        return self.name
