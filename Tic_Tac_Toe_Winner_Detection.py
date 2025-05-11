'''
Problem Statement:

You are given a 3x3 matrix representing the final state of a Tic Tac Toe game. Each cell in the matrix contains either ‘X’ or ‘O’. Your task is to determine the winner of the game or if it’s a tie.

A player wins if they have three of their symbols (‘X’ or ‘O’) in a row, column, or diagonal. If neither player has three in a row, column, or diagonal, then the game is a tie.

Write a function that takes the 3x3 matrix as input and returns “X wins”, “O wins”, or “Tie” accordingly.

Sample Input 1:

[
  ['X', 'O', 'O'],
  ['O', 'X', 'O'],
  ['O', 'O', 'X']
]

'''


def determine_winner(matrix):
    # Check rows for X
    for row in matrix:
        if row[0] == row[1] == row[2] == 'X':
            return "X wins"

    # Check columns for X
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] == 'X':
            return "X wins"

    # Check diagonals for X
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'X':
        return "X wins"
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'X':
        return "X wins"

    # Check rows for O
    for row in matrix:
        if row[0] == row[1] == row[2] == 'O':
            return "O wins"

    # Check columns for O
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] == 'O':
            return "O wins"

    # Check diagonals for O
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'O':
        return "O wins"
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'O':
        return "O wins"

    # No winner found
    return "Tie"


# Example usage
matrix = [
    ['X', 'O', 'O'],
    ['O', 'X', 'O'],
    ['O', 'O', 'X']
]
print(determine_winner(matrix))