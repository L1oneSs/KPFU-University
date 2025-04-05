import re
import sys
from collections import Counter
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QComboBox, QMainWindow, QFileDialog, QTextEdit, QFormLayout, QMessageBox
)
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import os
import string


ALPHABETS = {
    "Русский": "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я 0 1 2 3 4 5 6 7 8 9".split(),
    "Английский": "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9".split()
}


class VigenereCipherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифр Виженера")
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
        self.file_tab = FileTab(self.alphabet_choice)
        self.crack_tab = CrackTab(self.alphabet_choice)
        self.tabs.addTab(self.text_tab, "Шифр/Расшифр текста")
        self.tabs.addTab(self.file_tab, "Работа с файлами")
        self.tabs.addTab(self.crack_tab, "Взлом")

    def update_validators(self):
        # Обновляем валидаторы во всех табах
        self.text_tab.update_validator()
        self.file_tab.update_validator()
        self.crack_tab.update_validator()


class CipherOperations:
    @staticmethod
    def vigenere_cipher(text, key, alphabet, decrypt=False):
        key_length = len(key)
        key_as_int = [alphabet.index(char) for char in key]
        text_as_int = [alphabet.index(char) for char in text]
        result = ""

        for i in range(len(text_as_int)):
            if decrypt:
                value = (text_as_int[i] - key_as_int[i % key_length]) % len(alphabet)
            else:
                value = (text_as_int[i] + key_as_int[i % key_length]) % len(alphabet)
            result += alphabet[value]

        return result
    
    @staticmethod
    def preprocess_text(text):
        return ''.join(char.lower() for char in text)


