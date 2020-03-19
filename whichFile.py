"""
whichFileCSV.py is a reusable module that uses tkinter to produce a GUI for
the user to more easily select a file.
GUI search and click returns a file

Matt Hannan
12/3/2019

Updated 2/14/2020:

Takes a string to describe which file to select, as well as the file type.
    whichFile.select("Select Anne's ATM list", "xlsx")

"""

from tkinter import filedialog, Tk
import os


def select(title, file_type):
    # Build File Type stuff
    ft1 = file_type.upper() + " files"
    ft2 = "*." + file_type
    # Build the window
    Tk().withdraw()  # .withdraw() hides that second blank window

    # This sets to the users home directory
    init_dir = os.path.expanduser("~")

    # Fire up the GUI and get the users selection
    selected_file = filedialog.askopenfilename(
        initialdir=init_dir,
        title=title,
        filetypes=((ft1, ft2), ("All Files", "*.*"))
        )
    return selected_file
