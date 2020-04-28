from mnist import MNIST
import random
mndata = MNIST('samples')
images, labels = mndata.load_training(r'..\train\train-images-idx3-ubyte')
index = random.randrange(0, len(images))
print(mndata.display(images[index]))