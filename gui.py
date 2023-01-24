import PySimpleGUI as sg
import csvWriter

layout = [
    [sg.Text(csvWriter.GetStandTimeString(),key="TITLE")],
        [sg.Button("OK",button_color="red",visible=False),
        sg.Button("Sit",button_color="blue"),
        sg.Button("Stand",button_color="green")],
        [sg.Button("Get Stand Time")]
    ]

# layout = [
#     [sg.Text("Image Folder"),
#      sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
#      sg.FolderBrowse(),],
#     [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
# ]
# Create the window

# Create an event loop
def CreateGUI(): 
    csvWriter.LogAction("Start")
    window = sg.Window("Demo", layout,margins=(100, 50),keep_on_top=True)
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            csvWriter.LogAction("End")
            break
        if event == "Sit":
            csvWriter.LogAction("Sit")
        if event == "Stand":
            csvWriter.LogAction("Stand")
        if event == "Get Stand Time":
            pass
        window['TITLE'].update(csvWriter.GetStandTimeString())
        window.refresh()
    window.close()
CreateGUI()


