import PySimpleGUI as sg
from multiprocessing import Process
from main import start_pygame

sg.theme('BlueMono')

# Define the layout of the window
layout = [
    [sg.Text('Welcome to the game!')],
    [sg.Button('Start Game!', size=(10, 4), font=('Helvetica'))],
    [sg.Button('Quit Game!', size=(10, 4), font=('Helvetica'))],

]

# Create the window
window = sg.Window('Game Startup', layout, size=(600, 400), element_justification='center', background_color='Black')

# Event loop
if __name__ == '__main__':
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Quit Game!':
            print(f"Quitting game...!")
            break

        if event == 'Start Game!':
            game_process = Process(target=start_pygame)
            game_process.start()

    window.close()