import re
import sys
from collections import Counter
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QComboBox, QMainWindow, QFileDialog, QTextEdit, QFormLayout, QMessageBox, QScrollArea
)
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import os
import string
import random



ALPHABETS = {
    "Русский": "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я".split(),
    "Английский": "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
}


class Operations:
    @staticmethod
    def to_binary(text, alphabet):
        bit_length = 6 if len(alphabet) > 32 else 5
        # Преобразуем каждый символ текста в его индекс в алфавите и затем в двоичное представление
        binary_text = ''.join(format(alphabet.index(char), f'0{bit_length}b') for char in text)
        return binary_text
    
    @staticmethod
    def generate_gamma(length):
        half_length = length // 2
        gamma = ['0'] * half_length + ['1'] * half_length
        if length % 2 != 0:
            gamma.append(random.choice(['0', '1']))
        random.shuffle(gamma)
        return ''.join(gamma)


class CryptoResistantApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Криптостойкие шифры")
        self.setGeometry(200, 200, 800, 800)

        # Создание вкладок
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Выбор алфавита на уровне всего приложения
        self.alphabet_choice = QComboBox()
        self.alphabet_choice.addItems(["Русский", "Английский"])
        self.alphabet_choice.currentIndexChanged.connect(self.update_validators)

        # Основной макет для выбора алфавита
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Выберите алфавит:"))
        main_layout.addWidget(self.alphabet_choice)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setMenuWidget(main_widget)

        # Вкладки для работы с текстом и файлами
        self.text_tab = TextTab(self.alphabet_choice)
        self.gamma_tab = GammaTab(self.alphabet_choice)
        self.chain_tab = ChainTab(self.alphabet_choice)
        self.tabs.addTab(self.text_tab, "Шифр/Расшифр текста")
        self.tabs.addTab(self.gamma_tab, "Гаммирование")
        self.tabs.addTab(self.chain_tab, "Цепление блоков")

    def update_validators(self):
        # Обновляем валидаторы во всех табах
        self.text_tab.update_validator()
        self.gamma_tab.update_validator()
        self.chain_tab.update_validator()


