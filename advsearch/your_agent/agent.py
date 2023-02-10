import random
from typing import Tuple

from ..othello.gamestate import GameState
from os import PathLike
import random
import sys

MIN = -sys.maxsize -1
MAX = sys.maxsize

MAX_DEPTH = 6

WEIGHTS = [[4, -3, 2, 2, 2, 2, -3, 4],
           [-3, -4, -1, -1, -1, -1, -4, -3],
           [2, -1, 1, 0, 0, 1, -1, 2],
           [2, -1, 0, 1, 1, 0, -1, 2],
           [2, -1, 0, 1, 1, 0, -1, 2],
           [2, -1, 1, 0, 0, 1, -1, 2],
           [-3, -4, -1, -1, -1, -1, -4, -3],
           [4, -3, 2, 2, 2, 2, -3, 4]]

# WEIGHTS = [[100, -20, 10, 5, 5, 10, -20, 100],
#            [-20, -50, -2, -2, -2, -2, -50, -20],
#            [10, -2, -1, -1, -1, -1, -2, 10],
#            [5, -2, -1, -1, -1, -1, -2, 5],
#            [5, -2, -1, -1, -1, -1, -2, 5],
#            [10, -2, -1, -1, -1, -1, -2, 10],
#            [-20, -50, -2, -2, -2, -2, -50, -20],
#            [100, -20, 10, 5, 5, 10, -20, 100]]

class Node():
    def __init__(self, board, opponent, parent, weight, children, move):
        self.parent   = parent
        self.board    = board
        self.opponent = opponent 
        self.weight   = weight
        self.children = children
        self.move     = move #movimento que resultou no atual estado do board

    def expand(self, color):
        parent = self
        board  = self.board

        if board.is_terminal_state() is False:

            moves = board.legal_moves(color)

            for move in moves:
                x = move[0]
                y = move[1]

                node_board  = board.copy()
                node_weight = WEIGHTS[y][x]
                node_board.process_move(move,color)
                opponent = node_board.opponent(color)

                child = Node(node_board,opponent,parent,node_weight,[], move)

                self.children.append(child)

    def has_children(self):
        if self.children == []:
            return False
        else:
            return True

    def no_moves_left(self):
        if self.has_children() == False:
            return True
        else:
            return False

def max_player(node,color, depth, alpha, beta):
    if depth > MAX_DEPTH:
        return [node.weight,node]
    else:
        result = [MIN,node]

        while depth <= MAX_DEPTH:

            if node.has_children() == False:
                #print("max expandindo cor " + color)
                node.expand(color)
            if node.no_moves_left(): 
                break
            else:
                for child in node.children:
                    depth = depth + 1

                    before = result[0]
                    after     = max(result[0],min_player(child,child.opponent,depth,alpha,beta)[0])
                    if(after != before):
                        result = [after,child]

                    alpha = max(alpha,result[0])

                    if alpha >= beta:
                        break
    return result

def min_player (node, color, depth, alpha, beta):
    if depth > MAX_DEPTH:
        return [node.weight,node]
    else:
        result = [MAX,node]

        while depth <= MAX_DEPTH:

            if node.has_children() == False:
                #print("min expandindo cor " + color)
                node.expand(color)
            if node.no_moves_left(): 
                break
            else:
                for child in node.children:
                    depth = depth + 1
                    before = result[0]
                    after     = min(result[0],max_player(child,child.opponent,depth,alpha,beta)[0])
                    if(after != before):
                        result = [after,child]
                    beta  = min(beta,result[0])

                    if beta <= alpha:
                        break
    return result


def get_best_move(moves):
    best_move_weight = MIN
    for move in moves:
        x = move[0]
        y = move[1]

        weight = WEIGHTS[y][x]

        if weight > best_move_weight:
            best_move = move
            best_move_weight = weight
    
    return best_move

def minimax_alphabeta(board, color):
    if board.is_terminal_state() == True or board.has_legal_move(color) == False:
        return (-1, -1)
    elif board.piece_count.get('EMPTY') == 60: #jogada inicial
        return random.choice(board.legal_moves(color))
    elif board.has_legal_move(board.opponent(color)) == False: 
        return get_best_move(board.legal_moves(color))
    else:
        depth = 1
        opponent = board.opponent(color)
        node = Node(board,opponent,None,0,[],())

        v = max_player(node,color,depth,MIN,MAX)
        chosen_node = v[1]

        #print(v)
        return chosen_node.move

def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    result = minimax_alphabeta(state.board,state.player)
    print(result)
    return result