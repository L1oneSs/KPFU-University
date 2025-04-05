"""
# Bringing in tensorflow
import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# Brining in tensorflow datasets for fashion mnist
import tensorflow_datasets as tfds
# Bringing in matplotlib for viz stuff
from matplotlib import pyplot as plt

# Use the tensorflow datasets api to bring in the data source
ds = tfds.load('cifar10', split='train')

ds.as_numpy_iterator().next()['label']

# Do some data transformation
import numpy as np

# Setup connection aka iterator
dataiterator = ds.as_numpy_iterator()

# Getting data out of the pipeline
dataiterator.next()['image']

# Setup the subplot formatting
fig, ax = plt.subplots(ncols=4, figsize=(20, 20))
# Loop four times and get images
for idx in range(4):
    # Grab an image and label
    sample = dataiterator.next()
    # Plot the image using a specific subplot
    ax[idx].imshow(np.squeeze(sample['image']))
    # Appending the image label as the plot title
    ax[idx].title.set_text(sample['label'])


# Scale and return images only
def scale_images(data):
    image = data['image']
    return image / 255


# Reload the dataset
ds = tfds.load('cifar10', split='train')
# Running the dataset through the scale_images preprocessing step
ds = ds.map(scale_images)
# Cache the dataset for that batch
ds = ds.cache()
# Shuffle it up
ds = ds.shuffle(60000)
# Batch into 128 images per sample
ds = ds.batch(128)
# Reduces the likelihood of bottlenecking
ds = ds.prefetch(64)

ds.as_numpy_iterator().next().shape

# Bring in the sequential api for the generator and discriminator
from keras.models import Sequential
# Bring in the layers for the neural network
from keras.layers import Conv2D, Dense, Flatten, Reshape, LeakyReLU, Dropout, UpSampling2D


def build_generator():
    model = Sequential()

    # Takes in random values and reshapes it to 7x7x128
    # Beginnings of a generated image
    model.add(Dense(8 * 8 * 128, input_dim=128))  # Изменение размерности
    model.add(LeakyReLU(0.2))
    model.add(Reshape((8, 8, 128)))  # Изменение размерности

    # Upsampling block 1
    model.add(UpSampling2D())
    model.add(Conv2D(128, 5, padding='same'))
    model.add(LeakyReLU(0.2))

    # Upsampling block 2
    model.add(UpSampling2D())
    model.add(Conv2D(128, 5, padding='same'))
    model.add(LeakyReLU(0.2))

    # Convolutional block 1
    model.add(Conv2D(128, 5, padding='same'))  # Изменение размерности
    model.add(LeakyReLU(0.2))

    # Convolutional block 2
    model.add(Conv2D(3, 5, padding='same', activation='sigmoid'))  # Изменение количества каналов

    return model


generator = build_generator()

generator.summary()

# Generate new fashion
img = generator.predict(np.random.randn(4, 128, 1))
print(img.shape)
# Setup the subplot formatting
fig, ax = plt.subplots(ncols=4, figsize=(20, 20))
# Loop four times and get images
for idx, img in enumerate(img):
    # Plot the image using a specific subplot
    ax[idx].imshow(np.squeeze(img))
    # Appending the image label as the plot title
    ax[idx].title.set_text(idx)


def build_discriminator():
    model = Sequential()

    # First Conv Block
    model.add(Conv2D(32, 5, input_shape=(32, 32, 3)))  # Изменение размерности
    model.add(LeakyReLU(0.2))
    model.add(Dropout(0.4))

    # Second Conv Block
    model.add(Conv2D(64, 5))
    model.add(LeakyReLU(0.2))
    model.add(Dropout(0.4))

    # Third Conv Block
    model.add(Conv2D(128, 5))
    model.add(LeakyReLU(0.2))
    model.add(Dropout(0.4))

    # Fourth Conv Block
    model.add(Conv2D(256, 5))
    model.add(LeakyReLU(0.2))
    model.add(Dropout(0.4))

    # Flatten then pass to dense layer
    model.add(Flatten())
    model.add(Dropout(0.4))
    model.add(Dense(1, activation='sigmoid'))

    return model


discriminator = build_discriminator()

discriminator.summary()
img = img[0]
img.shape
img = generator.predict(np.random.randn(4, 128, 1))
discriminator.predict(img)

# Adam is going to be the optimizer for both
from keras.optimizers import Adam
# Binary cross entropy is going to be the loss for both
from keras.losses import BinaryCrossentropy

g_opt = Adam(learning_rate=0.0001)
d_opt = Adam(learning_rate=0.00001)
g_loss = BinaryCrossentropy()
d_loss = BinaryCrossentropy()

# Importing the base model class to subclass our training step
from keras.models import Model


class FashionGAN(Model):
    def __init__(self, generator, discriminator, *args, **kwargs):
        # Pass through args and kwargs to base class
        super().__init__(*args, **kwargs)

        # Create attributes for gen and disc
        self.generator = generator
        self.discriminator = discriminator

    def compile(self, g_opt, d_opt, g_loss, d_loss, *args, **kwargs):
        # Compile with base class
        super().compile(*args, **kwargs)

        # Create attributes for losses and optimizers
        self.g_opt = g_opt
        self.d_opt = d_opt
        self.g_loss = g_loss
        self.d_loss = d_loss

    def train_step(self, batch):
        # Get the data
        real_images = batch
        fake_images = self.generator(tf.random.normal((128, 128, 1)), training=False)

        # Train the discriminator
        with tf.GradientTape() as d_tape:
            # Pass the real and fake images to the discriminator model
            yhat_real = self.discriminator(real_images, training=True)
            yhat_fake = self.discriminator(fake_images, training=True)
            yhat_realfake = tf.concat([yhat_real, yhat_fake], axis=0)

            # Create labels for real and fakes images
            y_realfake = tf.concat([tf.zeros_like(yhat_real), tf.ones_like(yhat_fake)], axis=0)

            # Add some noise to the TRUE outputs
            noise_real = 0.15 * tf.random.uniform(tf.shape(yhat_real))
            noise_fake = -0.15 * tf.random.uniform(tf.shape(yhat_fake))
            y_realfake += tf.concat([noise_real, noise_fake], axis=0)

            # Calculate loss - BINARYCROSS
            total_d_loss = self.d_loss(y_realfake, yhat_realfake)

        # Apply backpropagation - nn learn
        dgrad = d_tape.gradient(total_d_loss, self.discriminator.trainable_variables)
        self.d_opt.apply_gradients(zip(dgrad, self.discriminator.trainable_variables))

        # Train the generator
        with tf.GradientTape() as g_tape:
            # Generate some new images
            gen_images = self.generator(tf.random.normal((128, 128, 1)), training=True)

            # Create the predicted labels
            predicted_labels = self.discriminator(gen_images, training=False)

            # Calculate loss - trick to training to fake out the discriminator
            total_g_loss = self.g_loss(tf.zeros_like(predicted_labels), predicted_labels)

            # Apply backprop
        ggrad = g_tape.gradient(total_g_loss, self.generator.trainable_variables)
        self.g_opt.apply_gradients(zip(ggrad, self.generator.trainable_variables))

        return {"d_loss": total_d_loss, "g_loss": total_g_loss}


# Create instance of subclassed model
fashgan = FashionGAN(generator, discriminator)

# Compile the model
fashgan.compile(g_opt, d_opt, g_loss, d_loss)

import os
from keras.utils import array_to_img
from keras.callbacks import Callback


class ModelMonitor(Callback):
    def __init__(self, num_img=3, latent_dim=128):
        self.num_img = num_img
        self.latent_dim = latent_dim

    def on_epoch_end(self, epoch, logs=None):
        random_latent_vectors = tf.random.uniform((self.num_img, self.latent_dim, 1))
        generated_images = self.model.generator(random_latent_vectors)
        generated_images *= 255
        generated_images.numpy()
        for i in range(self.num_img):
            img = array_to_img(generated_images[i])
            img.save(os.path.join('images', f'generated_img_{epoch}_{i}.png'))


# Recommend 2000 epochs
hist = fashgan.fit(ds, epochs=2000, callbacks=[ModelMonitor()])

plt.suptitle('Loss')
plt.plot(hist.history['d_loss'], label='d_loss')
plt.plot(hist.history['g_loss'], label='g_loss')
plt.legend()
plt.show()

current_directory = os.getcwd()

model_path = os.path.join(current_directory, 'generatormodel.h5')

imgs = generator.predict(tf.random.normal((16, 128, 1)))

fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(10, 10))
for r in range(4):
    for c in range(4):
        ax[r][c].imshow(imgs[(r + 1) * (c + 1) - 1])

generator.save('generatorcifar10.h5')
discriminator.save('discriminatorcifar10.h5')
"""
"""
from numpy import zeros
from numpy import ones
from numpy.random import randn
from numpy.random import randint
from keras.datasets.cifar10 import load_data
from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Reshape
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import Conv2DTranspose
from keras.layers import LeakyReLU
from keras.layers import Dropout

from matplotlib import pyplot as plt

########################################################################

# Load data and plot to get a quick understanding
# CIFAR10 classes are: airplane, automobile, bird, cat, deer, dog, frog, horse,
# ship, truck

(trainX, trainy), (testX, testy) = load_data()

# plot 25 images
for i in range(25):
    plt.subplot(5, 5, 1 + i)
    plt.axis('off')
    plt.imshow(trainX[i])
plt.show()


#############################################################################
# Define generator, discriminator, gan and other helper functions
# Using Sequential method from Keras as it makes the definition of models easy.
# We will use functional way of defining the model for the conditional gan
# but sequential for descriminator and generator as they are straightforward.
#########################################################################

# define the standalone discriminator model
# Given an input image, the Discriminator outputs the likelihood of the image being real.
# Binary classification - true or false (1 or 0). So using sigmoid activation.
def define_discriminator(in_shape=(32, 32, 3)):
    model = Sequential()

    model.add(Conv2D(128, (3, 3), strides=(2, 2), padding='same', input_shape=in_shape))  # 16x16x128
    model.add(LeakyReLU(alpha=0.2))

    model.add(Conv2D(128, (3, 3), strides=(2, 2), padding='same'))  # 8x8x128
    model.add(LeakyReLU(alpha=0.2))

    model.add(Flatten())  # shape of 8192
    model.add(Dropout(0.4))
    model.add(Dense(1, activation='sigmoid'))  # shape of 1
    # compile model
    opt = Adam(lr=0.0002, beta_1=0.5)
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    return model


test_discr = define_discriminator()
print(test_discr.summary())


# define the standalone generator model
# #Given input of latent vector, the Generator produces an image.(here: 32x32)
# latent_dim, for example, can be 100, 1D array of size 100

# Here we are only using Dense and conv2dlayers. But network can be complicated based
# on the application. For example, you can use VGG for super res. GAN.

def define_generator(latent_dim):  # latent_dim is the dimension of the latent vector (e.g., 100)
    model = Sequential()
    # We will reshape input latent vector into 8x8 image as a starting point.
    # So n_nodes for the Dense layer can be 128x8x8 so when we reshape the output
    # it would be 8x8x128 and that can be slowly upscaled to 32x32 image for output.
    n_nodes = 128 * 8 * 8  # 8192 nodes
    model.add(Dense(n_nodes, input_dim=latent_dim))  # Dense layer so we can work with 1D latent vector
    model.add(LeakyReLU(alpha=0.2))
    model.add(Reshape((8, 8, 128)))  # 8x8x128 dataset from the latent vector.
    # upsample to 16x16
    model.add(Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same'))  # 16x16x128
    model.add(LeakyReLU(alpha=0.2))
    # upsample to 32x32
    model.add(Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same'))  # 32x32x128
    model.add(LeakyReLU(alpha=0.2))
    # generate
    model.add(Conv2D(3, (8, 8), activation='tanh', padding='same'))  # 32x32x3
    return model  # Model not compiled as it is not directly trained like the discriminator.
    # Generator is trained via GAN combined model.


test_gen = define_generator(100)
print(test_gen.summary())


# define the combined generator and discriminator model, for updating the generator
# Discriminator is trained separately so here only generator will be trained by keeping
# the discriminator constant.
def define_gan(generator, discriminator):
    discriminator.trainable = False  # Discriminator is trained separately. So set to not trainable.
    # connect generator and discriminator
    model = Sequential()
    model.add(generator)
    model.add(discriminator)
    # compile model
    opt = Adam(lr=0.0002, beta_1=0.5)
    model.compile(loss='binary_crossentropy', optimizer=opt)
    return model


# load cifar training images
def load_real_samples():
    (trainX, _), (_, _) = load_data()
    # cConvert to float and scale.
    X = trainX.astype('float32')
    # scale from [0,255] to [-1,1]
    X = (X - 127.5) / 127.5  # Generator uses tanh activation so rescale
    # original images to -1 to 1 to match the output of generator.
    return X


# pick a batch of random real samples to train the GAN
# In fact, we will train the GAN on a half batch of real images and another
# half batch of fake images.
# For each real image we assign a label 1 and for fake we assign label 0.
def generate_real_samples(dataset, n_samples):
    # choose random images
    ix = randint(0, dataset.shape[0], n_samples)
    # select the random images and assign it to X
    X = dataset[ix]
    # generate class labels and assign to y
    y = ones((n_samples, 1))  ##Label=1 indicating they are real
    return X, y


# generate n_samples number of latent vectors as input for the generator
def generate_latent_points(latent_dim, n_samples):
    # generate points in the latent space
    x_input = randn(latent_dim * n_samples)
    # reshape into a batch of inputs for the network
    x_input = x_input.reshape(n_samples, latent_dim)
    return x_input


# use the generator to generate n fake examples, with class labels
# Supply the generator, latent_dim and number of samples as input.
# Use the above latent point generator to generate latent points.
def generate_fake_samples(generator, latent_dim, n_samples):
    # generate points in latent space
    x_input = generate_latent_points(latent_dim, n_samples)
    # predict using generator to generate fake samples.
    X = generator.predict(x_input)
    # Class labels will be 0 as these samples are fake.
    y = zeros((n_samples, 1))  # Label=0 indicating they are fake
    return X, y


# train the generator and discriminator
# We loop through a number of epochs to train our Discriminator by first selecting
# a random batch of images from our true/real dataset.
# Then, generating a set of images using the generator.
# Feed both set of images into the Discriminator.
# Finally, set the loss parameters for both the real and fake images, as well as the combined loss.

def train(g_model, d_model, gan_model, dataset, latent_dim, n_epochs=100, n_batch=128):
    bat_per_epo = int(dataset.shape[0] / n_batch)
    half_batch = int(n_batch / 2)  # the discriminator model is updated for a half batch of real samples
    # and a half batch of fake samples, combined a single batch.
    # manually enumerate epochs and bacthes.
    for i in range(n_epochs):
        # enumerate batches over the training set
        for j in range(bat_per_epo):
            # Train the discriminator on real and fake images, separately (half batch each)
            # Research showed that separate training is more effective.
            # get randomly selected 'real' samples
            X_real, y_real = generate_real_samples(dataset, half_batch)
            # update discriminator model weights
            ##train_on_batch allows you to update weights based on a collection
            # of samples you provide
            # Let us just capture loss and ignore accuracy value (2nd output below)
            d_loss_real, _ = d_model.train_on_batch(X_real, y_real)

            # generate 'fake' examples
            X_fake, y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
            # update discriminator model weights
            d_loss_fake, _ = d_model.train_on_batch(X_fake, y_fake)

            # d_loss = 0.5 * np.add(d_loss_real, d_loss_fake) #Average loss if you want to report single..

            # prepare points in latent space as input for the generator
            X_gan = generate_latent_points(latent_dim, n_batch)

            # The generator wants the discriminator to label the generated samples
            # as valid (ones)
            # This is where the generator is trying to trick discriminator into believing
            # the generated image is true (hence value of 1 for y)
            y_gan = ones((n_batch, 1))

            # Generator is part of combined model where it got directly linked with the discriminator
            # Train the generator with latent_dim as x and 1 as y.
            # Again, 1 as the output as it is adversarial and if generator did a great
            # job of folling the discriminator then the output would be 1 (true)
            # update the generator via the discriminator's error
            g_loss = gan_model.train_on_batch(X_gan, y_gan)

            # Print losses on this batch
            print('Epoch>%d, Batch %d/%d, d1=%.3f, d2=%.3f g=%.3f' %
                  (i + 1, j + 1, bat_per_epo, d_loss_real, d_loss_fake, g_loss))
    # save the generator model
    g_model.save('cifar_generator_250epochs.h5')


###################################################################
# Train the GAN

# size of the latent space
latent_dim = 100
# create the discriminator
discriminator = define_discriminator()
# create the generator
generator = define_generator(latent_dim)
# create the gan
gan_model = define_gan(generator, discriminator)
# load image data
dataset = load_real_samples()
# train model
train(generator, discriminator, gan_model, dataset, latent_dim, n_epochs=250)

################################################################################

# Now, let us load the generator model and generate images

from keras.models import load_model
from numpy.random import randn


# Plot generated images
def show_plot(examples, n):
    for i in range(n * n):
        plt.subplot(n, n, 1 + i)
        plt.axis('off')
        plt.imshow(examples[i, :, :, :])
    plt.show()


# load model
model = load_model('cifar_generator_250epochs.h5')  # Model trained for 100 epochs
# generate images
latent_points = generate_latent_points(100, 25)  # Latent dim and n_samples
# generate images
X = model.predict(latent_points)
# scale from [-1,1] to [0,1]
X = (X + 1) / 2.0

import numpy as np

X = (X * 255).astype(np.uint8)

# plot the result
show_plot(X, 5)

# Note: CIFAR10 classes are: airplane, automobile, bird, cat, deer, dog, frog, horse,
# ship, truck
"""


