
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def principal_window():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"/home/rado/workspace/is-live-on-twitch-linux/Views/build/assets/frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("579x434")
    window.configure(bg = "#FFFFFF")

    def retrieve_input():
        global user_input 
        user_input = entry_1.get()

        print(user_input)

        return user_input

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 434,
        width = 579,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        579.0,
        434.0,
        fill="#2A2929",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        289.5,
        217.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=139.0,
        y=198.0,
        width=301.0,
        height=37.0
    )

    canvas.create_text(
        139.0,
        171.0,
        anchor="nw",
        text="Streamer username",
        fill="#FFFFFF",
        font=("Battambang Regular", 15 * -1)
    )

    button_image_1 = PhotoImage( 
        file=relative_to_assets("button_1.png"))

    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: retrieve_input(),
        relief="flat"
    )
    button_1.place(
        x=209.0,
        y=274.0,
        width=161.0,
        height=60.0
    )

    canvas.create_text(
        57.0,
        97.0,
        anchor="nw",
        text="IS LIVE ON TWITCH?",
        fill="#FFFFFF",
        font=("RobotoRoman Bold", 48 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

    return user_input
