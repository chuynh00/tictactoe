'''
This is a class that will create the Tic-Tac-Toe GUI using Tkinter.
'''

# Include tkinter from the standard library
import tkinter as tk
from tkinter import Button
from tkinter.messagebox import askyesno, askquestion, showinfo
from tkinter import ttk
import game
import socket

class player2UIClass():

    address = 0
    port = 0
    currentTurn = 'Player 1'
    finalResults = ''
    myUsername = ''
    otherPlayerUserName = ''
    message = ''
    player2Socket = ''


    def __init__(self):


        self.canvasSetup()
        self.initTKVariables()
        self.buildButtons()
        self.createHostInfoEntry()
        self.createPortInfoEntry()
        self.createUsernameEntry()
        self.submit_username_button()
        self.connect_and_wait_button()


        self.runUI()


    # define a method that initalizes my tk variables (these are like normal variables but special bc they deal with tkinter)
    def initTKVariables(self):
        # initializing class variables
        self.address = tk.StringVar()
        self.port = tk.IntVar()
        self.currentTurn = tk.StringVar()
        self.finalResults = tk.StringVar()
        self.myUsername = tk.StringVar()
        self.otherPlayerUserName = tk.StringVar()
        self.message = tk.StringVar()


    # define a method to setup my canvas
    def canvasSetup(self):
        # initialize my tkinter canvas
        # This is the Tk interface object and we are going to call it master. Refer to master to make edits to interface
        self.master = tk.Tk()
        self.master.title("Tic Tac Toe")  # sets the window title
        self.master.geometry('800x400')  # sets the default size of the window
        self.master.configure(background='pink')  # set the background color of the window
        self.master.resizable(1,1)  # setting the x(horizontal) and y (vertical) to not be resizable. 1 is to allow resize, 0 is to not



    # define a method to build buttons for each slot
    def buildButtons(self):

        # Creating the buttons
        self.b1 = Button(self.master, text=" ", font=('Helvetica', 20), height=3, width=6, command=lambda: self.buttonClicked(self.b1))
        self.b2 = Button(self.master, text=" ", font=('Helvetica', 20), height=3, width=6, command=lambda: self.buttonClicked(self.b2))
        self.b3 = Button(self.master, text=" ", font=('Helvetica', 20), height=3, width=6, command=lambda: self.buttonClicked(self.b3))
        self.b4 = Button(self.master, text=" ", font=('Helvetica', 20), height=3, width=6, command=lambda: self.buttonClicked(self.b4))
        self.b5 = Button(self.master, text=" ", font=('Helvetica', 20), height=3, width=6, command=lambda: self.buttonClicked(self.b5))
        self.b6 = Button(self.master, text=" ", font=('Helvetica', 20), height=3, width=6, command=lambda: self.buttonClicked(self.b6))
        self.b7 = Button(self.master, text=" ", font=('Helvetica', 20), height=3, width=6, command=lambda: self.buttonClicked(self.b7))
        self.b8 = Button(self.master, text=" ", font=('Helvetica', 20), height=3, width=6, command=lambda: self.buttonClicked(self.b8))
        self.b9 = Button(self.master, text=" ", font=('Helvetica', 20), height=3, width=6, command=lambda: self.buttonClicked(self.b9))

        # Assigning positions of buttons on the grid
        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        self.buttonList = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]


    # define a method to fill in a slot by changing the text if player clicks on the slot
    def buttonClicked(self, button):
        button['text'] = 'O'

        if button == self.b1:
            self.pos = 1
        elif button == self.b2:
            self.pos = 2
        elif button == self.b3:
            self.pos = 3
        elif button == self.b4:
            self.pos = 4
        elif button == self.b5:
            self.pos = 5
        elif button == self.b6:
            self.pos = 6
        elif button == self.b7:
            self.pos = 7
        elif button == self.b8:
            self.pos = 8
        elif button == self.b9:
            self.pos = 9

        # Update game board in BoardClass and print the new updated board
        self.player2Move = ['O', self.pos]
        self.player2Board.updateGameBoard(self.player2Move)
        self.player2Board.printBoard()

        # Send my move to player1
        self.player1Socket.send(bytes(str(self.player2Move), encoding='ascii'))

        # Check to see if Player2 is a winner
        self.win = self.player2Board.isWinner("O")

        # If player2 is the winner, announce they are the winner in a pop up message
        # then ask if they want to play again. If yes then clear board from BoardClass and UI
        if self.win == True:
            self.recvPlayAgain = self.player1Socket.recv(1024).decode('ascii')
            if self.recvPlayAgain == "PLAY AGAIN":
                self.player2Board.resetGameBoard()

                for button in self.buttonList:
                    button['text'] = ' '
                self.gameloop()
                return True
            else:
                self.player2Board.printStats()
                self.createFinalResultsPopUp()
                self.master.quit()

        # Check to see if there is a Tie after player2 puts move down
        self.tie = self.player2Board.boardIsFull()
        if self.tie == True:
            self.recvPlayAgain = self.player1Socket.recv(1024).decode('ascii')
            if self.recvPlayAgain == "PLAY AGAIN":
                self.player2Board.resetGameBoard()

                for button in self.buttonList:
                    button['text'] = ' '
                self.gameloop()
                return True
            else:
                self.player2Board.printStats()
                self.createFinalResultsPopUp()
                self.master.quit()


        # Change last player to player1 before receiving the move
        self.player2Board.changeCurrentPlayer()
        self.currentTurnLabel.config(text="Current Turn:" + self.player2Board.__currentTurn__)
        self.master.update()
        print("Current Turn:", self.player2Board.__currentTurn__)



        # Receive Player1's move and play the move on my board
        self.message.set(self.player1Socket.recv(1024).decode('ascii'))

        # Clean and decode
        self.stringclean = self.message.get().strip('[')
        self.stringclean = self.stringclean.strip(']')
        self.stringclean = self.stringclean.replace("'", '')
        self.splitstring = self.stringclean.split(',')
        self.splitstring[1] = int(self.splitstring[1].strip())


        # Update Board Class
        self.player2Board.updateGameBoard(self.splitstring)
        self.player2Board.printBoard()

        # Update Player2's UI board
        if self.splitstring[1] == 1:
            self.b1['text'] = 'X'
        elif self.splitstring[1] == 2:
            self.b2['text'] = 'X'
        elif self.splitstring[1] == 3:
            self.b3['text'] = 'X'
        elif self.splitstring[1] == 4:
            self.b4['text'] = 'X'
        elif self.splitstring[1] == 5:
            self.b5['text'] = 'X'
        elif self.splitstring[1] == 6:
            self.b6['text'] = 'X'
        elif self.splitstring[1] == 7:
            self.b7['text'] = 'X'
        elif self.splitstring[1] == 8:
            self.b8['text'] = 'X'
        elif self.splitstring[1] == 9:
            self.b9['text'] = 'X'

        # Check to see if Player2 is the loser
        self.win = self.player2Board.isWinner("O")

        # If player1 is the loser, announce they are the loser in a pop up message
        # then ask if they want to play again. If yes then clear board from BoardClass and UI
        if self.win == False:
            self.recvPlayAgain = self.player1Socket.recv(1024).decode('ascii')
            if self.recvPlayAgain == "PLAY AGAIN":
                self.player2Board.resetGameBoard()

                for button in self.buttonList:
                    button['text'] = ' '
                self.gameloop()
                return True
            else:
                self.player2Board.printStats()
                self.createFinalResultsPopUp()
                self.master.quit()


        # Check to see if there is a tie after player1 puts move down
        self.tie = self.player2Board.boardIsFull()
        if self.tie == True:
            self.recvPlayAgain = self.player1Socket.recv(1024).decode('ascii')
            if self.recvPlayAgain == "PLAY AGAIN":
                self.player2Board.resetGameBoard()

                for button in self.buttonList:
                    button['text'] = ' '
                self.gameloop()
                return True
            else:
                self.player2Board.printStats()
                self.createFinalResultsPopUp()
                self.master.quit()


        # Change last player to player2
        self.player2Board.changeCurrentPlayer()
        self.currentTurnLabel.config(text="Current Turn:" + self.player2Board.__currentTurn__)
        self.master.update()
        print("Current Turn:", self.player2Board.__currentTurn__)






    # define a method that creates an entry field for host information
    def createHostInfoEntry(self):
        self.hostInfoLabel = tk.Label(self.master, text="Please enter host information:")
        self.hostInfoLabel.grid(row=3, column=3)
        self.hostEntry = tk.Entry(self.master, textvariable=self.address)
        self.hostEntry.grid(row=3, column=4)


    # define a method that creates an entry field for port number
    def createPortInfoEntry(self):
        self.portInfoLabel = tk.Label(self.master, text="Please enter port number:")
        self.portInfoLabel.grid(row=4, column=3)
        self.portEntry = tk.Entry(self.master, textvariable=self.port)
        self.portEntry.grid(row=4, column=4)



    # define a method that starts the server connection to player2 upon hitting the start
    def startServer(self):
        print("I am waiting for a connection")

        # Create a socket object (TCP socket stream AF_INET type)
        self.player2Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind my host with my port number
        # Pass a tuple with IP address and port number
        self.player2Socket.bind((self.address.get(), self.port.get()))

        # Setup my socket using listen function
        self.player2Socket.listen(5)

        # Begin accepting incoming connection requests
        self.player1Socket, self.player1Address = self.player2Socket.accept()


        # Printing Player1's address
        print("Player1 connected from: ", self.player1Address)



    # define a method that creates a start server button
    def connect_and_wait_button(self):
        self.connectButton = Button(self.master, text="Connect & Wait", command=self.startServer)
        self.connectButton.grid(row=4, column=5)


    # define a method that pops up a message box for player1 if socket connection to player2 has failed
    def connectFail(self):
        socketFail = askquestion(title="Tic Tac Toe", message="Connection failed. Would you like to try again?")
        return socketFail #this will return True/False


    # define method that pops up message box for player1 if socket connection is successful
    def connectSuccess(self):
        showinfo(title=None, message="Connection to player2 successful")


    # define a method that pops up a message box for player1 asking if they want to play again
    def playagainDialog(self):
        answer = askyesno(title="Tic Tac Toe", message="Do you want play again?")
        return answer #this will return True/False



    # define a method that creates an entry field for username information
    def createUsernameEntry(self):
        self.usernameLabel = tk.Label(self.master, text="Please enter your username: ")
        self.usernameLabel.grid(row=5, column=3)
        self.usernameEntry = tk.Entry(self.master, textvariable=self.myUsername)
        self.usernameEntry.grid(row=5, column=4)

    # define method for button that submits username
    def submit_username_button(self):
        self.send_username_button = Button(self.master, text='Send Username', command=self.send_username)
        self.send_username_button.grid(row=5, column=5)


    # define a method that returns the username as a string upon pressing button
    def send_username(self):
        # Receiving Player 1's username
        self.otherPlayerUserName.set(self.player1Socket.recv(1024).decode('ascii'))
        print("Player 1's username is:", self.otherPlayerUserName.get())

        # Then sending my username
        self.player1Socket.send(bytes(self.myUsername.get(), encoding='ascii'))

        self.player2Board = game.BoardClass((self.otherPlayerUserName.get(), self.myUsername.get()))

        self.createCurrentTurnLabel()

        self.gameloop()






    # define a method to start the gameloop (player2 first listens for player1's move and plays it on their board)
    def gameloop(self):
        self.currentTurnLabel['text'] = "Current Turn: " + self.player2Board.__currentTurn__
        self.currentTurnLabel.config(text="Current Turn:" + self.player2Board.__currentTurn__)
        print("Current Turn:", self.player2Board.__currentTurn__)

        # Receive Player1's move and play the move on my board
        self.message.set(self.player1Socket.recv(1024).decode('ascii'))

        # Clean and decode
        self.stringclean = self.message.get().strip('[')
        self.stringclean = self.stringclean.strip(']')
        self.stringclean = self.stringclean.replace("'", '')
        self.splitstring = self.stringclean.split(',')
        self.splitstring[1] = int(self.splitstring[1].strip())

        # Update Board Class
        self.player2Board.updateGameBoard(self.splitstring)
        self.player2Board.printBoard()

        # Update Player2's UI board
        if self.splitstring[1] == 1:
            self.b1['text'] = 'X'
        elif self.splitstring[1] == 2:
            self.b2['text'] = 'X'
        elif self.splitstring[1] == 3:
            self.b3['text'] = 'X'
        elif self.splitstring[1] == 4:
            self.b4['text'] = 'X'
        elif self.splitstring[1] == 5:
            self.b5['text'] = 'X'
        elif self.splitstring[1] == 6:
            self.b6['text'] = 'X'
        elif self.splitstring[1] == 7:
            self.b7['text'] = 'X'
        elif self.splitstring[1] == 8:
            self.b8['text'] = 'X'
        elif self.splitstring[1] == 9:
            self.b9['text'] = 'X'


        # Set last player to player 2
        self.player2Board.changeCurrentPlayer()
        self.currentTurnLabel.config(text="Current Turn:" + self.player2Board.__currentTurn__)
        print("Current Turn:", self.player2Board.__currentTurn__)








    # define a method that creates a label to display who's turn it currently is
    def createCurrentTurnLabel(self):
        self.currentTurnLabel = tk.Label(self.master, text="Current turn: " + self.player2Board.__currentTurn__)
        self.currentTurnLabel.grid(row=6, column=5)


    # define a method to display final results
    def createFinalResultsPopUp(self):
        self.finalResults = showinfo(title="Player 2 Stats", message="Final Results: \n" +
                                                            "Players usernames are: " + str(self.player2Board.__playerUserNames__) + '\n' +
                                                            "Last person to make a move: " + str(self.player2Board.__currentTurn__) + '\n' +
                                                            "Number of games played: " + str(self.player2Board.__numGames__) + '\n' +
                                                            "Number of wins: "+ str(self.player2Board.__numWins__) + '\n' +
                                                            "Number of losses: " + str(self.player2Board.__numLoss__) + '\n' +
                                                            "Number of ties: " + str(self.player2Board.__numTies__))





    # define a method that announces the winner and asks to play again
    def winner_announce1(self):
        self.playagain = askyesno(title="Winner Detected", message="Player 2 is the winner. Player 1 is the loser. Do you want to play again?")
        return self.playagain

    def loser_annouce1(self):
        self.playagain = askyesno(title="Winner Detected", message="Player 2 is the loser. Player 1 is the winner Do you want to play again?")
        return self.playagain


    # define method that announces a tie and asks to play again
    def tieAnnounce(self):
        self.playagain = askyesno(title="Tie Detected",
                                  message="There is a Tie. Do you want to play again?")
        return self.playagain



    # define a method start UI
    def runUI(self):
        # starts my UI - event handler
        self.master.mainloop()




    def randomClick(self):
        print("CLICKING RANDOM BUTTON")



if __name__ == '__main__':
    # Create a UI board for player1
    player2UI = player2UIClass()