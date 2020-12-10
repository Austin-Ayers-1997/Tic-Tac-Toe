import Tkinter as tk
import tic_tac_toe as ttt
from PIL import ImageTk, Image

# Main code to start and place features in the GUI
root_window = tk.Tk()

def startGameHandler():
    """
    Method to handle button clicks from the user in the program
    """
    ttt.play_game()

# List of strings used in the program to aid in readability ---------------------
start_message = "Start playing Tic-Tac-Toe"

# -------------------------------------------------------------------------------

test_button = tk.Button(root_window, text=start_message, padx=50, pady=10, command=startGameHandler)
test_button.grid(row=0, column=0)

cover_image = ImageTk.PhotoImage(Image.open("cover_image.jpg"))
label = tk.Label(image=cover_image)
label.pack()

root_window.title("Austin's Tic-Tac-Toe Game!!")            # Give the window a title
root_window.geometry("500x400")                             # Change the window size of the GUI
root_window.mainloop()                                      # Start the GUI