from numpy import zeros
from numpy import ones
from numpy.random import randn
from numpy.random import randint
from keras.datasets.cifar10 import load_data
from keras.optimizers import Adam
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers import Reshape
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import Conv2DTranspose
from keras.layers import LeakyReLU
from keras.layers import Dropout
from keras.layers import Embedding
from keras.layers import Concatenate

from matplotlib import pyplot as plt

########################################################################

# Load data and plot to get a quick understanding
# CIFAR10 classes are: airplane, automobile, bird, cat, deer, dog, frog, horse,
# ship, truck

(trainX, trainy), (testX, testy) = load_data()

# plot 25 images
for i in range(25):
    plt.subplot(5, 5, 1 + i)
    plt.axis('off')
    plt.imshow(trainX[i])
plt.show()


#############################################################################
# Define generator, discriminator, gan and other helper functions
# We will use functional way of defining model as we have multiple inputs;
# both images and corresponding labels.
########################################################################

# define the standalone discriminator model
# Given an input image, the Discriminator outputs the likelihood of the image being real.
# Binary classification - true or false (1 or 0). So using sigmoid activation.

# Unlike regular GAN here we are also providing number of classes as input.
# Input to the model will be both images and labels.
def define_discriminator(in_shape=(32, 32, 3), n_classes=10):
    # label input
    in_label = Input(shape=(1,))  # Shape 1
    # embedding for categorical input
    # each label (total 10 classes for cifar), will be represented by a vector of size 50.
    # This vector of size 50 will be learnt by the discriminator
    li = Embedding(n_classes, 50)(in_label)  # Shape 1,50
    # scale up to image dimensions with linear activation
    n_nodes = in_shape[0] * in_shape[1]  # 32x32 = 1024.
    li = Dense(n_nodes)(li)  # Shape = 1, 1024
    # reshape to additional channel
    li = Reshape((in_shape[0], in_shape[1], 1))(li)  # 32x32x1

    # image input
    in_image = Input(shape=in_shape)  # 32x32x3
    # concat label as a channel
    merge = Concatenate()([in_image, li])  # 32x32x4 (4 channels, 3 for image and the other for labels)

    # downsample: This part is same as unconditional GAN upto the output layer.
    # We will combine input label with input image and supply as inputs to the model.
    fe = Conv2D(128, (3, 3), strides=(2, 2), padding='same')(merge)  # 16x16x128
    fe = LeakyReLU(alpha=0.2)(fe)
    # downsample
    fe = Conv2D(128, (3, 3), strides=(2, 2), padding='same')(fe)  # 8x8x128
    fe = LeakyReLU(alpha=0.2)(fe)
    # flatten feature maps
    fe = Flatten()(fe)  # 8192  (8*8*128=8192)
    # dropout
    fe = Dropout(0.4)(fe)
    # output
    out_layer = Dense(1, activation='sigmoid')(fe)  # Shape=1

    # define model
    ##Combine input label with input image and supply as inputs to the model.
    model = Model([in_image, in_label], out_layer)
    # compile model
    opt = Adam(lr=0.0002, beta_1=0.5)
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    return model


