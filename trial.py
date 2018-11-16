import tkinter as tk
import time 


def convert_coordinate(x, y, d=50, q=75):
    nx, ny = q*x, q*y
    return nx +d, 305-ny

def delete_objs(canvas, objs):
    for each in objs:
        canvas.delete(each)
    
    return 0

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
    obj = kwargs['obj']


    highlighted = list()

    for x,y in obj:
        temp_line = canvas.create_line(points[x][0], points[x][1], points[y][0], points[y][1], fill='purple', width=5)
        highlighted.append(temp_line)
    
    canvas.after(4000, delete_objs, canvas,highlighted)
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
    theorems = [{
        "type": "311",
        "elems": ["AD", "EA"],
        "label": "AD是∠EAC的角平分线"
    },
        {
            "type": "101",
            "elems": ["AD", "BC"],
            "label": "AD∥BC"
        }
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
        x = tk.Button(given_listbox, text=each['label'], command= lambda k=each: highlight(canvas=canvas, points=points, obj=k['elems'])).grid(row=i+1, column=1)
        choices.append(x)

    root.mainloop()


if __name__ == '__main__':
    main()
