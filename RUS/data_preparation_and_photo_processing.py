from skimage.io import imread, imshow
import numpy as np

# функция подготовки изображения и формирования массива данных

def gray_image(x):
    # переводит все пиксели в оттенки серого
    image_gray = imread(x, as_gray=True)
    # формирует массив данных (decimals = 1, 1 знак после запятой, decimals = 0, целое число)
    # нам необходимо значение округленное до тысячных
    na_image_gray = np.around(image_gray, decimals = 3)
    return na_image_gray, image_gray

# в функцию размещается обрабатываемое изображение 
na_image_gray, image_gray = gray_image('name.JPG')

# формирует массив данных (1, 192) с интревалом занчений от 0.01 до 0.99
r_na_image_gray = (na_image_gray.reshape(1, 192) / 1.02) + 0.01

# округляем значения в массиве до сотых
data = np.around(r_na_image_gray, decimals = 2)

# вводим целевую переменную в наши данных np.insert(np.append(data, []), 'позиция т.е первая'0, 'целевая и известная переменная, она же номер группы'7)
target_data = np.insert(np.append(data, []), 0, 7)

# формируем лист (1, 193) для сохранения его в .csv файл
r_target_data = target_data.reshape(1, 193)
print(r_target_data.shape)

# сохраняем полученные значения и смотрим что получилось 
save_target_data = np.savetxt("target_data.csv", r_target_data, delimiter=",", newline='\n', encoding='ANSI')
load_target_data = np.loadtxt("target_data.csv", delimiter=",")
print(load_target_data)
print(load_target_data.shape)
