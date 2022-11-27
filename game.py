class BoardClass:
    """This class creates a game board object to track important information of the Tic-Tac-Toe game for
    each player who initializes the object.

    Attributes:
        __playerUserNames__: A tuple with player1's username as the first item and player2's username as the second item.
        __lastPlayer__: A string of either self's username or opponent's username. Will switch off throughout the game
        according to whoever made the last move.
        __numWins__: An integer count of how many games the player has won.
        __gameBoard__: A list of lists. There are 3 lists within the outer list, and each item in the list is a string of
        either '' indicating an empty slot or 'X' or 'O' indicating that the slot is taken by the player corresponding to the shape.
        Each inner list indicates a row. And each index 0, 1, or 2 will indicate the column.
        The slots are numbered from 1-9 like so:
            [   [1, 2, 3]
                [4, 5, 6]
                [7, 8, 9]
                            ]

    """

    # Variable to keep track of number of games played
    __numGames__ = 0

    # Game Board will be kept track in a nested list
    # Inner list are the rows and each index of that inner list is the column
    __gameBoard__ = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    # Initializes all instance variables
    __playerUserNames__ = 0
    __numWins__ = 0
    __numLoss__ = 0
    __numGames__ = 1
    __gameBoard__ = 0
    __currentTurn__ = 0



    def __init__(self, playerUserNames: tuple[str, str]):
        """Inits BoardClass with all the attributes.

        Args:
            A tuple passed in with player1's username as the first item and player2's username as the second item, both as strings.
        """
        self.__playerUserNames__ = playerUserNames
        self.__currentTurn__ = self.__playerUserNames__[0]
        self.__numWins__ = 0
        self.__numTies__ = 0
        self.__numLoss__ = 0
        self.__numGames__ = 1
        self.__gameBoard__ = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]


    def updateGamesPlayed(self):
        """Keeps track how many games have started by updating __numGames__ by 1.
        """
        self.__numGames__ += 1



    def resetGameBoard(self):
        """Clears all the moves from the game board.
        Return:
            A new cleared game board with each slot being an empty string ''.
        """
        self.__gameBoard__ = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        self.__numGames__ += 1
        return self.__gameBoard__


    def updateGameBoard(self, move: list[str, int]):
        """Updates the game board with the player's move.
        Replace the item in the slot with the player's according shape.
        Example: ['X', 9] would place an X in index 3 of the 3rd list.

        Argument:
            List that contains info of the player's move (X or O) as first item and slot number (1-9) as second item.
        """
        shape = move[0]
        pos = move[1]

        if pos == 1:
            self.__gameBoard__[0][0] = shape
        elif pos == 2:
            self.__gameBoard__[0][1] = shape
        elif pos == 3:
            self.__gameBoard__[0][2] = shape
        elif pos == 4:
           self. __gameBoard__[1][0] = shape
        elif pos == 5:
            self.__gameBoard__[1][1] = shape
        elif pos == 6:
            self.__gameBoard__[1][2] = shape
        elif pos == 7:
            self.__gameBoard__[2][0] = shape
        elif pos == 8:
            self.__gameBoard__[2][1] = shape
        elif pos == 9:
            self.__gameBoard__[2][2] = shape




    def isWinner(self, player_code: str) -> bool:
        """
        Checks if the latest move resulted in a win. Updates the wins and losses count.
        Checks all the combinations of moves by comparing the index positions of the game board.
        Calls another function isLoser() to check if the player lost the game while the other player won.
        If there is no winner or loser then pass.

        Argument:
            A string of 'X' or 'O'

        Return:
            True if player is the winner, False if they are the loser, None if neither.
        """
        other_player_code = ''
        if player_code == "X":
            other_player_code = "O"
        elif player_code == "O":
            other_player_code = "X"

        # Checking the rows
        # position: 1, 2, 3
        if (self.__gameBoard__[0][0] == self.__gameBoard__[0][1] == self.__gameBoard__[0][2] == player_code):
            print("YOU ARE THE WINNER")
            self.__numWins__ += 1
            return True
        # position: 4, 5, 6
        elif (self.__gameBoard__[1][0] == self.__gameBoard__[1][1] == self.__gameBoard__[1][2] == player_code ):
            print("YOU ARE THE WINNER")
            self.__numWins__ += 1
            return True
        # position 7, 8, 9
        elif (self.__gameBoard__[2][0] == self.__gameBoard__[2][1] == self.__gameBoard__[2][2] == player_code):
            print("YOU ARE THE WINNER")
            self.__numWins__ += 1
            return True
        # Checking the columns
        # position: 1, 4, 7
        elif (self.__gameBoard__[0][0] == self.__gameBoard__[1][0] == self.__gameBoard__[2][0] == player_code):
            print("YOU ARE THE WINNER")
            self.__numWins__ += 1
            return True
        # position: 2, 5, 8
        elif (self.__gameBoard__[0][1] == self.__gameBoard__[1][1] == self.__gameBoard__[2][1] == player_code):
            print("YOU ARE THE WINNER")
            self.__numWins__ += 1
            return True
        # position: 3, 6, 9
        elif (self.__gameBoard__[0][2] == self.__gameBoard__[1][2] == self.__gameBoard__[2][2] == player_code):
            print("YOU ARE THE WINNER")
            self.__numWins__ += 1
            return True
        # Checking diagonal
        # position: 1, 5, 9
        elif (self.__gameBoard__[0][0] == self.__gameBoard__[1][1] == self.__gameBoard__[2][2] == player_code):
            print("YOU ARE THE WINNER")
            self.__numWins__ += 1
            return True
        # position: 3, 5, 7
        elif (self.__gameBoard__[0][2] == self.__gameBoard__[1][1] == self.__gameBoard__[2][0] == player_code):
            print("YOU ARE THE WINNER")
            self.__numWins__ += 1
            return True
        else:
            if self.isLoser(player_code) == True:  # Check if the player is a loser, if they are return False
                print("YOU LOST AND OTHER PLAYER WON")
                self.__numLoss__ += 1
                return False
            else:
                print("NO WINNER YET")
                pass




    def boardIsFull(self):
        """
        Checks if the board is full (i.e. no more moves to make - tie).
        Updates the ties count

        Initializes a variable emptySpace to count the number of empty spaces in the game board list (empty spaces indicated by '')
        Loops over each row of __gameBoard__ to count how many empty spaces. Updates emptySpace while looping over each row
        If emptySpace != 0 then board is not full. Else, board is full.

        Return:
            True if board is full, False if board is not full
        """

        emptySpace = 0
        for row in self.__gameBoard__:
            emptySpace += row.count('')

        if emptySpace != 0:
            return False
        else:
            self.__numTies__ += 1
            return True




    def printStats(self):
        """
        Prints the following each on a new line:
            - players user name
            - username of the last person to make a move
            - number of games
            - number of wins
            - number of losses
            - number of ties

        """
        print("Players usernames are:", self.__playerUserNames__)
        print("Last person to make a move:", self.__currentTurn__)
        print("Number of games played:", self.__numGames__)
        print("Number of wins:", self.__numWins__)
        print("Number of losses:", self.__numLoss__)
        print("Number of ties:", self.__numTies__)


    def printBoard(self):
        """
        Prints the board
        """
        for row in self.__gameBoard__:
            print(row)
        print()


    def updateWins(self):
        """
        Updates __numWins__ by 1.
        """
        self.__numWins__ += 1

    def updateLoss(self):
        """
        Updates __numLoss__ by 1
        """
        self.__numLoss__ += 1

    def updateGamesPlayed(self):
        """
        Updates __numGames__ by 1.
        """
        self.__numGames__ += 1

    def isLoser(self, player_code: str) -> bool:
        """
        Checks to see if the player is a loser. Does this by checking if the other player is a winner essentially.
        Uses the same methodology as isWinner() by comparing the values indexed in __gameBoard__.
        Argument:
            player_code: A string of either "X" or "O".
        Return:
            True if player is a loser, False if player is a winner.
        """

        other_player_code = ''
        if player_code == "X":
            other_player_code = "O"
        elif player_code == "O":
            other_player_code = "X"

        # Checking the rows
        # position: 1, 2, 3
        if (self.__gameBoard__[0][0] == self.__gameBoard__[0][1] == self.__gameBoard__[0][2] == other_player_code):
            return True
        # position: 4, 5, 6
        elif (self.__gameBoard__[1][0] == self.__gameBoard__[1][1] == self.__gameBoard__[1][2] == other_player_code):
            return True
        # position 7, 8, 9
        elif (self.__gameBoard__[2][0] == self.__gameBoard__[2][1] == self.__gameBoard__[2][2] == other_player_code):
            return True
        # Checking the columns
        # position: 1, 4, 7
        elif (self.__gameBoard__[0][0] == self.__gameBoard__[1][0] == self.__gameBoard__[2][0] == other_player_code):
            return True
        # position: 2, 5, 8
        elif (self.__gameBoard__[0][1] == self.__gameBoard__[1][1] == self.__gameBoard__[2][1] == other_player_code):
            return True
        # position: 3, 6, 9
        elif (self.__gameBoard__[0][2] == self.__gameBoard__[1][2] == self.__gameBoard__[2][2] == other_player_code):
            return True
        # Checking diagonal
        # position: 1, 5, 9
        elif (self.__gameBoard__[0][0] == self.__gameBoard__[1][1] == self.__gameBoard__[2][2] == other_player_code):
            return True
        # position: 3, 5, 7
        elif (self.__gameBoard__[0][2] == self.__gameBoard__[1][1] == self.__gameBoard__[2][0] == other_player_code):
            return True
        else:
            False



    def changeCurrentPlayer(self):
        """
        A method that updates and alternates the last player to make a move.
        If the last player is player1, then it will update to make player2 be the last player, and vice versa.
        """
        if self.__currentTurn__ == self.__playerUserNames__[0]:
            self.__currentTurn__ = self.__playerUserNames__[1]

        elif self.__currentTurn__ == self.__playerUserNames__[1]:
            self.__currentTurn__ = self.__playerUserNames__[0]
