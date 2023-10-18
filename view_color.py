"""A mini program which takes a
color value and displays it graphically"""

import tkinter as tk
import pyperclip


def display(color_name="White",
            color_hex="#FFFFFF",
            color_rgb="255,255,255"):
    """Displays a color passed as argument"""
    window = tk.Tk()
    window.geometry("350x350+500+200")
    window.title(color_name)
    window.resizable(False, False)
    window.config(bg="silver")
    window.iconbitmap("python_icon.ico")

    def copy_rgb():
        pyperclip.copy(color_rgb)
        print("RGB Copied!")

    def copyhex():
        pyperclip.copy(color_hex)
        print("HEX Copied!")

    # color box
    colorbox_frame = tk.Frame(window)
    colorbox_frame.config(bg=color_hex, width=324, height=200)
    colorbox_frame.config(relief="groove", border=1)
    colorbox_frame.place(x=13, y=13)

    # Color details Box
    color_detail_frame = tk.Frame(window)
    color_detail_frame.config(bg="#f0f0f0", width=324, height=115)
    color_detail_frame.place(x=13, y=213)

    # Color Title Label
    color_title = tk.Label(
        color_detail_frame, text=color_name, font=("segoe ui", 15))
    color_title.config(bg="#f0f0f0")
    color_title.config(width=28)
    color_title.place(x=4, y=4)

    # RGB Row
    rgb_label = tk.Label(color_detail_frame,
                         text=f"Rgb: ({color_rgb})", font=("segoe ui", 13))
    rgb_label.config(width=18, bg="#f0f0f0", anchor="w")
    rgb_label.place(x=25, y=42)

    rgb_button = tk.Button(color_detail_frame, text="Copy Rgb")
    rgb_button.config(font=("segoe ui", 10))
    rgb_button.config(activebackground="#9e9e9e", activeforeground="#212121", relief="ridge",
                      cursor="hand2", command=copy_rgb)
    rgb_button.place(x=242, y=43)

    # HEX Row
    hex_label = tk.Label(color_detail_frame,
                         text=f"Hex: {color_hex}", font=("segoe ui", 13))
    hex_label.config(width=18, bg="#f0f0f0", anchor="w")
    hex_label.place(x=25, y=77)

    hex_button = tk.Button(color_detail_frame, text="Copy Hex")
    hex_button.config(font=("segoe ui", 10))
    hex_button.config(activebackground="#9e9e9e", activeforeground="#212121", relief="ridge",
                      cursor="hand2", command=copyhex)
    hex_button.place(x=242, y=80)

    window.mainloop()


if __name__ == "__main__":
    display()
