import tkinter as tk
import time 


def convert_coordinate(x, y, d=50, q=75):
    nx, ny = q*x, q*y
    return nx +d, 305-ny

def delete_objs(canvas, objs):
    for each in objs:
        canvas.delete(each)
    
    return 0

def make_label(root, clicked_items):
    t = clicked_items[-1]
    temp_label = tk.Label(root, text=t)
    return temp_label


def grid_label(root, clicked_items, stored_labels):
    this_label = make_label(root, clicked_items)
    stored_labels.append(this_label)
    this_label.grid(column=3, row=len(stored_labels)+ 1)
    return 


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
    label = kwargs['label']
    ct = kwargs['ct']

    ct.append(label)
    

    highlighted = list()

    for x,*z, y in obj:
        if x == '△':
            z1,z2 = z
            temp_line = canvas.create_line(points[z1][0], points[z1][1], points[z2][0], points[z2][1], fill='purple', width=5)
            highlighted.append(temp_line)

            temp_line = canvas.create_line(points[z2][0], points[z2][1], points[y][0], points[y][1], fill='purple', width=5)
            highlighted.append(temp_line)

            temp_line = canvas.create_line(points[z1][0], points[z1][1], points[y][0], points[y][1], fill='purple', width=5)
            highlighted.append(temp_line)
        elif len(z) == 0:
            temp_line = canvas.create_line(points[x][0], points[x][1], points[y][0], points[y][1], fill='purple', width=5)
            highlighted.append(temp_line)
        else:
            z = z[0]

            ## STEP 1
            # (x0, y0), (x1,y1) = x+z, z+y

            ## STEP 2
            

            ## STEP 3
            temp_arc = canvas.create_line(points[x][0], points[x][1], points[z][0], points[z][1],  fill='green', width=5)
            temp_arc_2 = canvas.create_line(points[z][0], points[z][1], points[y][0], points[y][1],  fill='green', width=5)

            highlighted += [temp_arc, temp_arc_2]
    
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
        "elems": ["AD", "EAC"],
        "label": "AD是∠EAC的角平分线"
    },
        {
            "type": "101",
            "elems": ["AD", "BC"],
            "label": "AD∥BC"
        },
        {
            "type": "102",
            "elems": ["AF", "BC"],
            "label": "AF⊥BC"
        },
        {
            "type": "306",
            "elems": ["EAC", "△ABC"],
            "label": "∠EAC 是 △ABC 的外角"
        }
    ]

    root = tk.Tk()
    root.geometry('2048x1024')
    root.title("Hack 2018")

    canvas = make_canvas(root, points)
    #canvas_2 = make_canvas(root, points, row=11)

    # temp_line = canvas.create_line(points['B'][0], points['B'][1], points['C'][0], points['C'][1], fill='purple', width=5)
    # canvas.after(4000, canvas.delete, temp_line)
    
    # given_frame = tk.Frame(root, width=250, height=330, highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=0, column=1, sticky='n')
    # condition_frames = insert_given(theorems, given_frame)

    given_listbox = tk.Listbox(root, highlightbackground='black', highlightcolor='black', highlightthickness=1)
    given_listbox.grid(row=1, column=1, rowspan=5)
    choices = list()
    clicked_term = list()
    stored_labels = list()

    for i, each in enumerate(theorems):
        x = tk.Button(given_listbox, text=each['label'], command= lambda k=each: highlight(
            canvas=canvas, 
            points=points, 
            obj=k['elems'], 
            label=k['label'],
            ct = clicked_term
            )).grid(row=i+1, column=1)
        choices.append(x)
    

    drag_listbox =tk.Listbox(root,highlightbackground='black',highlightcolor='black',highlightthickness=1)
    drag_listbox.grid(row=1,column=3,rowspan=10)
    add_button=tk.Button(root,text='>>>', command=lambda : grid_label(drag_listbox, clicked_term, stored_labels)).grid(row=1,column=2)
   
    root.mainloop()


if __name__ == '__main__':
    main()
