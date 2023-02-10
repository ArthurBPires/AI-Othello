from typing import Tuple
from ..othello.gamestate import GameState
import sys

MAX_DEPTH = 8

MIN = -sys.maxsize -1
MAX = sys.maxsize


WEIGHTS = [[100, -20, 10, 5, 5, 10, -20, 100],
           [-20, -50, -2, -2, -2, -2, -50, -20],
           [10, -2, -1, -1, -1, -1, -2, 10],
           [5, -2, -1, -1, -1, -1, -2, 5],
           [5, -2, -1, -1, -1, -1, -2, 5],
           [10, -2, -1, -1, -1, -1, -2, 10],
           [-20, -50, -2, -2, -2, -2, -50, -20],
           [100, -20, 10, 5, 5, 10, -20, 100]]

# WEIGHTS = [[4, -3, 2, 2, 2, 2, -3, 4],
#            [-3, -4, -1, -1, -1, -1, -4, -3],
#            [2, -1, 1, 0, 0, 1, -1, 2],
#            [2, -1, 0, 1, 1, 0, -1, 2],
#            [2, -1, 0, 1, 1, 0, -1, 2],
#            [2, -1, 1, 0, 0, 1, -1, 2],
#            [-3, -4, -1, -1, -1, -1, -4, -3],
#            [4, -3, 2, 2, 2, 2, -3, 4]]

class Node():
    def __init__(self, board, opponent, parent, weight, children, move):
        self.board    = board
        self.parent   = parent
        self.opponent = opponent 
        self.weight   = weight
        self.move     = move
        self.children = children

    def expand(self, player):
        parent = self
        board  = self.board

        if board.is_terminal_state() is False:

            moves = board.legal_moves(player)

            for move in moves:
                x = move[0]
                y = move[1]

                node_board  = board.copy()
                opponent = node_board.opponent(player)
                node_weight = WEIGHTS[y][x]
                node_board.process_move(move,player)

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

def max_gamer(node,color, depth, alpha, beta) -> Tuple[Node,int]: #Jogador max
    if depth > MAX_DEPTH:
        return (node.weight,node)
    else:
        result = (MIN,node)

        while depth <= MAX_DEPTH:

            if node.has_children() == False:
                node.expand(color)
            if node.no_moves_left(): 
                break
            else:
                for child in node.children:
                    depth = depth + 1

                    before = result[0]
                    after     = max(result[0],min_gamer(child,child.opponent,depth,alpha,beta)[0])
                    if(after != before):
                        result = (after,child)

                    alpha = max(alpha,result[0])

                    if alpha >= beta:
                        break
    return result

def min_gamer (node, color, depth, alpha, beta) -> Tuple[Node,int]: #Jogador min
    if depth > MAX_DEPTH:
        return (node.weight,node)
    else:
        result = (MAX,node)

        while depth <= MAX_DEPTH:

            if node.has_children() == False:
                node.expand(color)
            if node.no_moves_left(): 
                break
            else:
                for child in node.children:
                    depth = depth + 1
                    before = result[0]
                    after     = min(result[0],max_gamer(child,child.opponent,depth,alpha,beta)[0])
                    if(after != before):
                        result = (after,child)
                    beta  = min(beta,result[0])

                    if beta <= alpha:
                        break
    return result

def minimax_alphabeta(state):
    if state.legal_moves() == set():
        return (-1, -1)
    else:
        board = state.board
        player = state.player
        opponent = board.opponent(player)
        node = Node(board,opponent,None,0,[],())


        depth = 1
        result = max_gamer(node,player,depth,MIN,MAX)
        choosen_node = result[1]
        choosen_move = choosen_node.move

        return choosen_move

def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    result = minimax_alphabeta(state)
    
    return result