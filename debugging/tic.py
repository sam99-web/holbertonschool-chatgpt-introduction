def print_board(board):
    """Affiche le plateau de jeu."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Vérifie s'il y a un gagnant."""
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Retourne le symbole du gagnant

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def get_move(player):
    """Demande à l'utilisateur un coup valide."""
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in [0,1,2] or col not in [0,1,2]:
                print("Invalid input. Please enter numbers 0, 1, or 2.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def tic_tac_toe():
    """Fonction principale pour jouer au Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while True:
        print_board(board)
        row, col = get_move(player)
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue
        board[row][col] = player
        moves += 1

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if moves == 9:  # match nul
            print_board(board)
            print("It's a tie!")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

tic_tac_toe()
