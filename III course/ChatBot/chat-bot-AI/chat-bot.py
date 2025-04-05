import random

import telebot
import numpy as np
import torch
from googletrans import Translator
import matplotlib.pyplot as plt
from keras.models import load_model
import os

from numpy import asarray
from numpy.random import randn, randint
from telebot import types
from telebot.types import InputFile
from torch import nn

from bot import corpus_name, voc, EncoderRNN, LuongAttnDecoderRNN, device, GreedySearchDecoder, normalizeString, \
    evaluate

# Инициализация переменной состояния
user_state = {}

# Загрузка генератора
generator = load_model('generator.h5')
generator_cifar10 = load_model('cifar_conditional_generator_234epochs.h5')


def generate_latent_points(latent_dim, n_samples, n_classes=10):
    # generate points in the latent space
    x_input = randn(latent_dim * n_samples)
    # reshape into a batch of inputs for the network
    z_input = x_input.reshape(n_samples, latent_dim)
    # generate labels
    labels = randint(0, n_classes, n_samples)
    return [z_input, labels]


def generate_image_cifar10():
    # generate a single latent point
    latent_point = generate_latent_points(1, 100)[0]

    num = random.randint(0, 9)

    # specify label
    label = asarray([num])  # for example, generate an image with label 5

    # generate image
    X = generator_cifar10.predict([latent_point.reshape(1, 100), label])

    # scale from [-1,1] to [0,1]
    X = (X + 1) / 2.0
    X = (X * 255).astype(np.uint8)

    # plot the result
    plt.imshow(X[0])
    plt.axis('off')
    plt.show()

    os.makedirs('chat_generated_images', exist_ok=True)

    image_name = f'image_{np.random.randint(10000)}.png'
    image_path = os.path.join('chat_generated_images', image_name)

    plt.imsave(image_path, X.squeeze())
    # show_generated_image(image_path)

    return image_path


def generate_image():
    noise = np.random.randn(1, 128, 1)
    generated_image = generator.predict(noise)

    os.makedirs('chat_generated_images', exist_ok=True)

    image_name = f'image_{np.random.randint(10000)}.png'
    image_path = os.path.join('chat_generated_images', image_name)

    plt.imsave(image_path, generated_image.squeeze(), cmap='gray')
    show_generated_image(image_path)

    return image_path


'''
def is_valid_item(item_name):
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
                   'Ankle boot']
    return item_name in class_names
'''


def translate_to_english(text):
    try:
        translator = Translator()
        translated_text = translator.translate(text, src='ru', dest='en')
        return translated_text.text
    except Exception as e:
        print(f"An error occurred while translating: {e}")
        return text  # Возвращаем исходный текст в случае ошибки


def translate_to_russian(text):
    try:
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest='ru')
        return translated_text.text
    except Exception as e:
        print(f"An error occurred while translating: {e}")
        return text  # Возвращаем исходный текст в случае ошибки


def show_generated_image(image_path):
    generated_image = plt.imread(image_path)
    plt.imshow(generated_image, cmap='gray')
    plt.axis('off')
    plt.show()


bot = telebot.TeleBot('7060568100:AAFNkBPI-xyIQ3aUWrdJKICD5NcYSJ8ckGA')

from transformers import BarkModel, AutoProcessor
import torch
import scipy


def text_to_audio(text, bark_model='suno/bark', voice_preset='v2/ru_speaker_3'):
    model = BarkModel.from_pretrained(bark_model)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = model.to(device)
    processor = AutoProcessor.from_pretrained(bark_model)
    inputs = processor(text, voice_preset=voice_preset).to(device)
    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()
    sample_rate = model.generation_config.sample_rate
    # Генерация пути к аудиофайлу
    audio_file_path = f'{voice_preset.split("/")[1]}.mp3'
    # Проверка существования файла и его удаление
    if os.path.exists(audio_file_path):
        os.remove(audio_file_path)
    # Сохранение аудиофайла
    scipy.io.wavfile.write(audio_file_path, rate=sample_rate, data=audio_array)
    return audio_file_path


# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Привет, {message.from_user.first_name}'
#     bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    item_button = types.KeyboardButton('Generate Clothes')
    item_button.background_color = "#FF5733"  # Задаем цвет фона кнопки (в формате HEX)
    markup.add(item_button)

    item_button = types.KeyboardButton('Generate Image')
    item_button.background_color = "#FF5733"
    markup.add(item_button)

    item_button = types.KeyboardButton('Voice')
    item_button.background_color = "#FF5733"
    markup.add(item_button)

    mess = f'Hi, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Generate Clothes')
def generate_and_send_image(message):
    generated_image_path = generate_image()
    bot.send_photo(message.chat.id, open(generated_image_path, 'rb'))


