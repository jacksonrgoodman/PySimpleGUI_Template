import PySimpleGUI as sg


layout = [[sg.Text('Text Input:'), sg.Input(key='-IN-')],
          [sg.Text('Output goes here:', key='-OUT-')],
          [sg.Button('OK'), sg.Button('Exit')]]

window = sg.Window('Program1', layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    window['-OUT-'].update('Output goes here: '+values['-IN-'])

window.close()
