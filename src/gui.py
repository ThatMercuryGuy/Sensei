from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from VoiceRecording_A import start_recording
import threading
from main import start_application
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Programming\NYAS Fall 2023 Project\src\assets\frame0")

gate = [True]

timer = '00:00:00'
def update_timer():
    
    global timer
    if gate[0]:
        timer = time.strftime('%H:%M:%S', time.gmtime(time.time() - start_time))
        canvas.itemconfig(timer_text, text=timer)
        window.after(1000, update_timer)

def get_annotation_time(start_time: float):
    seconds = (round((time.time() - start_time)))
    return str(seconds) + '.00s'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def start_button():
    gate[0] = True
    timer = '00:00:00'
    canvas.itemconfig(timer_text, text=timer)
    global filename
    filename = time.ctime().replace(':', '.')
    
    global t1
    t1 = threading.Thread(target = start_recording, args = (gate,filename))
    
    global start_time
    start_time = time.time()
    t1.start()

    global stopwatch
    stopwatch = threading.Thread(target = update_timer)
    stopwatch.start()

def annotation():
    ann = entry_1.get("1.0", "end-1c")
    
    ua = open (f'{filename}_ANN.txt', 'a')
    ua.write(f'[{get_annotation_time(start_time)}] {ann}\n')
    ua.close()

def stop_button():
    gate[0] = False

    t1.join()
    stopwatch.join()

    app = threading.Thread(target = start_application, args = (filename,))
    app.start()

window = Tk()

window.geometry("1000x600")
window.configure(bg = "#A3BCF9")


canvas = Canvas(
    window,
    bg = "#EFEFEF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1000.0,
    76.0,
    fill="#1B2021",
    outline="")

canvas.create_text(
    150.0,
    17.0,
    anchor="nw",
    text="Sensei - AI Teaching Assistant",
    fill="#D0D6B3",
    font=("JetBrains Mono", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: start_button(),
    relief="flat"
)
button_1.place(
    x=47.0,
    y=104.0,
    width=311.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: stop_button(),
    relief="flat"
)
button_2.place(
    x=636.0,
    y=104.0,
    width=311.0,
    height=55.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: annotation(),
    relief="flat"
)
button_3.place(
    x=344.0,
    y=472.0,
    width=311.0,
    height=55.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    499.0,
    131.0,
    image=image_image_1
)

timer_text = canvas.create_text(
    385.0,
    104.0,
    anchor="nw",
    text=timer,
    fill="#4D4730",
    font=("JetBrains Mono", 36)
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    497.0,
    402.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=('JetBrains Mono',17,'normal')
)
entry_1.place(
    x=60.0,
    y=343.0,
    width=874.0,
    height=116.0
)
window.resizable(False, False)
window.mainloop()
