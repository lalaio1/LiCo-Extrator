import os
import sys
import qdarkstyle  # Importe o módulo QDarkStyle
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSize



class IconExtractorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon Extractor')
        self.setFixedSize(500, 400)

        layout = QtWidgets.QVBoxLayout(self)

        # Aplicar o estilo escuro
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # Layout para a parte superior
        top_layout = QtWidgets.QHBoxLayout()

        # Emoji Icon (Banner)
        emoji_icon = QtGui.QIcon('./assets/fds.png')  # Coloque o caminho do seu arquivo de ícone de emoji
        self.emoji_label = QtWidgets.QLabel(self)
        self.emoji_label.setPixmap(emoji_icon.pixmap(100, 100))
        top_layout.addWidget(self.emoji_label, alignment=QtCore.Qt.AlignCenter)  # Centralize o banner horizontalmente
        layout.addLayout(top_layout)

        # Labels e Edit Lines
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

        # Tamanho do ícone
        self.size_label = QtWidgets.QLabel('Tamanho do ícone:', self)
        layout.addWidget(self.size_label)

        self.size_spinbox = QtWidgets.QSpinBox(self)
        self.size_spinbox.setMinimum(1)
        self.size_spinbox.setMaximum(1000)  # Defina o valor máximo conforme necessário
        self.size_spinbox.setValue(100)  # Valor padrão
        layout.addWidget(self.size_spinbox)

        # Botões
        self.extract_button = QtWidgets.QPushButton('Extrair Ícone', self)
        self.extract_button.clicked.connect(self.extract_icons)
        layout.addWidget(self.extract_button)

        # Result Label
        self.result_label = QtWidgets.QLabel(self)
        layout.addWidget(self.result_label)

        # Animação
        self.movie_label = QtWidgets.QLabel(self)
        self.movie = QtGui.QMovie("./assets/R.gif")  # Coloque o caminho do seu arquivo de animação
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

            # Obtém o tamanho escolhido pelo usuário
            size = self.size_spinbox.value()

            pixmap = icon.pixmap(QSize(size, size))
            image_path = os.path.join(save_path, f"icon.{file_type}")
            if pixmap.toImage().save(image_path, quality=100):
                self.result_label.setText(f"Ícone extraído com sucesso em tamanho {size}x{size}!")
                self.result_label.setStyleSheet('color: green;')
            else:
                self.result_label.setText("Nenhum ícone extraído.")
                self.result_label.setStyleSheet('color: yellow;')

        except FileNotFoundError:
            self.result_label.setText('Caminho do arquivo não encontrado.')
            self.result_label.setStyleSheet('color: red;')
        except PermissionError:
            self.result_label.setText('Permissão negada para acessar o arquivo.')
            self.result_label.setStyleSheet('color: red;')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = IconExtractorApp()
    ex.show()
    sys.exit(app.exec_())