@bot.message_handler(func=lambda message: message.text == 'Generate Image')
def generate_and_send_image(message):
    generated_image_path = generate_image_cifar10()
    bot.send_photo(message.chat.id, open(generated_image_path, 'rb'))


# Обработчик для кнопки "Voice"
@bot.message_handler(func=lambda message: message.text == 'Voice')
def request_voice_handler(message):
    # Устанавливаем состояние пользователя в 'waiting_for_text'
    user_state[message.chat.id] = 'waiting_for_text'
    # Отправить сообщение с запросом на ввод текста
    bot.send_message(message.chat.id, "Введите текст для синтеза речи:")


# from bot import MAX_LENGTH

MAX_LENGTH = 40

# Configure models
model_name = 'cb_model'
attn_model = 'dot'
# attn_model = 'general'
# attn_model = 'concat'
hidden_size = 500
encoder_n_layers = 2
decoder_n_layers = 2
dropout = 0.1
batch_size = 32
save_dir = os.path.join("data", "save")

# NOTE : Set checkpoint to load from; set to None if starting from scratch
# loadFilename = None
checkpoint_iter = 8000
loadFilename = os.path.join(save_dir, model_name, corpus_name,
                            '{}-{}_{}'.format(encoder_n_layers, decoder_n_layers, hidden_size),
                            '{}_checkpoint.tar'.format(checkpoint_iter))

# Load model if a loadFilename is provided
if loadFilename:
    # If loading on same machine the model was trained on
    # checkpoint = torch.load(loadFilename)
    # If loading a model trained on GPU to CPU
    checkpoint = torch.load(loadFilename, map_location=torch.device('cpu'))
    encoder_sd = checkpoint['en']
    decoder_sd = checkpoint['de']
    encoder_optimizer_sd = checkpoint['en_opt']
    decoder_optimizer_sd = checkpoint['de_opt']
    embedding_sd = checkpoint['embedding']
    voc.__dict__ = checkpoint['voc_dict']

print('Building encoder and decoder ...')
# Initialize word embeddings
embedding = nn.Embedding(voc.num_words, hidden_size)
if loadFilename:
    embedding.load_state_dict(embedding_sd)
# Initialize encoder & decoder models
encoder = EncoderRNN(hidden_size, embedding, encoder_n_layers, dropout)
decoder = LuongAttnDecoderRNN(attn_model, embedding, hidden_size, voc.num_words, decoder_n_layers, dropout)
if loadFilename:
    encoder.load_state_dict(encoder_sd)
    decoder.load_state_dict(decoder_sd)
# Use appropriate device
encoder = encoder.to(device)
decoder = decoder.to(device)
print('Models built and ready to go!')

# Set dropout layers to eval mode
encoder.eval()
decoder.eval()

# Initialize search module
searcher = GreedySearchDecoder(encoder, decoder)


def get_response(text):
    try:
        # Get input sentence
        input_sentence = text
        # Check if it is quit case

        # Normalize sentence
        input_sentence = normalizeString(input_sentence)
        # Evaluate sentence
        output_words = evaluate(encoder, decoder, searcher, voc, input_sentence)
        # Format and print response sentence
        output_words[:] = [x for x in output_words if not (x == 'EOS' or x == 'PAD')]
        return ' '.join(output_words)

    except KeyError:
        return None


# Обработчик для ввода текста
@bot.message_handler(func=lambda message: True, content_types=['text'])
def text_input_handler(message):
    if message.chat.id in user_state and user_state[message.chat.id] == 'waiting_for_text':
        if message.text:
            # Вызываем функцию text_to_audio с введенным текстом
            audio_file_path = text_to_audio(message.text)
            # Открываем аудиофайл и получаем его длительность
            audio = open(audio_file_path, 'rb')
            duration = 10  # Замените это на реальную длительность вашего аудиофайла
            # Создаем объект types.InputFile для отправки аудиофайла с дополнительной информацией
            audio_with_metadata = InputFile(audio)
            # Отправляем аудиофайл пользователю
            bot.send_audio(message.chat.id, audio_with_metadata)
            # Удаляем аудиофайл после отправки
            #os.remove(audio_file_path)
            # Устанавливаем состояние пользователя обратно в 'idle'
            user_state[message.chat.id] = 'idle'
            return  # Завершаем обработку сообщения после отправки аудио
    else:
        # Если не в режиме ожидания текста для генерации речи, обрабатываем текст как обычно
        if message.text.isascii():
            item_name = message.text
            answer = get_response(item_name)
            if answer:
                bot.send_message(message.chat.id, answer)
            else:
                bot.send_message(message.chat.id, translate_to_english("Извините, я вас не понимаю"))
        else:
            item_name = translate_to_english(message.text)
            answer = translate_to_russian(get_response(item_name))
            if answer:
                bot.send_message(message.chat.id, answer)
            else:
                bot.send_message(message.chat.id, "Извините, я вас не понимаю")


bot.polling(none_stop=True)
