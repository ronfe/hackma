import tkinter as tk
import math 


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.canvas = tk.Canvas(width=400, height=400)
        self.canvas.pack(fill="both", expand=True)

        self._create_token((100, 100), "white")
        self._create_token((200, 300), "pink")
        self._create_arc((100,100), (200, 300))

    def _create_token(self, coord, color):
        '''Create a token at the given coordinate in the given color'''
        (x,y) = coord
        self.canvas.create_oval(x-5, y-5, x+5, y+5, 
                                outline=color, fill=color, tags="token")

    def _create_arc(self, p0, p1):
        extend_x = (self._distance(p0,p1) -(p1[0]-p0[0]))/2 # extend x boundary 
        extend_y = (self._distance(p0,p1) -(p1[1]-p0[1]))/2 # extend y boundary
        startAngle = math.atan2(p0[0] - p1[0], p0[1] - p1[1]) *180 / math.pi # calculate starting angle  
        self.canvas.create_arc(p0[0]-extend_x, p0[1]-extend_y , 
                               p1[0]+extend_x, p1[1]+extend_y, 
                               extent=180, start=90+startAngle, style=tk.ARC)

        '''use this rectangle for visualisation'''
        #self.canvas.create_rectangle(p0[0]-extend_x, p0[1]-extend_y, 
        #                                p1[0]+extend_x, p1[1]+extend_y)       

    def _distance(self, p0, p1):
        '''calculate distance between 2 points'''
        return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)   

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()