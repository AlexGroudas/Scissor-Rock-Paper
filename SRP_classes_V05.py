# coded by Alexander Groudas with Python Version 3.11.7.final.0
# Scissor Rock Paper
#
# 2024-06-19-1900
# V0.1 First code
# V0.2 Update: Error with imported classes fixed
# V0.3 Update: Integration of the game mechanics in the game class
# V0.4 Integration of GUI
# V0.41 Integration of GUI - Entry Gamemode and rounds
# V0.42 Removing the obsolete code for inputs of Player
# V0.5 ASCII-pictures

import random
import json
import os  # necessary to save data


class Player:
    '''
    Create player class with methods for human player and computer
    '''

    def __init__(self, name):
        self.name = name
        self.assignment_dict = {
            '1': 'Scissors',
            '2': 'Paper',
            '3': 'Rock',
            '4': 'Lizard',
            '5': 'Spock'
        }
        self.points = 0

    def play(self, name, hand) -> str:
        '''
        Receives a number as a satring that refers to a dict with the hands, assignment_dict.
        Can be used later (another method in the game class) to refer to the defeat_dict.
        :param hand: str
        :return: str
        '''
        print(f'{name} plays {self.assignment_dict[hand]}')  # gleich löschen, dient nur der Kontrolle
        return self.assignment_dict[hand]


class Game:
    '''
    Create a game class that contains the game mechanics
    '''

    def __init__(self, player, computer, gui, gamemode, rounds):
        # variablen
        self.defeat_dict = {
            'Scissors': ['Paper', 'Lizard'],
            'Paper': ['Rock', 'Spock'],
            'Rock': ['Scissors', 'Lizard'],
            'Lizard': ['Paper', 'Spock'],
            'Spock': ['Scissors', 'Rock']
        }
        self.player = player
        self.computer = computer
        self.gui = gui
        self.gamemode = gamemode
        self.rounds = rounds
        self.asciiPics = {
            '1': """
                        _______
                    ---'   ____)____
                              ______)
                           __________)
                          (____)
                    ---.__(___)
                    """,
            '3': """
                        _______
                    ---'   ____)
                          (_____)
                          (_____)
                          (____)
                    ---.__(___)
                    """,
            '2': """
                         _______
                    ---'    ____)____
                               ______)
                              _______)
                             _______)
                    ---.__________)
                    """,
            '4': """
                        ____
                    ---'  (_____)
                          (______)
                       (_________)
                        (____)
                    ---.__(___)
                    """,
            '5': """
                         _______
                    ---'   ____)____
                               ______)
                            __________)
                           (_______)
                    ---.__(___)
                    """,
            'You Won': """
                __     ______  _    _  __          __        _
                \ \   / / __ \| |  | | \ \        / /       | |
                 \ \_/ / |  | | |  | |  \ \  /\  / /__  _ __| |
                  \   /| |  | | |  | |   \ \/  \/ / _ \| '__| |
                   | | | |__| | |__| |    \  /\  / (_) | |  |_|
                   |_|  \____/ \____/      \/  \/ \___/|_|  (_)
                    """,
            'Loser': """
                __     ______  _    _   _      ____   _____ ______ 
                \ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
                 \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
                  \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
                   | | | |__| | |__| | | |___| |__| |____) | |____ 
                   |_|  \____/ \____/  |______\____/|_____/|______|
                    """
        }

    def decide(self, player_hand, computer_hand):
        '''
        method to decide who have won
        :param player_hand:
        :param computer_hand:
        :return:
        '''
        if player_hand in self.defeat_dict[computer_hand]:
            print(f'{computer_hand} beats {player_hand}')
            print('Computer wins this round')
            self.computer.points += 1
        else:
            print(f'{player_hand} beats {computer_hand}')
            print(f'{self.player.name} wins this round')
            self.player.points += 1
        print(f'{self.player.name} points: {self.player.points} of {self.rounds} to win')
        print(f'{self.computer.name} points: {self.computer.points} of {self.rounds} to win')

    def gameRun(self):
        round_number = 1  # round number for counting
        gameover = False  # variable for end of the game
        while gameover == False:
            print(f'---------------------------------\nRound: {round_number}')
            round_number += 1
            if self.gamemode == 'e':
                self.gui.playerHandExtended()  #
                player_choice = self.gui.get_chosen_hand()
                hands = ['1', '2', '3', '4',
                         '5']  # defining possible hands according to the extended or normal mode for computer
            elif self.gamemode == 'n':
                self.gui.playerHandNormal()
                player_choice = self.gui.get_chosen_hand()
                hands = ['1', '2', '3']
            else:
                break  # just for good programming style because player_choice ans hands could (in theory) be undefined

            player_hand = self.player.play(self.player.name, player_choice[0])
            computer_hand = self.computer.play(self.computer.name, random.choice(hands))
            print(self.asciiPics[player_choice[0]])

            if player_hand == computer_hand:
                print('DRAW! play again!')

            else:
                self.decide(player_hand, computer_hand)  # decides who wins and get the point

            # definition end of game
            if self.player.points == int(self.rounds):
                print('CONGRATS!!!! You have won!!!!')
                print(self.asciiPics['You Won'])
                gameover = True
            elif self.computer.points == int(self.rounds):
                print('LOSER!!!! Computer has won!!!!')
                print(self.asciiPics['Loser'])
                gameover = True

    def highscore(self):
        highscoreFile = 'highscores.json'

        # Loading of eventually existing highscore data
        if os.path.exists(highscoreFile):
            with open(highscoreFile, 'r') as file:
                highscores = json.load(file)
        else:
            highscores = {}

        # Updating high score data
        if self.player.name not in highscores:
            highscores[self.player.name] = {'wins': 0, 'losses': 0}

        if self.player.points == int(
                self.rounds):  # if put elif instead of if the name is saved with 0:0, instead of 0:1 or 1:0
            highscores[self.player.name]['wins'] += 1
        else:
            highscores[self.player.name]['losses'] += 1

        # saving the actual data
        with open(highscoreFile, 'w') as file:
            json.dump(highscores, file)

        print(
            f"Highscore for {self.player.name} saved: {highscores[self.player.name]['wins']} wins, {highscores[self.player.name]['losses']} losses")

    def showHighscores(self):
        highscore_file = 'highscores.json'
        if os.path.exists(highscore_file):
            with open(highscore_file, 'r') as file:
                highscores = json.load(file)
                print('other Highscores:')
                for player, scores in highscores.items():
                    print(f'Player: {player}')
                    print(f"  Wins: {scores['wins']}")
                    print(f"  Losses: {scores['losses']}")
        else:
            print('No highscore data availabe')
