import math
import sys

def print_board(board):
    for i in range(3):
        print('|'.join(board[3*i:3*i+3]))
        if i < 2:
            print('-'*5)

def check_winner(board):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]               # diags
    ]
    for line in wins:
        if board[line[0]] == board[line[1]] == board[line[2]] and board[line[0]] != ' ':
            return board[line[0]]
    if ' ' not in board:
        return 'Tie'
    return None

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    if winner == 'O':
        return -1
    if winner == 'Tie':
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    print("In AI evaluation move")
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [' '] * 9
    print("Positions are numbered 0-8 as follows:")
    print("0|1|2")
    print("3|4|5")
    print("6|7|8")
    print("You are 'O' and AI is 'X'. Let's start!\n")
    
    while True:
        print_board(board)
        while True:
            try:
                line = input("Your move (0-8): ")
                if not line.strip():
                    return
                move = int(line)
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move, try again")
                else:
                    board[move] = 'O'
                    break
            except (ValueError, EOFError):
                return

        winner = check_winner(board)
        if winner == 'O':
            print_board(board)
            print("You win!")
            break
        elif winner == 'Tie':
            print_board(board)
            print("It's a tie!")
            break

        # AI move
        ai_move = best_move(board)
        if ai_move is not None:
            board[ai_move] = 'X'
            winner = check_winner(board)
            if winner == 'X':
                print_board(board)
                print("AI wins")
                break
            elif winner == 'Tie':
                print_board(board)
                print("It's a tie")
                break

if __name__ == "__main__":
    play_game()
