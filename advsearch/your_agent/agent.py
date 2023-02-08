import random
from typing import Tuple

from ..othello.gamestate import GameState
from os import PathLike
import random
import sys
from copy import deepcopy

MIN = -99999999
MAX = 99999999

MAX_DEPTH = 6

WEIGHTS = [[4, -3, 2, 2, 2, 2, -3, 4],
           [-3, -4, -1, -1, -1, -1, -4, -3],
           [2, -1, 1, 0, 0, 1, -1, 2],
           [2, -1, 0, 1, 1, 0, -1, 2],
           [2, -1, 0, 1, 1, 0, -1, 2],
           [2, -1, 1, 0, 0, 1, -1, 2],
           [-3, -4, -1, -1, -1, -1, -4, -3],
           [4, -3, 2, 2, 2, 2, -3, 4]]

class Node():
    def __init__(self, the_board, opponent, parent, weight, children, move):
        self.parent   = parent
        self.board    = the_board
        self.opponent = opponent 
        self.weight   = weight
        self.children = children
        self.move     = move #movimento que resultou no atual estado do board

    def expand(self, color):
        parent = self
        board  = self.board

        if board.is_terminal_state() is False:

            moves = board._legal_moves.get(color)

            for move in moves:
                x = move[0]
                y = move[1]

                new_board  = deepcopy(board)
                new_weight = WEIGHTS[y][x]
                new_board.process_move(move,color)
                opponent   = new_board.opponent(color)

                child = Node(new_board,opponent,parent,new_weight,[], move)

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

def max_weight(node,color, depth, alpha, beta):
    if depth > MAX_DEPTH:
        return node.weight
    else:
        v = MIN 

        while depth <= MAX_DEPTH:

            if node.has_children() == False:
                node.expand(color)
            if node.no_moves_left(): #se após expandir o nodo ele segue sem filhos, não existem mais jogadas possiveis
                break
            else:
                for child in node.children:
                    depth = depth + 1
                    v     = max(v,min_weight(child,child.opponent,depth,alpha,beta))
                    alpha = max(alpha,v)

                    if alpha >= beta:
                        break
    return v

def min_weight (node, color, depth, alpha, beta):
    if depth > MAX_DEPTH:
        return node.weight
    else:
        v = MAX

        while depth <= MAX_DEPTH:

            if node.has_children() == False:
                node.expand(color)
            if node.no_moves_left(): #se após expandir o nodo ele segue sem filhos, não existem mais jogadas possiveis
                break
            else:
                for child in node.children:
                    depth = depth + 1
                    v     = min(v,max_weight(child,child.opponent,depth,alpha,beta))
                    beta  = min(beta,v)

                    if beta <= alpha:
                        break
    return v

# Percorre os nodos expandidos até encontrar o que possui o peso retornado pelo algoritmo alfa beta
def get_move_position(node,weight):
    children = node.children

    for child in children:
        if child.weight == weight:
            return child.move
        elif child.has_children():
            get_move_position(child, weight)

# Função chamada quando o oponente não possui jogadas
def get_best_move(moves):
    best_mov_weight = MIN

    for move in moves:
        x = move[0]
        y = move[1]

        new_weight = WEIGHTS[y][x]

        if new_weight > best_mov_weight:
            best_mov_pos = move
    
    return best_mov_pos

def alpha_beta_pruning(board, color):
    if board.is_terminal_state() == True or board.has_legal_move(color) == False:
        return (-1, -1)
    elif board.piece_count.get('EMPTY') == 60: #jogada inicial
        return random.choice(board._legal_moves[color])
    elif board.has_legal_move(board.opponent(color)) == False: #oponente não tem mais jogadas
        return get_best_move(board._legal_moves[color])
    else:
        depth    = 1
        opponent = board.opponent(color)
        node     = Node(board,opponent,None,0,[],())

        v = max_weight(node,color,depth,MIN,MAX)
    
        return get_move_position(node,v)

def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    return alpha_beta_pruning(state.board,state.player)