class TextTab(QWidget, Operations):
    def __init__(self, alphabet_choice):
        super().__init__()

        # Сохраняем ссылку на выбор алфавита
        self.alphabet_choice = alphabet_choice

        # Основной макет
        layout = QFormLayout()

        # Поле ввода для исходного сообщения
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Введите исходное сообщение")
        self.input_text.textChanged.connect(self.update_binary_text)
        layout.addRow(QLabel("Исходное сообщение:"), self.input_text)

        # Поле для двоичного представления исходного сообщения
        self.binary_input_text = QTextEdit()
        self.binary_input_text.setReadOnly(True)
        self.binary_input_text.setFixedHeight(50)
        layout.addRow(QLabel("Двоичное представление:"), self.binary_input_text)

        # Поле для ввода ключа
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Введите ключ")
        self.key_input.textChanged.connect(self.update_binary_key)
        layout.addRow(QLabel("Ключ:"), self.key_input)

        # Поле для двоичного представления ключа
        self.binary_key_input = QTextEdit()
        self.binary_key_input.setReadOnly(True)
        self.binary_key_input.setFixedHeight(50)
        layout.addRow(QLabel("Двоичное представление ключа:"), self.binary_key_input)

        # Кнопка для шифрования
        self.encrypt_button = QPushButton("XOR")
        self.encrypt_button.clicked.connect(self.xor_text)
        layout.addRow(self.encrypt_button)

        # Поле для вывода результата
        self.output_text = QLabel("Результат:")
        layout.addRow(self.output_text)

        # Кнопка для дешифрования
        self.decrypt_button = QPushButton("Расшифровать")
        self.decrypt_button.clicked.connect(self.decrypt_text)
        layout.addRow(self.decrypt_button)

        # Поле для вывода расшифрованного сообщения
        self.decrypted_text = QLabel("Расшифрованное сообщение:")
        layout.addRow(self.decrypted_text)

        # Поле для вывода расшифрованного сообщения в двоичном виде
        self.binary_decrypted_text = QTextEdit()
        self.binary_decrypted_text.setReadOnly(True)
        self.binary_decrypted_text.setFixedHeight(50)
        layout.addRow(QLabel("Двоичное представление расшифрованного сообщения:"), self.binary_decrypted_text)

        self.setLayout(layout)
        self.encrypted_text = ""  # Поле для хранения зашифрованного текста

        # Устанавливаем начальный валидатор
        self.update_validator()

        # Подключаем обновление валидатора при изменении выбора алфавита
        self.alphabet_choice.currentIndexChanged.connect(self.update_validator)

    def update_validator(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]

        regex = QRegExp(f"[{''.join(alphabet)}]*")

        validator = QRegExpValidator(regex)

        self.input_text.setValidator(validator)
        self.input_text.clear()

        # Обновляем валидатор для поля ввода ключа
        self.setup_key_validator()

        # Обнуляем все значения
        self.binary_input_text.clear()
        self.key_input.clear()
        self.binary_key_input.clear()
        self.output_text.setText("Результат:")
        self.decrypted_text.setText("Расшифрованное сообщение:")
        self.binary_decrypted_text.clear()
        self.encrypted_text = ""

    def setup_key_validator(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        regex = QRegExp(f"[{''.join(alphabet)}]*")
        validator = QRegExpValidator(regex)
        self.key_input.setValidator(validator)
        self.key_input.clear()

    def update_binary_text(self):
        text = self.input_text.text()
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        self.binary_input_text.setText(self.to_binary(text, alphabet))
        self.encrypted_text = ""  # Очищаем зашифрованное сообщение при изменении исходного текста
        self.output_text.setText("Результат:")
        self.decrypted_text.setText("Расшифрованное сообщение:")
        self.binary_decrypted_text.clear()

    def update_binary_key(self):
        key = self.key_input.text()
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        self.binary_key_input.setText(self.to_binary(key, alphabet))

    def xor_text(self):
        try:
            text = self.input_text.text()
            key = self.key_input.text()
            if not text or not key:
                self.output_text.setText("Ошибка: введите текст и ключ.")
                self.encrypted_text = ""
                self.decrypted_text.setText("Расшифрованное сообщение:")
                self.binary_decrypted_text.clear()
                return

            binary_text = self.binary_input_text.toPlainText()
            # binary_key = self.binary_key_input.toPlainText()

            # Повторяем ключ до длины текста
            # len(text) // len(key): Вычисляет, сколько раз ключ полностью помещается в текст.
            # key * (len(text) // len(key)): Повторяет ключ столько раз, сколько раз он полностью помещается в текст.
            # len(text) % len(key): Вычисляет оставшуюся длину, которая не покрывается полными повторениями ключа.
            # key[:len(text) % len(key)]: Берет часть ключа, необходимую для заполнения оставшейся длины.

            # Вычисление количества полных повторений ключа:
            # len(text) = 5
            # len(key) = 3
            # len(text) // len(key) = 5 // 3 = 1
            # key * (len(text) // len(key)) = "KEY" * 1 = "KEY"
            # Вычисление оставшейся длины:

            # len(text) % len(key) = 5 % 3 = 2
            # key[:len(text) % len(key)] = "KEY"[:2] = "KE"
            # Объединение полных повторений и оставшейся части:

            # repeated_key = "KEY" + "KE" = "KEYKE"
            repeated_key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
            binary_repeated_key = self.to_binary(repeated_key, ALPHABETS[self.alphabet_choice.currentText()])

            encrypted_binary = ''.join('1' if binary_text[i] != binary_repeated_key[i] else '0' for i in range(len(binary_text)))
            self.encrypted_text = encrypted_binary
            self.output_text.setText(f"Зашифрованное сообщение: {encrypted_binary}")
        except ValueError as e:
            self.output_text.setText(str(e))
            self.encrypted_text = ""
            self.decrypted_text.setText("Расшифрованное сообщение:")
            self.binary_decrypted_text.clear()

    def decrypt_text(self):
        try:
            if not self.encrypted_text:
                self.decrypted_text.setText("Ошибка: нет текста для расшифровки.")
                self.binary_decrypted_text.clear()
                return

            binary_text = self.encrypted_text
            key = self.key_input.text()
            repeated_key = (key * (len(binary_text) // len(key))) + key[:len(binary_text) % len(key)]
            binary_repeated_key = self.to_binary(repeated_key, ALPHABETS[self.alphabet_choice.currentText()])

            decrypted_binary = ''.join('1' if binary_text[i] != binary_repeated_key[i] else '0' for i in range(len(binary_text)))
            
            bit_length = 6 if len(ALPHABETS[self.alphabet_choice.currentText()]) > 32 else 5

            # range(0, len(decrypted_binary), bit_length): Создает последовательность индексов с шагом bit_length.
            # decrypted_binary[i:i+bit_length]: Извлекает подстроку длиной bit_length из decrypted_binary, начиная с индекса i.
            # int(decrypted_binary[i:i+bit_length], 2): Преобразует подстроку из двоичного представления в десятичное число.
            # ALPHABETS[self.alphabet_choice.currentText()][...]: Использует десятичное число как индекс для поиска соответствующего символа в алфавите.
            decrypted_text = ''.join(ALPHABETS[self.alphabet_choice.currentText()][int(decrypted_binary[i:i+bit_length], 2)] for i in range(0, len(decrypted_binary), bit_length))
            
            self.decrypted_text.setText(f"Расшифрованное сообщение: {decrypted_text}")
            self.binary_decrypted_text.setText(f"{decrypted_binary}")
        except ValueError as e:
            self.decrypted_text.setText(str(e))
            self.encrypted_text = ""
            self.binary_decrypted_text.clear()

class GammaTab(QWidget, Operations):
    def __init__(self, alphabet_choice):
        super().__init__()

        # Сохраняем ссылку на выбор алфавита
        self.alphabet_choice = alphabet_choice

        # Основной макет
        layout = QFormLayout()

        # Поле ввода для исходного сообщения
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Введите исходное сообщение")
        self.input_text.textChanged.connect(self.update_binary_text)
        layout.addRow(QLabel("Исходное сообщение:"), self.input_text)

        # Поле для двоичного представления исходного сообщения
        self.binary_input_text = QTextEdit()
        self.binary_input_text.setReadOnly(True)
        self.binary_input_text.setFixedHeight(50)
        layout.addRow(QLabel("Двоичное представление:"), self.binary_input_text)

        # Кнопка для генерации гаммы
        self.generate_button = QPushButton("Сгенерировать")
        self.generate_button.clicked.connect(self.generate_gamma_text)
        layout.addRow(self.generate_button)

        # Поле для отображения гаммы
        self.gamma_text = QTextEdit()
        self.gamma_text.setReadOnly(True)
        self.gamma_text.setFixedHeight(50)
        layout.addRow(QLabel("Гамма:"), self.gamma_text)

        # Кнопка для шифрования
        self.encrypt_button = QPushButton("XOR")
        self.encrypt_button.clicked.connect(self.xor_text)
        layout.addRow(self.encrypt_button)

        # Поле для вывода результата
        self.output_text = QLabel("Результат:")
        layout.addRow(self.output_text)

        # Кнопка для дешифрования
        self.decrypt_button = QPushButton("Расшифровать")
        self.decrypt_button.clicked.connect(self.decrypt_text)
        layout.addRow(self.decrypt_button)

        # Поле для вывода расшифрованного сообщения
        self.decrypted_text = QLabel("Расшифрованное сообщение:")
        layout.addRow(self.decrypted_text)

        # Поле для вывода расшифрованного сообщения в двоичном виде
        self.binary_decrypted_text = QTextEdit()
        self.binary_decrypted_text.setReadOnly(True)
        self.binary_decrypted_text.setFixedHeight(50)
        layout.addRow(QLabel("Двоичное представление расшифрованного сообщения:"), self.binary_decrypted_text)

        self.setLayout(layout)
        self.encrypted_text = ""  # Поле для хранения зашифрованного текста

        # Устанавливаем начальный валидатор
        self.update_validator()

        # Подключаем обновление валидатора при изменении выбора алфавита
        self.alphabet_choice.currentIndexChanged.connect(self.update_validator)

    def update_validator(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]

        regex = QRegExp(f"[{''.join(alphabet)}]*")

        validator = QRegExpValidator(regex)

        self.input_text.setValidator(validator)
        self.input_text.clear()

        # Обнуляем все значения
        self.binary_input_text.clear()
        self.gamma_text.clear()
        self.output_text.setText("Результат:")
        self.decrypted_text.setText("Расшифрованное сообщение:")
        self.binary_decrypted_text.clear()
        self.encrypted_text = ""

    def update_binary_text(self):
        text = self.input_text.text()
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        self.binary_input_text.setText(self.to_binary(text, alphabet))
        self.gamma_text.clear()
        self.encrypted_text = ""  # Очищаем зашифрованное сообщение при изменении исходного текста
        self.output_text.setText("Результат:")
        self.decrypted_text.setText("Расшифрованное сообщение:")
        self.binary_decrypted_text.clear()

    def generate_gamma_text(self):
        binary_text = self.binary_input_text.toPlainText()
        if not binary_text:
            self.gamma_text.setText("Ошибка: введите текст для генерации гаммы.")
            return

        gamma = self.generate_gamma(len(binary_text))
        self.gamma_text.setText(gamma)

    def xor_text(self):
        try:
            binary_text = self.binary_input_text.toPlainText()
            gamma = self.gamma_text.toPlainText()
            if not binary_text or not gamma:
                self.output_text.setText("Ошибка: введите текст и сгенерируйте гамму.")
                self.encrypted_text = ""
                self.decrypted_text.setText("Расшифрованное сообщение:")
                self.binary_decrypted_text.clear()
                return

            encrypted_binary = ''.join('1' if binary_text[i] != gamma[i] else '0' for i in range(len(binary_text)))
            self.encrypted_text = encrypted_binary
            self.output_text.setText(f"Зашифрованное сообщение: {encrypted_binary}")
        except ValueError as e:
            self.output_text.setText(str(e))
            self.encrypted_text = ""
            self.decrypted_text.setText("Расшифрованное сообщение:")
            self.binary_decrypted_text.clear()

    def decrypt_text(self):
        try:
            if not self.encrypted_text:
                self.decrypted_text.setText("Ошибка: нет текста для расшифровки.")
                self.binary_decrypted_text.clear()
                self.gamma_text.clear()
                return

            if not self.gamma_text.toPlainText():
                self.decrypted_text.setText("Ошибка: гамма не была сгенерирована.")
                self.binary_decrypted_text.clear()
                self.gamma_text.clear()
                return

            binary_text = self.encrypted_text
            gamma = self.gamma_text.toPlainText()
            decrypted_binary = ''.join('1' if binary_text[i] != gamma[i] else '0' for i in range(len(binary_text)))
            
            bit_length = 6 if len(ALPHABETS[self.alphabet_choice.currentText()]) > 32 else 5

            # range(0, len(decrypted_binary), bit_length): Создает последовательность индексов с шагом bit_length.
            # decrypted_binary[i:i+bit_length]: Извлекает подстроку длиной bit_length из decrypted_binary, начиная с индекса i.
            # int(decrypted_binary[i:i+bit_length], 2): Преобразует подстроку из двоичного представления в десятичное число.
            # ALPHABETS[self.alphabet_choice.currentText()][...]: Использует десятичное число как индекс для поиска соответствующего символа в алфавите.
            decrypted_text = ''.join(ALPHABETS[self.alphabet_choice.currentText()][int(decrypted_binary[i:i+bit_length], 2)] for i in range(0, len(decrypted_binary), bit_length))
            
            self.decrypted_text.setText(f"Расшифрованное сообщение: {decrypted_text}")
            self.binary_decrypted_text.setText(f"{decrypted_binary}")
        except ValueError as e:
            self.decrypted_text.setText(str(e))
            self.encrypted_text = ""
            self.binary_decrypted_text.clear()

class ChainTab(QWidget, Operations):
    def __init__(self, alphabet_choice):
        super().__init__()

        # Сохраняем ссылку на выбор алфавита
        self.alphabet_choice = alphabet_choice

        # Основной макет
        layout = QFormLayout()

        # Поле ввода для исходного сообщения
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Введите исходное сообщение")
        self.input_text.textChanged.connect(self.update_binary_text)
        layout.addRow(QLabel("Исходное сообщение:"), self.input_text)

        # Поле для двоичного представления исходного сообщения
        self.binary_input_text = QTextEdit()
        self.binary_input_text.setReadOnly(True)
        self.binary_input_text.setFixedHeight(50)
        layout.addRow(QLabel("Двоичное представление:"), self.binary_input_text)

        # Кнопка для генерации итерационного вектора
        self.generate_button = QPushButton("Сгенерировать")
        self.generate_button.clicked.connect(self.generate_iv)
        layout.addRow(self.generate_button)

        # Поле для отображения итерационного вектора
        self.iv_text = QTextEdit()
        self.iv_text.setReadOnly(True)
        self.iv_text.setFixedHeight(50)
        layout.addRow(QLabel("Итерационный вектор:"), self.iv_text)

        # Поле для ввода ключа
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Введите ключ")
        self.key_input.textChanged.connect(self.update_binary_key)
        layout.addRow(QLabel("Ключ:"), self.key_input)

        # Поле для двоичного представления ключа
        self.binary_key_input = QTextEdit()
        self.binary_key_input.setReadOnly(True)
        self.binary_key_input.setFixedHeight(50)
        layout.addRow(QLabel("Двоичное представление ключа:"), self.binary_key_input)

        # Кнопка для шифрования
        self.encrypt_button = QPushButton("Зашифровать")
        self.encrypt_button.clicked.connect(self.encrypt_text)
        layout.addRow(self.encrypt_button)

        # Поле для отображения IV2
        self.iv2_text = QTextEdit()
        self.iv2_text.setReadOnly(True)
        self.iv2_text.setFixedHeight(50)
        layout.addRow(QLabel("IV2:"), self.iv2_text)

        # Поле для вывода результата шифрования
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFixedHeight(50)
        layout.addRow(QLabel("Результат шифрования:"), self.output_text)

        # Кнопка для дешифрования
        self.decrypt_button = QPushButton("Расшифровать")
        self.decrypt_button.clicked.connect(self.decrypt_text)
        layout.addRow(self.decrypt_button)

        # Поле для вывода расшифрованного сообщения
        self.decrypted_text = QLabel("Расшифрованное сообщение:")
        layout.addRow(self.decrypted_text)

        # Поле для вывода расшифрованного сообщения в двоичном виде
        self.binary_decrypted_text = QTextEdit()
        self.binary_decrypted_text.setReadOnly(True)
        self.binary_decrypted_text.setFixedHeight(50)
        layout.addRow(QLabel("Двоичное представление расшифрованного сообщения:"), self.binary_decrypted_text)

        self.setLayout(layout)
        self.encrypted_text = ""  # Поле для хранения зашифрованного текста

        # Устанавливаем начальный валидатор
        self.update_validator()

        # Подключаем обновление валидатора при изменении выбора алфавита
        self.alphabet_choice.currentIndexChanged.connect(self.update_validator)

    def update_validator(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]

        regex = QRegExp(f"[{''.join(alphabet)}]*")

        validator = QRegExpValidator(regex)

        self.input_text.setValidator(validator)
        self.input_text.clear()

        # Обновляем валидатор для поля ввода ключа
        self.setup_key_validator()

        # Обнуляем все значения
        self.binary_input_text.clear()
        self.iv_text.clear()
        self.key_input.clear()
        self.binary_key_input.clear()
        self.iv2_text.clear()
        self.output_text.clear()
        self.decrypted_text.setText("Расшифрованное сообщение:")
        self.binary_decrypted_text.clear()
        self.encrypted_text = ""

    def setup_key_validator(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        regex = QRegExp(f"[{''.join(alphabet)}]*")
        validator = QRegExpValidator(regex)
        self.key_input.setValidator(validator)
        self.key_input.clear()

    def update_binary_text(self):
        text = self.input_text.text()
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        self.binary_input_text.setText(self.to_binary(text, alphabet))
        self.iv_text.clear()  # Обнуляем итерационный вектор при изменении текста

    def update_binary_key(self):
        key = self.key_input.text()
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        self.binary_key_input.setText(self.to_binary(key, alphabet))

    def generate_iv(self):
        bit_length = 6 if len(ALPHABETS[self.alphabet_choice.currentText()]) > 32 else 5
        iv = self.generate_gamma(bit_length)
        self.iv_text.setText(iv)

    def encrypt_text(self):
        try:
            binary_text = self.binary_input_text.toPlainText()
            key = self.key_input.text()
            iv = self.iv_text.toPlainText()
            if not binary_text or not key or not iv:
                self.output_text.setText("Ошибка: введите текст, ключ и сгенерируйте итерационный вектор.")
                self.iv2_text.setText("")
                self.encrypted_text = ""
                self.decrypted_text.setText("Расшифрованное сообщение:")
                self.binary_decrypted_text.clear()
                return

            binary_key = self.binary_key_input.toPlainText()
            iv2 = ''.join('1' if binary_key[i] != iv[i] else '0' for i in range(len(iv)))
            self.iv2_text.setText(iv2)

            bit_length = 6 if len(ALPHABETS[self.alphabet_choice.currentText()]) > 32 else 5
            blocks = [binary_text[i:i+bit_length] for i in range(0, len(binary_text), bit_length)]

            encrypted_blocks = []
            previous_block = iv2
            for block in blocks:
                encrypted_block = ''.join('1' if block[i] != previous_block[i] else '0' for i in range(bit_length))
                encrypted_blocks.append(encrypted_block)
                previous_block = encrypted_block

            self.encrypted_text = ''.join(encrypted_blocks)
            self.output_text.setText(f"{self.encrypted_text}")
        except ValueError as e:
            self.output_text.setText(str(e))
            self.encrypted_text = ""
            self.decrypted_text.setText("Расшифрованное сообщение:")
            self.binary_decrypted_text.clear()

    def decrypt_text(self):
        try:
            if not self.encrypted_text:
                self.decrypted_text.setText("Ошибка: нет текста для расшифровки.")
                self.binary_decrypted_text.clear()
                return

            binary_text = self.encrypted_text
            iv2 = self.iv2_text.toPlainText()
            bit_length = 6 if len(ALPHABETS[self.alphabet_choice.currentText()]) > 32 else 5
            blocks = [binary_text[i:i+bit_length] for i in range(0, len(binary_text), bit_length)]

            decrypted_blocks = []
            previous_block = iv2
            for block in blocks:
                decrypted_block = ''.join('1' if block[i] != previous_block[i] else '0' for i in range(bit_length))
                decrypted_blocks.append(decrypted_block)
                previous_block = block

            decrypted_binary = ''.join(decrypted_blocks)
            decrypted_text = ''.join(ALPHABETS[self.alphabet_choice.currentText()][int(decrypted_binary[i:i+bit_length], 2)] for i in range(0, len(decrypted_binary), bit_length))

            self.decrypted_text.setText(f"Расшифрованное сообщение: {decrypted_text}")
            self.binary_decrypted_text.setText(f"{decrypted_binary}")
        except ValueError as e:
            self.decrypted_text.setText(str(e))
            self.encrypted_text = ""
            self.binary_decrypted_text.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoResistantApp()
    window.show()
    sys.exit(app.exec_())