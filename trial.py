import tkinter as tk
import time 
import server, theorem


def convert_coordinate(x, y, d=50, q=75):
    nx, ny = q*x, q*y
    return nx +d, 305-ny

def delete_objs(canvas, objs):
    for each in objs:
        canvas.delete(each)
    
    return 0

def make_label(root, clicked_items):
    t = clicked_items[-1]
    temp_label_dueto = tk.Label(root, text='∵  {}'.format(t), anchor='w', justify='left', font=('Times', '16','bold'))
    temp_label_therefore = tk.Label(root, text='∴  ', anchor='w', justify='left', font=('Times', '16','bold'))
    return temp_label_dueto, temp_label_therefore


def grid_label(root, clicked_items, stored_labels):
    this_label_dueto, this_label_therefore = make_label(root, clicked_items)
    stored_labels.append(this_label_dueto)
    this_label_dueto.grid(column=3, row=len(stored_labels)+ 1, columnspan=4)

    stored_labels.append(this_label_therefore)
    this_label_therefore.grid(column=3, row=len(stored_labels)+ 1)
    return 


def update_preview(preview, logs):
    x = logs[-1]
    t_dueto = ','.join([t['label'] for t in x['dueto']])
    dueto = tk.Label(preview, text= '∵ {}'.format(t_dueto))
    therefore = tk.Label(preview, text='∴ {}'.format(x['therefore'][0]['label']))

    dueto.grid(row=2*len(logs)+6, column=3, columnspan=5)
    therefore.grid(row=2*len(logs)+7, column=5, columnspan=5)



def add_therefore_input(root, row, column, symbol):
    left_entry = tk.Entry(root)
    symbol_label = tk.Label(root, text=symbol)
    right_entry = tk.Entry(root)

    left_entry.grid(row=row, column=column)
    symbol_label.grid(row=row, column=column+1)
    right_entry.grid(row=row, column=column+2)


def add_button(root, column, candidates=['∥', '⊥', '=', '∠=']):
    buttons = list()
    for i, candidate in enumerate(candidates):
        buttons.append(tk.Button(root, text=' {} '.format(candidate), command=lambda k=i, j=candidate: add_therefore_input(root, k+1, column-4, candidate)))
        buttons[-1].grid(column=column, row=i+1)
    
    return buttons


def make_canvas(root, points, row=0, column=0):
    canvas = tk.Canvas(root, width=400, height=330)
    canvas.grid(row=row+1, column=column, rowspan=10, sticky='n')
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

def change_dueto_text(text, dueto_label):
    if len(text) == 1:
        dueto_label['text'] = text[-1]
        return 

    dueto_label['text'] +=  ', ' +text[-1]
    return

def change_symbol(v):
    global symbol
    symbol = v



def confirm_content(dueto, therefore, user_logs, theorems, choices, choice_listbox, canvas, points, clicked_term, preview, dueto_frame):

    # therefore = s_therefore[-1]

    # type
    s_type = None
    if len(dueto) == 0:
        return 
    
    s_dueto = list()
    for sd in dueto:
        for each in theorems:
            if each['label'] == sd:
                s_dueto.append(each)
    

    if therefore[1] == '∥':
        s_type = '101'
    if therefore[1] == '⊥':
        s_type = '102'
    if therefore[1] == '=':
        if therefore[0][0] == '∠':
            s_type = '301'
        else:
            s_type = '201'

    s_label = ''.join(therefore)
    
    # elems
    s_elems = list()

    if therefore[0][0] == '∠':
        s_elems.append(therefore[0][-3:])
    else:
        s_elems.append(therefore[0])
    
    if '+' in therefore[2]:
        temp_elem = therefore[2].split('+')
        # temp_elem = [t.strip() for t in temp_elem]
        for i, each in enumerate(temp_elem):
            if each[0] == '∠':
                temp_elem[i] = each[1:]
        
        s_elems.append(''.join(temp_elem))
    
    elif therefore[2][0] == '∠':
        s_elems.append(therefore[2][-3:])
    else:
        s_elems.append(therefore[2])

    s_therefore = [{
        'type': s_type,
        'elems': s_elems,
        'label': s_label
    }]

    step_log = {
        "dueto": s_dueto,
        "therefore": s_therefore
    }

    user_logs.append(step_log)
    theorems.append(s_therefore[0])

    x = tk.Button(choice_listbox, text=s_therefore[0]['label'], command= lambda k=s_therefore: highlight(
            canvas=canvas, 
            points=points, 
            obj=k[0]['elems'], 
            label=k[0]['label'],
            ct = clicked_term
            ))
    x.grid(row=len(choices)+1, column=1)
    choices.append(x)

    update_preview(preview, user_logs)

    dueto_frame['text'] = ''
    for t in dueto[::-1]:
        dueto.remove(t)


