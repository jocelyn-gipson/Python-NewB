import tkinter as tk

    




#root.mainloop()




root = tk.Tk()

imgpath = 'Artboard.png'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
tk.Button(root, text="Hello World", command=SimpleApp.draw).pack()

class SimpleApp(object):
    #spin image
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=1270, height=688)
        self.canvas.pack()
        self.canvas.create_image(640, 345, image=photo)
        
        self.update = self.spin().__next__
        master.after(500, self.update)

    #spin function
    def spin(self):
        image = Image.open("small1.png")
        angle = 0
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(1025, 240, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle += 10
            angle %= 360





        
    
app = SimpleApp(root, 'C:/Users/cycle/Desktop/small1.png')


root.mainloop()
