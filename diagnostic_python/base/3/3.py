import os.path
from PIL import Image

def reflect(path, size, *coordinates):
    if os.path.exists(path):
        image = Image.open(path).convert('RGB')
        count = len(coordinates) # количество вырезаемых квадратов - составляющая длины итогового прямоугольника
        result = Image.new('RGB', (size*count, size*2)) # длина = сторона квадрата * их количество, ширина = два квадрата (второй для зеркального изображения)
        for crd in range(count):
            left_x, left_y = coordinates[crd]
            right_x, right_y = left_x + size, left_y + size
            img = image.crop((left_x, left_y, right_x, right_y)) # для вырезания нужны 2 координаты - верний левый угол и правый нижний
            img_turn = img.transpose(Image.FLIP_TOP_BOTTOM) # отзеркалить - перевернуть относительно 0X
            result.paste(img, (0 + crd*size, 0)) # вставляем на чистый фон вырезанный квадрат (координаты вставки - левый верхний угол)
            result.paste(img_turn, (0 + crd*size, size)) # и сразу же зеркальное отражение
        result.save('city.png')
        result.show()

reflect('towers.png', 150, (70, 0), (0, 150), (350, 110), (650, 250))       
