###########################################################
########### MIT license 2022 Vladimir Shalyapin ###########
###########            Python   v 3.8           ###########
###########################################################
 
# Импорт необходимых библиотек
from skimage.io import imread, imshow
from skimage.transform import resize
import matplotlib.pyplot as plt
 
# Загружаем файл и его размер
image = imread('namefile.JPG')
print(image.shape)
 
# Визуализация исходного изображения
plt.imshow(image)
plt.show()
 
# Изменение размеров до необходимого 16*12 px, по средствам изменения // 77 и // 124
image_resized = resize(image, (image.shape[0] // 77, image.shape[1] // 124), anti_aliasing=True)
 
# Визуализация полученного изображения
print(image_resized.shape)
plt.imshow(image_resized)
plt.show()

# Сохраняем результат преобразования
plt.imsave('new_namefile.JPG', image_resized)
