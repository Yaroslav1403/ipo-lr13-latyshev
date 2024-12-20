from PIL import ImageFilter, ImageDraw, ImageFont  #Импортируем необходимые модули из библиотеки PIL

class ImageProcessor:  #Определяем класс ImageProcessor
    def __init__(self, img):  #Метод инициализации
        self.img = img  #Инициализируем переменную для хранения изображения

    def contour(self):  #Метод для применения фильтра контура к изображению
        self.img = self.img.filter(ImageFilter.CONTOUR)  #Применяем фильтр контура к изображению
        return self.img  #Возвращаем обработанное изображение

    def text_var(self):  #Метод для добавления текста к изображению
        size = self.img.size  #Получаем размеры изображения
        draw = ImageDraw.Draw(self.img)  #Создаем объект для рисования на изображении
        font = ImageFont.load_default()  #Загрузка системного шрифта
        text = "Вариант 3"  #Текст для добавления на изображение
        #Вычисляем размер текста с помощью textbbox
        bbox = draw.textbbox((0, 0), text, font = font)  #Вычисляем ограничивающий прямоугольник текста
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]  #Вычисляем ширину и высоту текста
        #Вычисляем координаты для центрирования текста
        text_x = (size[0] - text_width) / 2  #Вычисляем координату x для центрирования текста
        text_y = (size[1] - text_height) / 2  #Вычисляем координату y для центрирования текста
        draw.text((text_x, text_y), text, font = font)  #Рисуем текст на изображении с указанными координатами и шрифтом
        return self.img  #Возвращаем изображение с добавленным текстом
