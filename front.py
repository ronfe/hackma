import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title("Hack 2018")

# graph_zone = tk.Frame(root, width=400, height=300, highlightbackground='black', highlightcolor='black', highlightthickness=1).pack(padx=10, pady=10, side='left')
canvas = tk.Canvas(root, width=500, height=330, highlightbackground='black', highlightcolor='black', highlightthickness=1)
canvas.grid()

### draw
## A - 165, 165
## B - 25, 305
## D - 305, 165
## E - 305, 25
## F - 165, 305
## C - 305, 305
canvas.create_line(305,25, 25,305, 305,305, 165,165, 165,305)
canvas.create_line(165,165, 305,165)
canvas.create_text(160, 160, text='A')
canvas.create_text(20, 310, text='B')
canvas.create_text(310, 310, text='C')
canvas.create_text(310, 160, text='D')
canvas.create_text(310, 20, text='E')
canvas.create_text(160, 310, text='F')


setting = {
    "A": {
        "B": "3",
        "F": "IV",
        "C": "4",
        "D": "I",
        "E": "1"
    },
    "B": {
        "FC": "I",
        "AE": "1"
    },
    "C": {
        "A": "2",
        "FB": "III"
    },
    "D": {
        "A": "III"
    },
    "E": {
        "AB": "3"
    },
    "F": {
        "A": "II",
        "B": "III",
        "C": "I"
    }
}


operation_zone = tk.Frame(root, width=400, height=200, highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(padx=10, pady=10, sticky='W')

root.mainloop()