class TextTab(QWidget, CipherOperations):
    def __init__(self, alphabet_choice):
        super().__init__()

        # Сохраняем ссылку на выбор алфавита
        self.alphabet_choice = alphabet_choice

        # Основной макет
        layout = QFormLayout()

        # Поле ввода для исходного сообщения
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Введите исходное сообщение")
        layout.addRow(QLabel("Исходное сообщение:"), self.input_text)

        # Поле для ввода ключа
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Введите ключ")
        layout.addRow(QLabel("Ключ:"), self.key_input)

        # Кнопка для шифрования
        self.encrypt_button = QPushButton("Зашифровать")
        self.encrypt_button.clicked.connect(self.encrypt_text)
        layout.addRow(self.encrypt_button)

        # Кнопка для дешифрования
        self.decrypt_button = QPushButton("Расшифровать")
        self.decrypt_button.clicked.connect(self.decrypt_text)
        layout.addRow(self.decrypt_button)

        # Поле для вывода результата
        self.output_text = QLabel("Результат:")
        layout.addRow(self.output_text)

        self.setLayout(layout)
        self.encrypted_text = ""  # Поле для хранения зашифрованного текста

        # Устанавливаем начальный валидатор
        self.update_validator()

        # Подключаем обновление валидатора при изменении выбора алфавита
        self.alphabet_choice.currentIndexChanged.connect(self.update_validator)

    def update_validator(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]

        regex = QRegExp(f"[{''.join(alphabet)}{''.join(c.upper() for c in alphabet)}]*")

        validator = QRegExpValidator(regex)

        self.input_text.setValidator(validator)
        self.input_text.clear()

        # Обновляем валидатор для поля ввода ключа
        self.setup_key_validator()

    def setup_key_validator(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        regex = QRegExp(f"[{''.join(alphabet)}]*")
        validator = QRegExpValidator(regex)
        self.key_input.setValidator(validator)
        self.key_input.clear()

    def encrypt_text(self):
        try:
            text = self.input_text.text()
            if not text:
                self.output_text.setText("Ошибка: введите текст для шифрования.")
                self.encrypted_text = ""
                return

            key = self.key_input.text()
            if len(key) == 0:
                raise ValueError("Ошибка: введите ключ.")
            alphabet = ALPHABETS[self.alphabet_choice.currentText()]
            preprocessed_text = self.preprocess_text(text)
            self.encrypted_text = self.vigenere_cipher(preprocessed_text, key, alphabet)
            self.output_text.setText(f"Зашифрованное сообщение: {self.encrypted_text}")
        except ValueError as e:
            self.output_text.setText(str(e))
            self.encrypted_text = ""

    def decrypt_text(self):
        try:
            if not self.encrypted_text:
                self.output_text.setText("Ошибка: нет текста для расшифровки.")
                self.encrypted_text = ""
                return

            key = self.key_input.text()
            if len(key) == 0:
                raise ValueError("Ошибка: введите ключ.")
            alphabet = ALPHABETS[self.alphabet_choice.currentText()]
            preprocessed_text = self.preprocess_text(self.encrypted_text)
            decrypted_text = self.vigenere_cipher(preprocessed_text, key, alphabet, decrypt=True)
            self.output_text.setText(f"Расшифрованное сообщение: {decrypted_text}")
        except ValueError as e:
            self.output_text.setText(str(e))
            self.encrypted_text = ""


class FileTab(QWidget, CipherOperations):
    def __init__(self, alphabet_choice):
        super().__init__()
        self.alphabet_choice = alphabet_choice
        layout = QVBoxLayout()

        # Кнопка выбора файла
        self.file_button = QPushButton("Выбрать файл")
        self.file_button.clicked.connect(self.open_file)
        layout.addWidget(self.file_button)

        # Поле для отображения текста из файла
        self.file_text_display = QTextEdit()
        self.file_text_display.setReadOnly(True)
        layout.addWidget(self.file_text_display)

        # Поле для ввода ключа
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Введите ключ")
        layout.addWidget(QLabel("Ключ:"))
        layout.addWidget(self.key_input)

        # Кнопка для шифрования
        self.encrypt_button = QPushButton("Зашифровать")
        self.encrypt_button.clicked.connect(self.encrypt_text)
        layout.addWidget(self.encrypt_button)

        # Поле для отображения зашифрованного текста
        self.encrypted_text_display = QTextEdit()
        self.encrypted_text_display.setReadOnly(True)
        layout.addWidget(QLabel("Зашифрованный текст:"))
        layout.addWidget(self.encrypted_text_display)

        # Кнопка для расшифровки текста
        self.decrypt_button = QPushButton("Расшифровать")
        self.decrypt_button.clicked.connect(self.decrypt_text)
        layout.addWidget(self.decrypt_button)

        # Поле для отображения расшифрованного текста
        self.decrypted_text_display = QTextEdit()
        self.decrypted_text_display.setReadOnly(True)
        layout.addWidget(QLabel("Расшифрованный текст:"))
        layout.addWidget(self.decrypted_text_display)

        # Кнопка для сохранения зашифрованного текста
        self.save_button = QPushButton("Сохранить в файл (Зашифрованный текст)")
        self.save_button.clicked.connect(self.save_file)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.file_text = ""
        self.encrypted_text = ""
        self.decrypted_text = ""

        # Устанавливаем валидатор для поля ввода ключа
        self.setup_key_validator()

    def setup_key_validator(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        regex = QRegExp(f"[{''.join(alphabet)}]*")
        validator = QRegExpValidator(regex)
        self.key_input.setValidator(validator)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Text Files (*.txt);")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.file_text = file.read()

            if all(char.lower() in string.punctuation + " " + "\n—" for char in self.file_text):
                    self.file_text_display.setText("Ошибка: некорректный текст.")
                    self.file_text = ""

            # Проверяем соответствие языка
            elif self.is_valid_text():
                self.file_text_display.setPlainText(self.file_text)
            else:
                self.file_text_display.setPlainText("Ошибка: текст не соответствует выбранному языку.")
                self.file_text = ""
                self.decrypted_text_display.setPlainText("")
                self.encrypted_text_display.setPlainText("")
                self.key_input.clear()
                self.decrypted_text = ""
                self.encrypted_text = ""

    def is_valid_text(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        return all(char.lower() in alphabet for char in self.file_text)
    
    def update_validator(self):
        self.file_text_display.clear()
        self.encrypted_text_display.clear()
        self.file_text = ""
        self.encrypted_text = ""
        self.decrypted_text = ""
        self.decrypted_text_display.clear()
        self.key_input.clear()
        self.setup_key_validator() 

    def encrypt_text(self):
        try:
            if self.file_text == "" or self.file_text == '':
                self.encrypted_text_display.setPlainText("Ошибка: текст не выбран.")
            else:
                key = self.key_input.text()
                if len(key) == 0:
                    raise ValueError("Ошибка: введите ключ.")
                alphabet = ALPHABETS[self.alphabet_choice.currentText()]
                preprocessed_text = self.preprocess_text(self.file_text)    
                self.encrypted_text = self.vigenere_cipher(preprocessed_text, key, alphabet)
                self.encrypted_text_display.setPlainText(self.encrypted_text)
        except ValueError as e:
            self.encrypted_text_display.setPlainText(str(e))

    def decrypt_text(self):
        try:
            if self.encrypted_text == "" or self.encrypted_text == '':
                self.decrypted_text_display.setPlainText("Ошибка: зашифрованный текст не выбран.")
            else:
                key = self.key_input.text()
                if len(key) == 0:
                    raise ValueError("Ошибка: введите ключ.")
                alphabet = ALPHABETS[self.alphabet_choice.currentText()]
                preprocessed_text = self.preprocess_text(self.encrypted_text)
                self.decrypted_text = self.vigenere_cipher(preprocessed_text, key, alphabet, decrypt=True)
                self.decrypted_text_display.setPlainText(self.decrypted_text)
        except ValueError as e:
            self.decrypted_text_display.setPlainText(str(e))

    def save_file(self):
        if self.decrypted_text == "" or self.decrypted_text == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Ошибка: зашифрованный текст не выбран.")
            msg.setWindowTitle("Предупреждение")
            msg.exec_()
        else:
            file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt);")
            if file_path:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.encrypted_text)



class CrackTab(QWidget):
    def __init__(self, alphabet_choice):
        super().__init__()
        self.alphabet_choice = alphabet_choice
        layout = QVBoxLayout()

        # Кнопка для выбора файла
        self.file_button = QPushButton("Выбрать файл")
        self.file_button.clicked.connect(self.open_file)
        layout.addWidget(self.file_button)

        # Поле для отображения зашифрованного текста
        self.encrypted_text_display = QTextEdit()
        self.encrypted_text_display.setReadOnly(True)
        layout.addWidget(QLabel("Зашифрованный текст:"))
        layout.addWidget(self.encrypted_text_display)

        # Кнопка для взлома
        self.crack_button = QPushButton("Взломать")
        self.crack_button.clicked.connect(self.crack_text)
        layout.addWidget(self.crack_button)

        # Поле для отображения предполагаемого ключа
        self.key_display = QLabel("Предполагаемый ключ: ")
        layout.addWidget(self.key_display)

        # Поле для отображения расшифрованного текста
        self.decrypted_text_display = QTextEdit()
        self.decrypted_text_display.setReadOnly(True)
        layout.addWidget(QLabel("Дешифрованный текст:"))
        layout.addWidget(self.decrypted_text_display)

        self.setLayout(layout)

        self.file_text = ""

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Text Files (*.txt);")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.file_text = file.read()
            
            if all(char.lower() in string.punctuation + " " + "\n—" for char in self.file_text):
                self.encrypted_text_display.setText("Ошибка: некорректный текст.")
                self.file_text = ""

            elif self.is_valid_text():
                self.encrypted_text_display.setPlainText(self.file_text)
            else:
                self.encrypted_text_display.setText("Ошибка: текст не соответствует выбранному языку.")
                self.file_text = ""
                self.key_display.setText("Предполагаемый ключ: ")
                self.decrypted_text_display.setPlainText("")

    def is_valid_file(self, file_path):
        file_name = file_path.split("/")[-1]
        return bool(re.match(r"^shifr\d+\.txt$", file_name))

    def is_valid_text(self):
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        return all(char.lower() in alphabet for char in self.file_text)
    
    def update_validator(self):
        self.encrypted_text_display.clear()
        self.file_text = ""
        self.key_display.setText("Предполагаемый ключ: ")
        self.decrypted_text_display.clear()

    def crack_text(self):
        if not self.file_text:
            self.decrypted_text_display.setPlainText("Ошибка: не выбран файл для взлома.")
            self.key_display.setText("Предполагаемый ключ: ")
            return

        text = CipherOperations.preprocess_text(self.file_text)
        alphabet = ALPHABETS[self.alphabet_choice.currentText()]
        key = self.index_of_coincidence(text, alphabet)
        
        if key:
            decrypted_text = CipherOperations.vigenere_cipher(text, key, alphabet, decrypt=True)
            self.key_display.setText(f"Предполагаемый ключ: {key}")
            self.decrypted_text_display.setPlainText(decrypted_text)
        else:
            self.decrypted_text_display.setPlainText("Ключ не найден.")

    def index_of_coincidence(self, text, alphabet):
        def find_key_length(ciphertext, alphabet):

            # avg_ic = 0.0553 if 'о' in alphabet else 0.0667

            avg_ic = 0.0667  # Средний индекс совпадений для русского и английского языков
            ic_table = []
            key_len = 1 
            tolerance = 0.01

            try:
                while True:
                    ic_sum = 0.0
                    # Проходимся по длине ключа
                    for i in range(key_len):
                        # Выделяем всевозможные подстроки с шагом key_len
                        substring = ciphertext[i::key_len]
                        # Подсчитываем частоты букв в подстроке
                        letter_counts = Counter(substring)
                        # Берем длину подстроки
                        substring_len = len(substring)
                        # Индекс совпадения группы = Σ(f × (f-1)) / (N × (N-1))
                        # где:
                        # f - количество появлений буквы 
                        # N - мощность текста
                        ic = sum([letter_counts[letter] * (letter_counts[letter] - 1) for letter in alphabet if letter in letter_counts]) / (substring_len * (substring_len - 1))
                        # Суммируем индексы совпадения для каждой группы
                        ic_sum += ic
                    # Средний индекс совпадения для данной длины ключа
                    average_ic = ic_sum / key_len
                    ic_table.append((key_len, average_ic))

                    # Проверка, если найдено значение, близкое к avg_ic
                    if abs(average_ic - avg_ic) < tolerance:  # Допустимое отклонение
                        return key_len

                    # Увеличиваем длину ключа
                    key_len += 1
            except ZeroDivisionError:
                self.decrypted_text_display.setPlainText("Ключ не найден.")

            # Найти длину ключа, которая ближе всего к avg_ic
            # closest_key_len = min(ic_table, key=lambda x: abs(x[1] - avg_ic))[0]
            # return closest_key_len

        def find_key(ciphertext, key_len, alphabet):
            russian_letter_frequencies = {
                'о': 0.10983, 'е': 0.08483, 'а': 0.07998, 'и': 0.07367, 'н': 0.067,
                'т': 0.06318, 'с': 0.05473, 'р': 0.04746, 'в': 0.04533, 'л': 0.04343,
                'к': 0.03486, 'м': 0.03203, 'д': 0.02977, 'п': 0.02804, 'у': 0.02615,
                'я': 0.02001, 'ы': 0.01898, 'ь': 0.01735, 'г': 0.01687, 'з': 0.01641,
                'б': 0.01592, 'ч': 0.0145, 'й': 0.01208, 'х': 0.00966, 'ж': 0.0094,
                'ш': 0.00718, 'ю': 0.00639, 'ц': 0.00486, 'щ': 0.00361, 'э': 0.00331,
                'ф': 0.00267, 'ъ': 0.00037, 'ё': 0.00013,
                '0': 0.001, '1': 0.001, '2': 0.001, '3': 0.001, '4': 0.001,
                '5': 0.001, '6': 0.001, '7': 0.001, '8': 0.001, '9': 0.001
            }

            english_letter_frequencies = {
                'e': 0.12702, 't': 0.09056, 'a': 0.08167, 'o': 0.07507, 'i': 0.06966,
                'n': 0.06749, 's': 0.06327, 'h': 0.06094, 'r': 0.05987, 'd': 0.04253,
                'l': 0.04025, 'c': 0.02782, 'u': 0.02758, 'm': 0.02406, 'w': 0.0236,
                'f': 0.02228, 'g': 0.02015, 'y': 0.01974, 'p': 0.01929, 'b': 0.01492,
                'v': 0.00978, 'k': 0.00772, 'j': 0.00153, 'x': 0.0015, 'q': 0.00095,
                'z': 0.00074,
                '0': 0.001, '1': 0.001, '2': 0.001, '3': 0.001, '4': 0.001,
                '5': 0.001, '6': 0.001, '7': 0.001, '8': 0.001, '9': 0.001
            }

            
            letter_frequencies = russian_letter_frequencies if 'о' in alphabet else english_letter_frequencies
            key = ''
            # Проходимся по длине ключа
            for i in range(key_len):
                # Выделяем подстроку с шагом key_len
                substring = ciphertext[i::key_len]
                # Подсчитываем частоты букв в подстроке
                letter_counts = Counter(substring)
                best_shift = 0
                max_correlation = 0
                # Проходимся по всем возможным сдвигам
                for shift in range(len(alphabet)):
                    shifted_counts = {}
                    # Перебор всех индексов букв в алфавите
                    for j in range(len(alphabet)):
                        # Подсчитываем частоты букв в сдвинутой подстроке
                        # Сдвинутая буква => ее частота в подстроке
                        # Записываем буква -> частота после сдвига
                        shifted_counts[alphabet[j]] = letter_counts[alphabet[(j + shift) % len(alphabet)]]
                    # Нахождение корреляции
                    correlation = 0
                    for letter in alphabet:
                        # Корреляция = Σ(частота_в_языке × частота_в_сдвинутой_группе)
                        correlation += letter_frequencies.get(letter, 0) * shifted_counts.get(letter, 0)
                    if correlation > max_correlation:
                        max_correlation = correlation
                        best_shift = shift
                # Добавляем букву в ключ
                key += alphabet[best_shift]
            return key

        key_length = find_key_length(text, alphabet)
        if key_length == None:
            self.decrypted_text_display.setPlainText("Не удалось определить длину ключа.")
            return None
        key = find_key(text, key_length, alphabet)
        return key





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VigenereCipherApp()
    window.show()
    sys.exit(app.exec_())