test_discr = define_discriminator()
print(test_discr.summary())


# define the standalone generator model
# latent vector and label as inputs

def define_generator(latent_dim, n_classes=10):
    # label input
    in_label = Input(shape=(1,))  # Input of dimension 1
    # embedding for categorical input
    # each label (total 10 classes for cifar), will be represented by a vector of size 50.
    li = Embedding(n_classes, 50)(in_label)  # Shape 1,50

    # linear multiplication
    n_nodes = 8 * 8  # To match the dimensions for concatenation later in this step.
    li = Dense(n_nodes)(li)  # 1,64
    # reshape to additional channel
    li = Reshape((8, 8, 1))(li)

    # image generator input
    in_lat = Input(shape=(latent_dim,))  # Input of dimension 100

    # foundation for 8x8 image
    # We will reshape input latent vector into 8x8 image as a starting point.
    # So n_nodes for the Dense layer can be 128x8x8 so when we reshape the output
    # it would be 8x8x128 and that can be slowly upscaled to 32x32 image for output.
    # Note that this part is same as unconditional GAN until the output layer.
    # While defining model inputs we will combine input label and the latent input.
    n_nodes = 128 * 8 * 8
    gen = Dense(n_nodes)(in_lat)  # shape=8192
    gen = LeakyReLU(alpha=0.2)(gen)
    gen = Reshape((8, 8, 128))(gen)  # Shape=8x8x128
    # merge image gen and label input
    merge = Concatenate()([gen, li])  # Shape=8x8x129 (Extra channel corresponds to the label)
    # upsample to 16x16
    gen = Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same')(merge)  # 16x16x128
    gen = LeakyReLU(alpha=0.2)(gen)
    # upsample to 32x32
    gen = Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same')(gen)  # 32x32x128
    gen = LeakyReLU(alpha=0.2)(gen)
    # output
    out_layer = Conv2D(3, (8, 8), activation='tanh', padding='same')(gen)  # 32x32x3
    # define model
    model = Model([in_lat, in_label], out_layer)
    return model  # Model not compiled as it is not directly trained like the discriminator.


