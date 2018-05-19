"""
File name: game.play
Purpose: To play the classic game of Tic Tac Toe
Author: Eddie Tapia, UCSD Undergraduate 
"""

print '---------------------------TIC TAC TOE-----------------------------\n'
print '\t\t\t   |   |'
print '\t\t\t---+---+---'
print '\t\t\t   |   |   '
print '\t\t\t---+---+---'
print '\t\t\t   |   |   '
print "Choose your symbol:\n1.Player1 -> X\n2.Player2 -> O\n>>"
print '\t\t\t 1 | 2 | 3 '
print '\t\t\t---+---+---'
print '\t\t\t 4 | 5 | 6 '
print '\t\t\t---+---+---'
print '\t\t\t 7 | 8 | 9 '
list_Pl1 = []
list_Pl2 = []
# Define empty list with 10 empty spaces to keep track of spots on the board
list = ['', '-', '-', '-', '-', '-', '-', '-', '-', '-']


# this function will display the tic tac toe game display.here we have a list named list which stores the position input from players .
# i have created the list of 10 integers because i had some problems doing
# the program =>not important


def displayBoard(player, input):
    """
    Purpose: This function will display the current state of the board
    @param player: Keeps track of player (either X or O )
    @param input: 
    """
    print 'The input is', input
    ''''''
    print '\t\t\t',list[1],'|',list[2],'|', list[3]
    print '\t\t\t--+---+--'
    print '\t\t\t',list[4],'|',list[5],'|', list[6]
    print '\t\t\t--+---+--'
    print '\t\t\t',list[7],'|',list[8],'|', list[9]

def check_input(input_pl):
    """
    Purpose: This function is used to check if the position entered by the user is taken or not
    @param input_pl: The position where the user wants to place their move
    @return: True if spot is open, False if invalid move
    """
    if input_pl > 9 or input_pl < 0:
        return False
    # TODO:
    # If list[input_pl] has not been taken, return True
    
    # If it is not taken return False
    return False

def winner(chk):
    """
    Purpose: This function checks all the winning conditions to see if they are true
    """
    # TODO:
    # If spots 1 2 3 are equal
    # If spots 4 5 6 are equal
    # If spots 7 8 9 are equal
    # If spots 1 4 7 are equal 
    # If spots 2 5 8 are equal
    # If spots 3 6 9 are equal
    # If spots 1 5 9 are equal
    # If spots 7 5 3 are equal
    
    # If none of the above conditions are true, return False 
    return False

def play():
    """
    Purpose: This function is the main function that will run the game of tic tac toe
    """
    # This will count the number of inputs we've inserted into the board
    number_of_inputs = 1

    error_pl2 = 'off'
    # Run the loop until we've inserted 9 items into the board, which means there are no more moves to make
    while(number_of_inputs <= 9):
        # Odd means input from player 1("X") and even means player2("O")
        if(number_of_inputs % 2 != 0):  
            print 'Player: X Enter your desired position'
            # Store input from player 1
            input_Pl1 = int(input(''))

            if (check_input(input_Pl1)) and (error_pl2 == 'off'):
                list[input_Pl1] = "X"
                displayBoard('X', input_Pl1)
                if(winner('X')):
                    print("X is winner")
                    break
                number_of_inputs += 1
            # If position is already taken then  we continue the loop so again beginning from top
            else:
                print 'The position is already taken.Please choose wisely player X\n'
                continue
        else:
            # Runs for even number_of_inputs
            if(number_of_inputs != 9):
                print 'Player: O Enter your desired position'
                input_Pl2 = int(input(''))
                if check_input(input_Pl2):
                    list[input_Pl2] = "O"
                    list_Pl2.append(input_Pl2)
                    if(winner("O")):
                        print("O is winner")
                        break
                    number_of_inputs += 1
                    displayBoard("O", input_Pl2)
                    error_pl2 = 'off'
                else:
                    print 'The position is already taken .Please choose wisely player O \n'
                    # Assign error_pl2 so that for next iteration we can skip asking input for player 1.
                    error_pl2 = 'on'

"""
Now that you've fixed the functions, it's time to call the play function
"""
# TODO: 
# Call the function to play the game

