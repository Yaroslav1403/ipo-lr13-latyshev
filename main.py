from PIL import Image
from imag.imageFunction import Imagine
import tkinter as tk

class Application(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.title('Фото - редактор')
        first_label = tk.Label(self, text = "Фото", font = 20) 
        first_label.pack(padx = 4, pady = 4) 
        self.image_handler = Imagine(master = self) 
        self.image_handler.pack(pady = 10, padx = 10) 
        
app = Application() 
app.mainloop() 