test_gen = define_generator(100, n_classes=10)
print(test_gen.summary())


# #Generator is trained via GAN combined model.
# define the combined generator and discriminator model, for updating the generator
# Discriminator is trained separately so here only generator will be trained by keeping
# the discriminator constant.
def define_gan(g_model, d_model):
    d_model.trainable = False  # Discriminator is trained separately. So set to not trainable.

    ## connect generator and discriminator...
    # first, get noise and label inputs from generator model
    gen_noise, gen_label = g_model.input  # Latent vector size and label size
    # get image output from the generator model
    gen_output = g_model.output  # 32x32x3

    # generator image output and corresponding input label are inputs to discriminator
    gan_output = d_model([gen_output, gen_label])
    # define gan model as taking noise and label and outputting a classification
    model = Model([gen_noise, gen_label], gan_output)
    # compile model
    opt = Adam(lr=0.0002, beta_1=0.5)
    model.compile(loss='binary_crossentropy', optimizer=opt)
    return model


# load cifar images
def load_real_samples():
    # load dataset
    (trainX, trainy), (_, _) = load_data()  # cifar
    # convert to floats and scale
    X = trainX.astype('float32')
    # scale from [0,255] to [-1,1]
    X = (X - 127.5) / 127.5  # Generator uses tanh activation so rescale
    # original images to -1 to 1 to match the output of generator.
    return [X, trainy]


