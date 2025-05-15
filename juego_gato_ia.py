import math

# Representación del tablero
board = [" " for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in cond) for cond in win_conditions)

def game_over():
    return winner("X") or winner("O") or " " not in board

def minimax(is_maximizing, ai_player, human_player):
    if winner(ai_player):
        return 1
    elif winner(human_player):
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = ai_player
            score = minimax(False, ai_player, human_player)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = human_player
            score = minimax(True, ai_player, human_player)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(ai_player, human_player):
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = ai_player
        score = minimax(False, ai_player, human_player)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

def main():
    print("Bienvenido al Juego del Gato (Jugador vs IA)\n")
    player = input("¿Quieres ser X o O?: ").upper()
    ai = "O" if player == "X" else "X"
    current = "X"

    while not game_over():
        print_board()
        if current == player:
            move = int(input("Tu turno (0-8): "))
            if board[move] != " ":
                print("Movimiento inválido, intenta de nuevo.")
                continue
            board[move] = player
        else:
            print("Turno de la IA...")
            move = best_move(ai, player)
            board[move] = ai
        current = "O" if current == "X" else "X"

    print_board()
    if winner(player):
        print("¡Ganaste!")
    elif winner(ai):
        print("La IA ganó.")
    else:
        print("¡Empate!")

if __name__ == "__main__":
    main()
