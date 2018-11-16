import tkinter as tk
import time 


def convert_coordinate(x, y, d=50, q=75):
    nx, ny = q*x, q*y
    return nx +d, 305-ny

def add_one(a,b):
    return a+b+1

def add_two(a, b):
    return a+b+2

def make_canvas(root, points, row=0, column=0):
    canvas = tk.Canvas(root, width=400, height=330)
    canvas.grid(row=row, column=column, rowspan=10, sticky='n')
    canvas.create_rectangle(5,5,400,330,outline='black')
    

    #flat_list = [item for sublist in [points['E'], points['B'],points['C'], points['A'],points['D']] for item in sublist]

    canvas.create_line(points['E'][0], points['E'][1], points['B'][0], points['B'][1], points['C'][0], points['C'][1], points['A'][0], points['A'][1], points['D'][0], points['D'][1])
    canvas.create_line(points['A'][0], points['A'][1], points['F'][0], points['F'][1])

    offset = 10

    for c in ['A', 'B', 'C', 'D', 'E', 'F']:
        canvas.create_text(points[c][0]-offset, points[c][1]+offset, text=c, font=('Times', '16', 'bold italic'))
    
    return canvas


def highlight(**kwargs):
    canvas = kwargs['canvas']
    points = kwargs['points']
    temp_line_1 = canvas.create_line(points['B'][0], points['B'][1], points['C'][0], points['C'][1], fill='purple', width=5)
    temp_line_2 = canvas.create_line(points['A'][0], points['A'][1], points['D'][0], points['D'][1], fill='purple', width=5)

    canvas.after(4000, canvas.delete, temp_line_1)
    canvas.after(4000, canvas.delete, temp_line_2)
    return 

def main():
    points = {
        "A": convert_coordinate(1,2),
        "B": convert_coordinate(0,0),
        "C": convert_coordinate(2,0),
        "D": convert_coordinate(2,2),
        "E": convert_coordinate(1.5, 3),
        "F": convert_coordinate(1,0)
    }
    theorems = [
        'AD∥BC',
        'XYXYXYX',
        '1234567'
    ]

    root = tk.Tk()
    root.geometry('2048x1024')
    root.title("Hack 2018")

    canvas = make_canvas(root, points)
    canvas_2 = make_canvas(root, points, row=11)

    # temp_line = canvas.create_line(points['B'][0], points['B'][1], points['C'][0], points['C'][1], fill='purple', width=5)
    # canvas.after(4000, canvas.delete, temp_line)
    
    # given_frame = tk.Frame(root, width=250, height=330, highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=0, column=1, sticky='n')
    # condition_frames = insert_given(theorems, given_frame)

    given_listbox = tk.Listbox(root, highlightbackground='black', highlightcolor='black', highlightthickness=1)
    given_listbox.grid(row=0, column=1, rowspan=5)
    choices = list()
    for i, each in enumerate(theorems):
        x = tk.Button(given_listbox, text=each, command=lambda: highlight(canvas=canvas_2, points=points)).grid(row=i+1, column=1)
        choices.append(x)

    root.mainloop()


if __name__ == '__main__':
    main()