def rate(logs, root):
    x = server.rater(logs, theorem.setting)
    score = tk.Label(root, text='您的得分是： {}\n 每一步得分: {}'.format(x['score'], x['correct']))
    score.grid(row=4, column=7)



def main():
    user_logs = list()
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

    tk.Label(root, text='如图，已知 ∠EAC 是 △ABC 的外角，AD 平分 ∠EAC ，且 AD ∥ BC \n 求证：∠ABC = ∠BCA', font=('Times', '16', 'bold')).grid(row=0, column=0, padx=10, pady=10, sticky='nw')

    canvas = make_canvas(root, points)
    #canvas_2 = make_canvas(root, points, row=11)

    # temp_line = canvas.create_line(points['B'][0], points['B'][1], points['C'][0], points['C'][1], fill='purple', width=5)
    # canvas.after(4000, canvas.delete, temp_line)
    
    # given_frame = tk.Frame(root, width=250, height=330, highlightbackground='black', highlightcolor='black', highlightthickness=1).grid(row=0, column=1, sticky='n')
    # condition_frames = insert_given(theorems, given_frame)

    given_listbox = tk.Listbox(root, highlightbackground='black', highlightcolor='black', highlightthickness=1)
    given_listbox.grid(row=1, column=1, rowspan=15, sticky='n')
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
            ))
        x.grid(row=i+1, column=1, sticky='w', padx=10)
        choices.append(x)
    
    

    content_listbox =tk.Listbox(root,highlightbackground='black',highlightcolor='black',highlightthickness=1, width=60)
    content_listbox.grid(row=1, column=3, rowspan=2, columnspan=5, sticky='n')

    tk.Label(content_listbox, text='∵ ').grid(row=2, column=3, sticky='w')
    tk.Label(content_listbox, text='∴ ').grid(row=3, column=3, sticky='w')

    dueto = tk.Label(content_listbox, text='')
    dueto.grid(row=2, column=4, columnspan=4, sticky='w')


    right_arrow = tk.Button(root, text='>>>', command= lambda : change_dueto_text(clicked_term, dueto))
    right_arrow.grid(row=1, column=2, sticky='n')

    ### therefore grid
    left_input = tk.Entry(content_listbox)
    right_input = tk.Entry(content_listbox)

    symbol = '='
    optionList = ('∥', '⊥', '=')
    v = tk.StringVar()
    v.set(optionList[2])
    om = tk.OptionMenu(content_listbox, v, *optionList, command=change_symbol)
    
    left_input.grid(row=3, column=4, sticky='n')
    om.grid(row=3, column=5, sticky='n')
    right_input.grid(row=3, column=6, sticky='n')

    


    ### Preview frame
    preview_frame = tk.Listbox(root, highlightbackground='black', highlightcolor='black', highlightthickness=1, height=30, width=45)
    preview_frame.grid(row=10, rowspan=5, column=3, columnspan=5)


    # confirmation
    confirm_button = tk.Button(content_listbox, text='确定', command=lambda : confirm_content(clicked_term, [left_input.get(), symbol, right_input.get()], user_logs, theorems, choices, given_listbox, canvas, points, clicked_term, preview_frame, dueto))
    confirm_button.grid(row=4, column=6, sticky='se')

    submit_button = tk.Button(root, text='提交', command=lambda : rate(user_logs, root), font=('Times', '18', 'bold'), highlightcolor='black', highlightthickness=1, height=3,width=8)
    submit_button.grid(row=22, column=5, sticky='sw', columnspan=4)
    

    
    

    # drag_listbox =tk.Listbox(root,highlightbackground='black',highlightcolor='black',highlightthickness=1)
    # drag_listbox.grid(row=1,column=3,rowspan=10)

    # right_arrow=tk.Button(root,text='>>>', command=lambda : grid_label(drag_listbox, clicked_term, stored_labels)).grid(row=1,column=2)

    # drag_listbutton = tk.Listbox(root,highlightbackground='black',highlightcolor='black',highlightthickness=1)
    # drag_listbutton.grid(row=1,column=8,rowspan=10)
    
    # symbol_buttons = add_button(drag_listbutton, 4)
    root.iconbitmap('favicon.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
