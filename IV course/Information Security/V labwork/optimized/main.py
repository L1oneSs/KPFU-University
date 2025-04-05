# -*- coding: utf-8 -*-
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from factor_ui import Ui_MainWindow
from quadratic_sieve import factorize, decode_secret_word


class FactorizationThread(QThread):
    finish_signal = pyqtSignal(tuple, float)

    def __init__(self, function, N):
        super().__init__()
        self.function = function
        self.N = N

    def run(self):
        start_time = time.time()
        result = self.function(self.N)
        elapsed_time = time.time() - start_time
        if not result:
            result = None, None, None, None
        self.finish_signal.emit(result, elapsed_time)


class DecodingThread(QThread):
    finish_signal = pyqtSignal(tuple, float)

    def __init__(self, function, N, E, Sw):
        super().__init__()
        self.function = function
        self.N = N
        self.E = E
        self.Sw = Sw

    def run(self):
        start_time = time.time()
        result = self.function(self.N, self.E, self.Sw)
        elapsed_time = time.time() - start_time
        if not result:
            result = None, None, None, None
        self.finish_signal.emit(result, elapsed_time)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.worker2 = None
        self.worker = None
        self.setupUi(self)

        self.setFixedSize(749, 389)

        self.factorFirstPrime.setReadOnly(True)
        self.factorSecondPrime.setReadOnly(True)
        self.factorRuntime.setReadOnly(True)
        self.factorBSmooth.setReadOnly(True)
        self.factorSolutions.setReadOnly(True)

        self.decodeFirstPrime.setReadOnly(True)
        self.decodeSecondPrime.setReadOnly(True)
        self.decodeRuntime.setReadOnly(True)
        self.decodePrivateKey.setReadOnly(True)
        self.decodeDecodedWord.setReadOnly(True)

        self.factorGroupBox.setEnabled(False)
        self.factorGroupBox.setVisible(False)
        self.loadingGroupBox.setVisible(False)

        self.groupbox_layout = QVBoxLayout()
        self.loadingGroupBox.setLayout(self.groupbox_layout)

        self.loading_label = QLabel()
        self.loading_label.setAlignment(Qt.AlignCenter)  # Центрирование GIF
        self.loading_gif = QMovie("../misc/loading.gif")
        self.loading_label.setMovie(self.loading_gif)

        self.groupbox_layout.addWidget(self.loading_label)

        self.decodeGroupBox.setEnabled(False)
        self.decodeGroupBox.setVisible(False)
        self.loadingGroupBox2.setVisible(False)

        self.groupbox_layout2 = QVBoxLayout()
        self.loadingGroupBox2.setLayout(self.groupbox_layout2)

        self.loading_label2 = QLabel()
        self.loading_label2.setAlignment(Qt.AlignCenter)
        self.loading_gif2 = QMovie("../misc/loading.gif")
        self.loading_label2.setMovie(self.loading_gif2)

        self.groupbox_layout2.addWidget(self.loading_label2)

        self.factorizeButton.clicked.connect(self.factorize_number)
        self.decodeButton.clicked.connect(self.decode_secret_word)

    def factorize_number(self):
        N = self.factorNumberText.toPlainText()

        if not N or not N.isdigit():
            return

        self.loadingGroupBox.setVisible(True)
        self.loading_gif.start()

        self.factorGroupBox.setEnabled(False)
        self.factorGroupBox.setVisible(False)

        self.factorizeButton.setEnabled(False)

        if not self.worker or not self.worker.isRunning():
            self.worker = FactorizationThread(factorize, int(N))
            self.worker.finish_signal.connect(self.on_factorization_finished)
            self.worker.start()

    def on_factorization_finished(self, result, elapsed_time):
        self.loading_gif.stop()
        self.loadingGroupBox.setVisible(False)
        self.factorGroupBox.setEnabled(True)
        self.factorGroupBox.setVisible(True)
        self.factorizeButton.setEnabled(True)

        self.factorFirstPrime.setPlainText(f"{result[0]}")
        self.factorSecondPrime.setPlainText(f"{result[1]}")
        self.factorBSmooth.setPlainText(f"{result[2]}")
        self.factorSolutions.setPlainText(f"{result[3]}")
        self.factorRuntime.setPlainText(f"{elapsed_time:.2f} сек")

    def decode_secret_word(self):
        N = self.decodeNumberText.toPlainText()
        E = self.decodePublicKey.toPlainText()
        Sw = self.decodeSecretWord.toPlainText()

        if not N or not E or not Sw or not N.isdigit() or not E.isdigit() or not Sw.isdigit():
            return

        self.loadingGroupBox2.setVisible(True)
        self.loading_gif2.start()

        self.decodeGroupBox.setEnabled(False)
        self.decodeGroupBox.setVisible(False)

        self.decodeButton.setEnabled(False)

        if not self.worker2 or not self.worker2.isRunning():
            self.worker2 = DecodingThread(decode_secret_word, int(N), int(E), int(Sw))
            self.worker2.finish_signal.connect(self.on_decoding_finished)
            self.worker2.start()

    def on_decoding_finished(self, result, elapsed_time):
        self.loading_gif2.stop()
        self.loadingGroupBox2.setVisible(False)
        self.decodeGroupBox.setEnabled(True)
        self.decodeGroupBox.setVisible(True)
        self.decodeButton.setEnabled(True)

        self.decodeFirstPrime.setPlainText(f"{result[0]}")
        self.decodeSecondPrime.setPlainText(f"{result[1]}")
        self.decodePrivateKey.setPlainText(f"{result[2]}")
        self.decodeDecodedWord.setPlainText(f"{result[3]}")
        self.decodeRuntime.setPlainText(f"{elapsed_time:.2f} сек")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
