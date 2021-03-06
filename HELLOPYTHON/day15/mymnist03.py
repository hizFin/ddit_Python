from keras import layers
from keras import models
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_labels.shape)    # (60000,)
print(train_labels[1])       # 0
print(train_images[1])       # 
print(train_images.shape[1]) # 28

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# 신경망에 맞게 바꿔주는 
train_labels = to_categorical(train_labels) # 0~9 숫자를 배열 idx로 표현
test_labels = to_categorical(test_labels)


print(train_labels.shape)   # (60000, 10)
print(train_labels[1])      # [1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]



# 몰라도됨
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# 강화 ( 크게5, 작은 128(?))
model.fit(train_images, train_labels, epochs=5, batch_size=128)