# # select real samples
# pick a batch of random real samples to train the GAN
# In fact, we will train the GAN on a half batch of real images and another
# half batch of fake images.
# For each real image we assign a label 1 and for fake we assign label 0.
def generate_real_samples(dataset, n_samples):
    # split into images and labels
    images, labels = dataset
    # choose random instances
    ix = randint(0, images.shape[0], n_samples)
    # select images and labels
    X, labels = images[ix], labels[ix]
    # generate class labels and assign to y (don't confuse this with the above labels that correspond to cifar labels)
    y = ones((n_samples, 1))  # Label=1 indicating they are real
    return [X, labels], y


# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples, n_classes=10):
    # generate points in the latent space
    x_input = randn(latent_dim * n_samples)
    # reshape into a batch of inputs for the network
    z_input = x_input.reshape(n_samples, latent_dim)
    # generate labels
    labels = randint(0, n_classes, n_samples)
    return [z_input, labels]


# use the generator to generate n fake examples, with class labels
# Supply the generator, latent_dim and number of samples as input.
# Use the above latent point generator to generate latent points.
def generate_fake_samples(generator, latent_dim, n_samples):
    # generate points in latent space
    z_input, labels_input = generate_latent_points(latent_dim, n_samples)
    # predict outputs
    images = generator.predict([z_input, labels_input])
    # create class labels
    y = zeros((n_samples, 1))  # Label=0 indicating they are fake
    return [images, labels_input], y


