import os
import sys
import qdarkstyle  
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSize
from PIL import Image

import requests
class IconExtractorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon Extractor')
        self.setFixedSize(500, 420)

        layout = QtWidgets.QVBoxLayout(self)

        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        top_layout = QtWidgets.QHBoxLayout()

        emoji_icon = QtGui.QIcon('./assets/fds.png')
        self.emoji_label = QtWidgets.QLabel(self)
        self.emoji_label.setPixmap(emoji_icon.pixmap(100, 100))
        top_layout.addWidget(self.emoji_label, alignment=QtCore.Qt.AlignCenter)
        layout.addLayout(top_layout)

        self.path_label = QtWidgets.QLabel('Caminho do arquivo:', self)
        layout.addWidget(self.path_label)

        self.path_layout = QtWidgets.QHBoxLayout()
        self.path_edit = QtWidgets.QLineEdit(self)
        self.path_layout.addWidget(self.path_edit)
        self.path_button = QtWidgets.QPushButton('Selecionar', self)
        self.path_button.clicked.connect(self.select_file)
        self.path_layout.addWidget(self.path_button)
        layout.addLayout(self.path_layout)

        self.save_label = QtWidgets.QLabel('Local de salvamento:', self)
        layout.addWidget(self.save_label)

        self.save_layout = QtWidgets.QHBoxLayout()
        self.save_edit = QtWidgets.QLineEdit(self)
        self.save_layout.addWidget(self.save_edit)
        self.save_button = QtWidgets.QPushButton('Selecionar', self)
        self.save_button.clicked.connect(self.select_folder)
        self.save_layout.addWidget(self.save_button)
        layout.addLayout(self.save_layout)

        self.file_type_label = QtWidgets.QLabel('Tipo de arquivo:', self)
        layout.addWidget(self.file_type_label)

        self.file_type_combobox = QtWidgets.QComboBox(self)
        self.file_type_combobox.addItems(['PNG', 'ICO', 'SVG', 'BMP', 'GIF', 'TIFF'])
        layout.addWidget(self.file_type_combobox)

        self.size_label = QtWidgets.QLabel('Tamanho do ícone:', self)
        layout.addWidget(self.size_label)

        self.size_spinbox = QtWidgets.QSpinBox(self)
        self.size_spinbox.setMinimum(1)
        self.size_spinbox.setMaximum(1000)  
        self.size_spinbox.setValue(100)  
        layout.addWidget(self.size_spinbox)

        self.extract_button = QtWidgets.QPushButton('Extrair Ícone', self)
        self.extract_button.clicked.connect(self.extract_icons)
        layout.addWidget(self.extract_button)

        self.result_label = QtWidgets.QLabel(self)
        layout.addWidget(self.result_label)

        self.movie_label = QtWidgets.QLabel(self)
        self.movie = QtGui.QMovie("./assets/R.gif")
        self.movie_label.setMovie(self.movie)
        self.movie.start()
        layout.addWidget(self.movie_label)

    def select_file(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, 'Selecione o arquivo')
        if file_path:
            self.path_edit.setText(file_path)

    def select_folder(self):
        folder_dialog = QtWidgets.QFileDialog(self)
        folder_path = folder_dialog.getExistingDirectory(self, 'Selecione a pasta', QtCore.QDir.homePath())
        if folder_path:
            self.save_edit.setText(folder_path)

    def extract_icons(self):
        try:
            path = self.path_edit.text()
            save_path = self.save_edit.text()
            file_type_index = self.file_type_combobox.currentIndex()
            file_types = ['png', 'ico', 'svg', 'bmp', 'gif', 'tiff']
            file_type = file_types[file_type_index]

            model = QtWidgets.QFileSystemModel()
            icon = model.fileIcon(model.index(path))

            size = self.size_spinbox.value()

            pixmap = icon.pixmap(QSize(size, size))
            image_path = os.path.join(save_path, f"icon.{file_type}")
            if pixmap.toImage().save(image_path, quality=100):
                file_name = os.path.basename(image_path)
                file_size = os.path.getsize(image_path)
                self.result_label.setText(f"<font color='green'>Ícone extraído com sucesso em tamanho {size}x{size}!</font>")
                self.show_icon_info_popup(file_name, file_size, size, image_path)
            else:
                self.result_label.setText("<font color='yellow'>Nenhum ícone extraído.</font>")

        except FileNotFoundError:
            self.result_label.setText("<font color='red'>Caminho do arquivo não encontrado.</font>")
        except PermissionError:
            self.result_label.setText("<font color='red'>Permissão negada para acessar o arquivo.</font>")


    def clear_ui_fields(self):
        self.path_edit.clear()
        self.save_edit.clear()
        self.file_type_combobox.setCurrentIndex(0)
        self.size_spinbox.setValue(100)
        self.result_label.clear()

    def show_icon_info_popup(self, file_name, file_size, size, image_path):
        popup = QtWidgets.QMessageBox(self)
        popup.setWindowTitle("Informações do Ícone")

        image = Image.open(image_path)
        image_format = image.format
        image_mode = image.mode
        image_width, image_height = image.size

        image_colors = image.getcolors()
        unique_colors = len(image_colors) if image_colors else 0

        info_text = (
            f"Nome do Arquivo: {file_name}\n"
            f"Tamanho do Arquivo: {file_size} bytes\n"
            f"Formato da Imagem: {image_format}\n"
            f"Modo da Imagem: {image_mode}\n"
            f"Resolução da Imagem: {image_width}x{image_height}\n"
            f"File size: {size}px\n"
            f"Número de Cores Únicas: {unique_colors}\n"
            f"Caminho do Arquivo: {image_path}"
        )
        popup.setText(info_text)

        icon = QtGui.QIcon(image_path)
        popup.setIconPixmap(icon.pixmap(64, 64))  

        popup.finished.connect(self.clear_ui_fields)

        popup.addButton(QtWidgets.QMessageBox.Ok)
        popup.exec_()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    icon = QtGui.QIcon('./assets/rose.png')
    app.setWindowIcon(icon)
    ex = IconExtractorApp()
    ex.show()
    sys.exit(app.exec_())
