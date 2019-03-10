import PySimpleGUIWeb as sg

print('Starting up...')

layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', size=(10,1), key='_OUTPUT_') ],
          [sg.Input(key='_IN_')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title').Layout(layout)
while True:                 # Event Loop
  print('event loop')
  event, values = window.Read()
  if event in (None, 'Exit'):
    break
  elif event == 'Show':
    window.Element('_OUTPUT_').Update(values['_IN_'])
  print(event, values)


window.Close()
