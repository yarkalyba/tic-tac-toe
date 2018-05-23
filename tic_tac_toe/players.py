from anytree import RenderTree, Node
import random


class AbstractPlayer:
    """Abstract class for players"""

    def __init__(self, player_name, symbol):
        self.player_name = player_name
        self.symbol = symbol

    def symbol(self):
        return self.symbol


class Player(AbstractPlayer):
    """Class to represent the player"""

    def make_move(self, board, symbol):
        """
        Method to add move of the user
        :param board: playing board
        :param symbol: symbol of the user
        :return: boars with new symbol
        """
        while True:
            new_board = board.user_move(symbol)
            if new_board != None:
                break
        return new_board


class Bot(AbstractPlayer):
    """Class to represent the Bot"""

    def __init__(self, player_name, symbol):
        super().__init__(player_name, symbol)

    def make_move(self, board, symbol):
        """
        Method to add move of the bot
        :param board: playing board
        :param symbol: symbol of the bot
        :return: boars with new symbol
        """
        lst_words = ['Are you already afraid?', 'Rybka is watching you!',
                     'Ready?', 'Eat this!']
        print('{} is making a move now: '.format(self.player_name))
        tree = TreeHelper(board)
        print(lst_words[random.randint(0, len(lst_words) - 1)])
        new_board = tree.best_child(symbol)
        print(new_board.name)
        return new_board.name


class TreeHelper:
    """Class to represent the tree"""

    def __init__(self, board):
        board_node = Node(board)
        self.tree = RenderTree(board_node)

    def best_child(self, symbol):
        """
        Method to choose the best move
        :param symbol: symbol of the bot
        :return: board with the best move
        """
        self._fill_tree(symbol)
        try:
            board = max(self.tree.node.children, key=lambda x: x.point)
        except ValueError:
            return self.tree.node
        return board

    def _fill_tree(self, symbol):
        """
        Method to build the tree with all possible moves
        :param symbol: symbol of the player
        """

        def fill_tree_node(node):
            """recursive filling of the tree"""
            board = node.name
            children = board.make_children(symbol)
            for child in children:
                child_node = Node(child, parent=node, point=0)
                if child.play:
                    fill_tree_node(child_node)

                    points = sum(
                        [smaller.point for smaller in child_node.children])
                    child_node.points = points
                if child.draw:
                    child_node.point = 0
                if child.have_winner:
                    winner = child.winner()
                    if winner == Bot.symbol:
                        child_node.point = 1
                    else:
                        child_node.point = -1

        fill_tree_node(self.tree.node)
