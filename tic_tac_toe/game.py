from tic_tac_toe.players import Player, Bot
from tic_tac_toe.board import Board
import random


def introduction():
    """
    Function to start the game(get user's name, choose who is x
    :return: instances for Bot and User
    """

    player_name = input("Lets start the game<3\nEnter your name, please: ")
    print("Now it will be randomly chousen who is making first step\n")
    player_symbol = random.randint(0, 1)
    if player_symbol == 1:
        player_symbol = Board.CROSS
        print("Yaaay(づ｡◕‿‿◕｡)づ, you are making first step!\n")
        bot_symbol = Board.ZERO
        player = Player(player_name, player_symbol)
        bot = Bot('Rybka🐟', bot_symbol)
        return player, bot

    else:
        player_symbol = Board.ZERO
        bot_symbol = Board.CROSS
        player = Player(player_name, player_symbol)
        bot = Bot('Rybka🐟', bot_symbol)
        print("{} is making first step!\n".format(bot.player_name))
        return bot, player


def main():
    """main function to ran the game"""
    first, second = introduction()
    if isinstance(first, Player):
        player = 'x_symbol'
    else:
        player = 'o_symbol'
    board = Board()
    while True:
        if board.play:
            board = first.make_move(board, Board.CROSS)
            board.check_status()
        if board.play:
            board = second.make_move(board, Board.ZERO)
            board.check_status()
        else:
            break
    if board.draw:
        print('The game ended in a draw (ಥ_ಥ)')
    # representing end of the game
    if board.have_winner:
        winner = board.winner()
        if (winner == '✗' and player == 'x_symbol'):
            print(
                'Cool, {}, you won the battle, but what about the the '
                'war'.format(
                    first.player_name))
        elif (winner == 'o' and player == 'o_symbol'):
            print(
                'Cool, {}, you won the battle, but what about the the '
                'war'.format(
                    second.player_name))
        else:
            print('You lost the battle, but what about the war')


if __name__ == "__main__":
    main()
