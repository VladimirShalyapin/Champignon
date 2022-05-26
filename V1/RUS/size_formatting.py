###########################################################
########### MIT license 2022 Vladimir Shalyapin ###########
###########            Python   v 3.8           ###########
###########################################################
 
# импорт необходимых библиотек
from skimage.io import imread, imshow
from skimage.transform import resize
import matplotlib.pyplot as plt
 
# загружаем файл и его размер
image = imread('namefile.JPG')
print(image.shape)
 
# визуализация исходного изображения
plt.imshow(image)
plt.show()
 
# изменение размеров до необходимого 16*12 px, по средствам изменения // 77 и // 124
image_resized = resize(image, (image.shape[0] // 77, image.shape[1] // 124), anti_aliasing=True)
 
# визуализация полученного изображения
print(image_resized.shape)
plt.imshow(image_resized)
plt.show()

# сохраняем результат преобразования
plt.imsave('new_namefile.JPG', image_resized)
