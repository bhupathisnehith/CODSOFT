
import math

board = [" " for _ in range(9)]  

HUMAN = "X"
AI = "O"

def print_board(board):
    print("-------------")
    for i in range(3):
        print(f"| {board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} |")
        print("-------------")

def is_board_full(board):
    return " " not in board

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = AI

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] != " ":
            print("Invalid move. Try again.")
            continue
        board[human_move] = HUMAN
        print_board(board)

        if check_winner(board, HUMAN):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move(board)
        print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()

***OUTPUT:***
Welcome to Tic-Tac-Toe!
-------------
|   |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter your move (0-8): 4
-------------
|   |   |   |
-------------
|   | X |   |
-------------
|   |   |   |
-------------
AI is making a move...
-------------
| O |   |   |
-------------
|   | X |   |
-------------
|   |   |   |
-------------
Enter your move (0-8): 0
Invalid move. Try again.
Enter your move (0-8): 1
-------------
| O | X |   |
-------------
|   | X |   |
-------------
|   |   |   |
-------------
AI is making a move...
-------------
| O | X |   |
-------------
|   | X |   |
-------------
|   | O |   |
-------------
Enter your move (0-8): 8
-------------
| O | X |   |
-------------
|   | X |   |
-------------
|   | O | X |
-------------
AI is making a move...
-------------
| O | X | O |
-------------
|   | X |   |
-------------
|   | O | X |
-------------
Enter your move (0-8): 5
-------------
| O | X | O |
-------------
|   | X | X |
-------------
|   | O | X |
-------------
AI is making a move...
-------------
| O | X | O |
-------------
| O | X | X |
-------------
|   | O | X |
-------------
Enter your move (0-8): 6
-------------
| O | X | O |
-------------
| O | X | X |
-------------
| X | O | X |
-------------
It's a draw!