# train the generator and discriminator
# We loop through a number of epochs to train our Discriminator by first selecting
# a random batch of images from our true/real dataset.
# Then, generating a set of images using the generator.
# Feed both set of images into the Discriminator.
# Finally, set the loss parameters for both the real and fake images, as well as the combined loss.
def train(g_model, d_model, gan_model, dataset, latent_dim, n_epochs=100, n_batch=128):
    bat_per_epo = int(dataset[0].shape[0] / n_batch)
    half_batch = int(n_batch / 2)  # the discriminator model is updated for a half batch of real samples
    # and a half batch of fake samples, combined a single batch.
    # manually enumerate epochs
    for i in range(n_epochs):
        # enumerate batches over the training set
        for j in range(bat_per_epo):
            # Train the discriminator on real and fake images, separately (half batch each)
            # Research showed that separate training is more effective.
            # get randomly selected 'real' samples
            # get randomly selected 'real' samples
            [X_real, labels_real], y_real = generate_real_samples(dataset, half_batch)

            # update discriminator model weights
            ##train_on_batch allows you to update weights based on a collection
            # of samples you provide
            d_loss_real, _ = d_model.train_on_batch([X_real, labels_real], y_real)

            # generate 'fake' examples
            [X_fake, labels], y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
            # update discriminator model weights
            d_loss_fake, _ = d_model.train_on_batch([X_fake, labels], y_fake)

            # d_loss = 0.5 * np.add(d_loss_real, d_loss_fake) #Average loss if you want to report single..

            # prepare points in latent space as input for the generator
            [z_input, labels_input] = generate_latent_points(latent_dim, n_batch)

            # The generator wants the discriminator to label the generated samples
            # as valid (ones)
            # This is where the generator is trying to trick discriminator into believing
            # the generated image is true (hence value of 1 for y)
            # create inverted labels for the fake samples
            y_gan = ones((n_batch, 1))
            # Generator is part of combined model where it got directly linked with the discriminator
            # Train the generator with latent_dim as x and 1 as y.
            # Again, 1 as the output as it is adversarial and if generator did a great
            # job of folling the discriminator then the output would be 1 (true)
            # update the generator via the discriminator's error
            g_loss = gan_model.train_on_batch([z_input, labels_input], y_gan)
            # Print losses on this batch
            print('Epoch>%d, Batch%d/%d, d1=%.3f, d2=%.3f g=%.3f' %
                  (i + 1, j + 1, bat_per_epo, d_loss_real, d_loss_fake, g_loss))
        # save the generator model
        g_model.save(f'cifar_conditional_generator_{i}epochs.h5')


