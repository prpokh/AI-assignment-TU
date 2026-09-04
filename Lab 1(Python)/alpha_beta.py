import math
from common_data import game_tree, leaf_values, show_student_info

def alpha_beta(node, is_max, alpha, beta):
    # Terminal leaf check
    if node in leaf_values:
        return leaf_values[node]

    children = game_tree.get(node, [])

    if is_max:
        max_eval = -math.inf
        for child in children:
            eval_score = alpha_beta(child, False, alpha, beta)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                print(f"Pruned remaining children of {node} (Beta={beta} <= Alpha={alpha})")
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in children:
            eval_score = alpha_beta(child, True, alpha, beta)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                print(f"Pruned remaining children of {node} (Beta={beta} <= Alpha={alpha})")
                break
        return min_eval

if __name__ == "__main__":
    initial_alpha = -math.inf
    initial_beta = math.inf

    root_val = alpha_beta('ROOT', is_max=True, alpha=initial_alpha, beta=initial_beta)

    print(f"\nOptimal Root Evaluation Score: {root_val}")
    show_student_info("07 - Minimax with Alpha-Beta Pruning")