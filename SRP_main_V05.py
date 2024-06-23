# coded by Alexander Groudas with Python Version 3.11.7.final.0
# Scissor Rock Paper
#
# 2024-06-19-1900
# V0.1 First code
# V0.2 Update: Error with imported classes fixed
# V0.3 Update: Integration of the game mechanics in the game class
# V0.4 Integration of GUI - Entry Name
# V0.41 Integration of GUI - Entry Gamemode and rounds
# V0.42 Removing the obsolete code for inputs of Player
# V0.5 ASCII-pictures and Highscore


from SRP_classes_V05 import Game, Player
from SRP_gui_V042 import Gui

gui = Gui()
gui.nameEntryWindow()
name = gui.returnPlayerName()
computer = Player('Computer')  # deriving instances player and computer from Player class
player = Player(name)

gui.gamemodeAndRoundsWindow()
gamemode = gui.returnGamemode()
rounds = gui.returnRounds()
game = Game(player, computer, gui, gamemode, rounds)  # deriving instance game from Game class
game.gameRun()
game.highscore()
game.showHighscores()
