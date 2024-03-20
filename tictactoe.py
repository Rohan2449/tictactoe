"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # the count of X and O in the board
    x_count = 0
    o_count = 0

    # iterates through the board, and counts the occurances
    # of X and Y marks 
    for row in board:
        for col in row:
            if col == X:
                x_count += 1
            elif col == O:
                o_count += 1

    #returns X or Y. Whichever has the next turn on the board
    if x_count <= o_count:
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    #create a set of all possible actions
    possible_actions = set()

    #iterate through each element on the board.
    for row in range(len(board)):
        for col in range(len(board[row])):
            #if the square is empty, it is a possible move
            if board[row][col] == EMPTY:
                #therefore add the possible move to the set
                possible_actions.add((row, col))
    
    #return the set of all possible actions
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #check if action is a possible action
    if action not in actions(board):
        raise Exception("Invalid action!")
    
    #create deep copy of the current board
    copy_board = copy.deepcopy(board)

    #player = whoevers turn it is (X or Y)
    mark = player(copy_board)

    #obtain row and column of the action
    i = action[0]
    j = action[1]

    #mark the copy board with the player's action
    copy_board[i][j] = mark

    #return the updated copy board
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #squares of each board. Left to Right. Top to Bottom.

    one = board[0][0]
    two = board[0][1]
    three = board[0][2]
    four = board[1][0]
    five = board[1][1]
    six = board[1][2]
    seven = board[2][0]
    eight  = board[2][1]
    nine = board[2][2]

    for mark in [X, O]:
        #checking horizontal
        if one == two == three == mark:
            return mark
        if four == five == six == mark:
            return mark
        if seven == eight == nine == mark:
            return mark
        
        #checking vertical
        if one == four == seven == mark:
            return mark
        if two == five == eight == mark:
            return mark
        if three == six == nine == mark:
            return mark
        
        #checking diagnol
        if one == five == nine == mark:
            return mark
        if three == five == seven == mark:
            return mark

    return None
    



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winner_player = winner(board)
    if winner_player in [X, O]:
        return True
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
            
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    #return 1 if winner is X
    #return -1 if winner is O
    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    
    #return 0 if no winner
    return 0


def max_value(board):
    #if a winning move has been found
    if terminal(board):
        return utility(board)
    max = -2
    for action in actions(board):
        best_min_move = min_value(result(board, action))

        if best_min_move == 1:
            return best_min_move
        if best_min_move > max:
            max = best_min_move
        
    return max


def min_value(board):
    if terminal(board):
        return utility(board)
    
    min = 2
    for action in actions(board):
        best_max_move = max_value(result(board, action))

        if best_max_move == -1:
            return best_max_move
        if best_max_move < min:
            min = best_max_move
    return min


"""
    The function minimax could be optimized.
    On the first move of the game, the AI will calculate all of the
    possible outcomes of the game. 

    After each additional turn, the AI will recalculate every possible outcome
    again.

    There is no need for this. If the outcomes can be stored somewhere, like a trie
    then we can improve run time efficiency and eliminate the need for unnecessary
    calculations.
"""

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    player_turn = player(board)
    if player_turn == X:
        best_score = -2

        for action in actions(board):
            action_utility = min_value(result(board, action))

            if action_utility > best_score:
                best_score = action_utility
                best_move = action
    elif player_turn == O:
        best_score = 2

        for action in actions(board):
            action_utility = max_value(result(board, action))

            if action_utility < best_score:
                best_score = action_utility
                best_move = action
    

    return best_move
    





