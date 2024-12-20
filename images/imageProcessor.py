from PIL import ImageFilter, ImageDraw

class ImageProcessor:
    def __init__(self, img):
        self.img = img  

    def contour(self, img):
        self.img = self.img.filter(ImageFilter.CONTOUR) 
        return self.img  


    def text_var(self):
        size = self.img.size
        draw = ImageDraw.Draw(self.img)
        draw.text((size[0]/2,size[1]/2), 'option 3 ', fill = ('#1C0606'))
        return self.img
