import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import filedialog as fd
from tkinter import simpledialog
from PIL import Image, ImageTk
from .imageHandler import ImageHandler

class Imagine(tk.Frame,ImageHandler):
    def __init__(self, master=None):
        super().__init__(master)
        self.initUI()

    def initUI(self):
        self.pack()
        
        ttk.Button(self, text = 'Файл', command = self.load_image_gui).pack(fill = tk.X)
        ttk.Button(self, text = 'Размер', command = self.re_size_gui).pack(fill = tk.X)
        ttk.Button(self, text = 'Сохранить', command = self.save_to_file_gui).pack(fill = tk.X)
        ttk.Button(self, text = 'Контур', command = self.contour_gui).pack(fill = tk.X)
        ttk.Button(self, text = 'Текст', command = self.text_var_load_gui).pack(fill = tk.X)
 
        self.label_photo = ttk.Label(self)
        self.label_photo.pack(pady = 20)
    
    def load_image_gui(self):
        self.file_path = fd.askopenfilename(title = "Выберите фото для редактирования", filetypes = [("Image Files", "*.png;*.jpg;*.jpeg;*")]) 
        try:
            self.load_image(self.file_path)
            self.update_label(self.img) 
        except:
            showerror("Ошибка", "Не удалось открыть фото") 

    def update_label(self, img):
        self.img_tk = ImageTk.PhotoImage(img) 
        self.label_photo.config(image = self.img_tk)  

    def re_size_gui(self):
        self.re_size()
        self.update_label(self.img) 
    
    def contour_gui(self):
        self.countor_load()
        self.update_label(self.img) 

    def save_to_file_gui(self):
        name = simpledialog.askstring("Введите название файла", "Название файла")
        try:
            self.save_to_file(self.file_path, name)
        except:
             showerror("Ошибка", "Не удалось Сохранить изображение") 
    
    def text_var_load_gui(self):
        self.text_var_load()
        self.update_label(self.img) 


