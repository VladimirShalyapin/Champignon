from skimage.io import imread, imshow
import numpy as np

def sig(x):
    # делате все изображение серым
    # make the whole image gray
    image_gray = imread(x, as_gray=True)
    # округляет значения для сигмойды (до 1 знака после запятой или если 0 то до целого числа)
    # rounds values ​​for sigmoid (up to 1 decimal place or if 0 then to an integer)
    na_image_gray = np.around(image_gray, decimals = 3)
    return na_image_gray, image_gray

def image_gray(x):
    # Выбрал два столбца значения в середине  матрицы
    # Selected two columns of value in the middle of the matrix
    na_image_gray_8 = x[:,7]
    na_image_gray_9 = x[:,8]
    na_image_gray_6 = x[5,:]
    na_image_gray_7 = x[6,:]
    sum_na_image_gray_8_9 = np.array(na_image_gray_8 + na_image_gray_9)
    sum_na_image_gray_6_7 = np.array(na_image_gray_6 + na_image_gray_7)
    return sum_na_image_gray_8_9, sum_na_image_gray_6_7

# обработка изображения в серый цвет с помощью функции
# processing the image to gray using the function
f_im, a_im = sig('NAME_FILE.JPG')

# получение значений из функции

# getting values ​​from a function
newimage_gray_8_9, newimage_gray_6_7 = np.array(image_gray(f_im))
s_newimage_gray_8_9 = np.around(sum(newimage_gray_8_9), decimals = 2)
s_newimage_gray_6_7 = np.around(sum(newimage_gray_6_7), decimals = 2)

# первые значения соответстуют сумме значений, третье значение является целевой, диамметр шляпки шампиньона
# the first values ​​correspond to the sum of the values, the third value is the target, the diameter of the champignon cap
ars_ng6_9 = np.array([s_newimage_gray_8_9, s_newimage_gray_6_7, float(5.25)])
print(ars_ng6_9)
