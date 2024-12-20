from PIL import Image
from .imageProcessor import *
import os


class ImageHandler():
    def __init__(self):
        self.img = None  
        self.file_path = None  

    def load_image(self,file_path):
        self.img = Image.open(self.file_path)
        
    def re_size(self):
        max_size = (200,200) 
        self.img.thumbnail(max_size) 

    def save_to_file(self, file_path, name):
        self.img.save(self.file_path)  
        os.rename(self.file_path, name)
    
    def countor_load(self):
        filter = ImageProcessor(self.img)
        self.img = filter.contour(self.img)

    def text_var_load(self):
        filter = ImageProcessor(self.img)
        self.img = filter.text_var()
    




                      