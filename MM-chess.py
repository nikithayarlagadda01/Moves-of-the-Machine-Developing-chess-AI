import chess
import math

def evaluate_position(board):

    piece_scores = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 0}
    total_score = 0
    for piece in board.piece_map().values():
        piece_value = piece_scores[piece.symbol().lower()]
        total_score += piece_value if piece.color else -piece_value
    return total_score

def alpha_beta_search(board, depth, alpha, beta, is_maximizing):
    """
    To see the best move we evaluate Alpha-Beta Pruning.
    """
    if depth == 0 or board.is_game_over():
        return evaluate_position(board)

    if is_maximizing:
        max_score = -math.inf
        for move in board.legal_moves:
            board.push(move)
            current_score = alpha_beta_search(board, depth - 1, alpha, beta, False)
            board.pop()
            max_score = max(max_score, current_score)
            alpha = max(alpha, current_score)
            if beta <= alpha:
                break  # Beta cutoff
        return max_score
    else:
        min_score = math.inf
        for move in board.legal_moves:
            board.push(move)
            current_score = alpha_beta_search(board, depth - 1, alpha, beta, True)
            board.pop()
            min_score = min(min_score, current_score)
            beta = min(beta, current_score)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_score

def determine_best_move(board, search_depth):
    """
    Identify the best move for the current player.
    """
    optimal_move = None
    optimal_value = -math.inf if board.turn else math.inf
    alpha = -math.inf
    beta = math.inf

    for move in board.legal_moves:
        board.push(move)
        move_value = alpha_beta_search(board, search_depth - 1, alpha, beta, not board.turn)
        board.pop()

        if (board.turn and move_value > optimal_value) or (not board.turn and move_value < optimal_value):
            optimal_value = move_value
            optimal_move = move

    return optimal_move

# Main game loop
board = chess.Board()
while not board.is_game_over():
    print(board)
    if board.turn:  # White's move
        print("White's turn...")
        selected_move = determine_best_move(board, 3)
    else:  # Black's move
        print("Black's turn...")
        selected_move = determine_best_move(board, 3)
    board.push(selected_move)
    print(f"Move played: {selected_move}\n")

print("Game Over!")
print(f"Result: {board.result()}")