# Train the GAN

# size of the latent space
latent_dim = 100
# create the discriminator
d_model = define_discriminator()
# create the generator
g_model = define_generator(latent_dim)
# create the gan
gan_model = define_gan(g_model, d_model)
# load image data
dataset = load_real_samples()
# train model
train(g_model, d_model, gan_model, dataset, latent_dim, n_epochs=250)

##########################################################
# Now, let us load the generator model and generate images
# Lod the trained model and generate a few images
from numpy import asarray
from numpy.random import randn
from numpy.random import randint
from keras.models import load_model
import numpy as np

#

# Note: CIFAR10 classes are: airplane, automobile, bird, cat, deer, dog, frog, horse,
# ship, truck

# load model
model = load_model('cifar_conditional_generator_250epochs.h5')

# generate multiple images

latent_points, labels = generate_latent_points(100, 100)
# specify labels - generate 10 sets of labels each gping from 0 to 9
labels = asarray([x for _ in range(10) for x in range(10)])
# generate images
X = model.predict([latent_points, labels])
# scale from [-1,1] to [0,1]
X = (X + 1) / 2.0
X = (X * 255).astype(np.uint8)


# plot the result (10 sets of images, all images in a column should be of same class in the plot)
# Plot generated images
def show_plot(examples, n):
    for i in range(n * n):
        plt.subplot(n, n, 1 + i)
        plt.axis('off')
        plt.imshow(examples[i, :, :, :])
    plt.show()


show_plot(X, 10)