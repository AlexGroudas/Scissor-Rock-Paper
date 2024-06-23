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

import tkinter


class Gui:
    def __init__(self):
        self.name = ''
        self.gamemode = ''
        self.rounds = ''
        self.chosen_player_hand = ''

    def nameEntryWindow(self):
        '''
        :return: name of Player
        '''

        def getName():
            self.name = name_entry.get().strip()
            root.destroy()

        root = tkinter.Tk()  # main window
        root.title('Name Entry')
        root.geometry('250x100')
        tkinter.Label(root, text='Name:').pack()  # Label and Entry for the name
        name_entry = tkinter.Entry(root)
        name_entry.pack()
        submit_button = tkinter.Button(root, text='Confirm', command=getName)  # Button for confirming
        submit_button.pack()
        root.mainloop()  # main loop for the name-window

    def returnPlayerName(self):
        return self.name

    def gamemodeAndRoundsWindow(self):
        def submitGamemodeAndRounds():
            self.gamemode = gamemode_var.get()
            self.rounds = rounds_var.get()
            root.destroy()

        root = tkinter.Tk()
        root.title('Game Mode and Rounds')
        root.geometry('400x400')
        tkinter.Label(root, text=f'Ok, {self.name}, you are ready for a round of Scissor-Rock-Paper?').pack(pady=10)
        tkinter.Label(root, text='Do you prefer the normal version or the extended version?').pack(pady=5)
        gamemode_var = tkinter.StringVar(value='n')
        tkinter.Radiobutton(root, text='Normal', variable=gamemode_var, value='n').pack()
        tkinter.Radiobutton(root, text='Extended', variable=gamemode_var, value='e').pack()
        # The window contains radio buttons to allow the user to choose between different options.
        tkinter.Label(root, text='Which number of rounds does the winner have to win:').pack(pady=10)
        rounds_var = tkinter.StringVar(value='2')
        tkinter.Radiobutton(root, text='2 of 3', variable=rounds_var, value='2').pack()
        tkinter.Radiobutton(root, text='3 of 5', variable=rounds_var, value='3').pack()
        tkinter.Radiobutton(root, text='4 of 7', variable=rounds_var, value='4').pack()
        submit_button = tkinter.Button(root, text='Submit', command=submitGamemodeAndRounds)
        submit_button.pack(pady=10)
        root.mainloop()

    def returnGamemode(self):
        return self.gamemode

    def returnRounds(self):
        return self.rounds

    def playerHandExtended(self):
        root = tkinter.Tk()
        root.title(
            'Scissor, Rock, Paper, Lizard, Spock')  # Main window is created with title 'Scissor, Rock, Paper, Lizard, Spock'.
        # Layout: frame widget is  placed in the main window. Inside this frame, a label with the text "Make your Choice:" is added.
        frame = tkinter.Frame(root)
        frame.pack(pady=20)
        tkinter.Label(frame, text='Make your Choice:').pack()

        buttons = ['1: Scissors', '2: Paper', '3: Rock', '4: Lizard', '5: Spock']
        for each_button in buttons:
            # tkinter.Button(frame, text=each_button, width=10, command=lambda:self.returnChosenPlayerHand(each_button, root)).pack(side=tkinter.LEFT, padx=5)
            tkinter.Button(frame, text=each_button, width=10,
                           command=lambda each_button=each_button: self.returnChosenPlayerHand(each_button, root)).pack(
                side=tkinter.LEFT, padx=5)
        root.mainloop()  # start of loop

    def playerHandNormal(self):
        root = tkinter.Tk()
        root.title('Scissor, Rock, Paper')  # Main window is created with title 'Scissor, Rock, Paper, Lizard, Spock'.
        # Layout: frame widget is  placed in the main window. Inside this frame, a label with the text "Make your Choice:" is added.
        frame = tkinter.Frame(root)
        frame.pack(pady=20)
        tkinter.Label(frame, text='Make your Choice:').pack()

        buttons = ['1: Scissors', '2: Paper', '3: Rock']
        for each_button in buttons:
            tkinter.Button(frame, text=each_button, width=10,
                           command=lambda each_button=each_button: self.returnChosenPlayerHand(each_button, root)).pack(
                side=tkinter.LEFT, padx=5)
        root.mainloop()  # start of loop

    def returnChosenPlayerHand(self, hand, root):  # Method to return the chosen hand
        self.chosen_player_hand = hand
        print(f"Chosen hand: {self.chosen_player_hand}")  # To test, prints the selected hand
        root.destroy()  # close the window

    def get_chosen_hand(self):  # Method to get the chosen hand from outside
        return self.chosen_player_hand
