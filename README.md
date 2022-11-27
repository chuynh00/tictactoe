# Tic-Tac-Toe GUI Game

To run the program with GUI Tkinter library:

First run player2UI.py, then run player1UI.py. 

Enter the hostname and port information on player2UI.py and press the "Connect & Wait" button. Player 2 is the server and will wait for Player 1, the client, to connect.

Next, enter the host and port information on player1UI.py. If the connection is unsuccessful a message box will pop up asking if you want to attempt to connect again. 

Once the connection is established a messagebox will pop up confirming that connection has begun.

Next, enter the username information on player1UI first and press the "Send Username" button. This sends the username of player1 over to player2. After player2 should do the same with entering their username and pressing the "Send Username" button.

Once player 2 sends their username over the game starts and player1 gets to make the first move. 

If there is a tie or winner detected, a message box will pop up on player1UI.py and ask if they want to play again. If "Yes" is chosen, then continue playing a new game. If "No" is chosen then player1UI.py and player2UI.py will have message boxes that pop up and report each player's game statistics. After they each close that messagebox, the program terminates. 

The program also supports a printed gameboard on the console if you don't want to use the GUI version. These can be done by running player1.py and player2.py.
