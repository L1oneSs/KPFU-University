from logger import Logger


logger = Logger()

# class RC4:
#     def __init__(self, key: str):
#         logger.info(f"Инициализация RC4 с ключом: {key}")
#         self.key = [ord(c) for c in str(key)]
#         self.S = list(range(256))
#         self._ksa()
        
#     def _ksa(self):
#         """Key Scheduling Algorithm."""
#         j = 0
#         for i in range(256):
#             j = (j + self.S[i] + self.key[i % len(self.key)]) % 256
#             self.S[i], self.S[j] = self.S[j], self.S[i]
            
#     def encrypt(self, data: str) -> str:
#         S = self.S.copy()  # Создаем копию состояния для каждой операции
#         i = j = 0
#         result = []
        
#         for byte in [ord(c) for c in data]:
#             i = (i + 1) % 256
#             j = (j + S[i]) % 256
#             S[i], S[j] = S[j], S[i]
#             k = S[(S[i] + S[j]) % 256]
#             result.append(chr(byte ^ k))
            
#         encrypted = ''.join(result)
#         return encrypted

class RC4:
    """
    Реализация потокового шифра RC4.
    RC4 генерирует псевдослучайный поток байтов и комбинирует его с открытым текстом операцией XOR.
    """
    def __init__(self, key: str):
        """
        Инициализация RC4 с ключом.
        Args:
            key (str): Ключ шифрования
        """
        logger.info(f"Инициализация RC4 с ключом: {key}")
        # Преобразуем каждый символ ключа в его ASCII код
        self.key = [ord(c) for c in key]
        # Создаем начальную перестановку чисел от 0 до 255
        self.S = list(range(256))
        # Инициализируем S-блок на основе ключа
        self.init_sbox()
        
    def init_sbox(self):
        """
        Инициализация S-блока (Key Scheduling Algorithm).
        Перемешивает начальную перестановку на основе ключа.
        """
        j = 0
        for i in range(256):
            # Обновляем j на основе текущего состояния и ключа
            # Создаем псевдослучайную перестановку 256 раз
            j = (j + self.S[i] + self.key[i % len(self.key)]) % 256
            #   │  │    │       │    │     └─ длина ключа
            #   │  │    │       │    └─ массив ASCII-кодов ключа
            #   │  │    │       └─ индекс в массиве ключа (цикличный)
            #   │  │    └─ значение из S-блока по индексу i
            #   │  └─ предыдущее значение j
            #   └─ результат по модулю 256
            # Меняем местами элементы для создания перестановки
            self.S[i], self.S[j] = self.S[j], self.S[i]
            
    def encrypt(self, data: str) -> str:
        """
        Шифрование/дешифрование данных (Pseudo-Random Generation Algorithm - PRGA).
        
        Args:
            data (str): Входные данные для шифрования/дешифрования
            
        Returns:
            str: Зашифрованный/расшифрованный текст
        """
        # Копируем состояние для независимости операций
        S = self.S.copy()
        i = j = 0
        result = []
        
        # Преобразуем входную строку в байты
        bytes_data = [ord(c) for c in data]
        
        for byte in bytes_data:
            # Генерируем следующий байт ключевого потока
            # Увеличиваем i на 1 по модулю 256
            i = (i + 1) % 256
            # Обновляем j, используя значение из S по индексу i
            j = (j + S[i]) % 256
            # Меняем местами значения S[i] и S[j]
            S[i], S[j] = S[j], S[i]
            # Получаем байт ключевого потока
            k = S[(S[i] + S[j]) % 256]
            # XOR с текущим байтом данных
            encrypted_byte = byte ^ k
            # Преобразуем результат обратно в символ
            result.append(chr(encrypted_byte))
            
        return ''.join(result)
    
    # Дешифрование идентично шифрованию из-за свойств XOR
    decrypt = encrypt