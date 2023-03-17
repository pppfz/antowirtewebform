import sys
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QMimeData

class ImageUploader(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle('图片上传')
        self.setGeometry(100, 100, 600, 400)

        # 创建标签和按钮
        self.label = QLabel(self)
        self.label.setText('请上传图片')
        self.button = QPushButton('上传', self)
        self.button.clicked.connect(self.upload_image)

        # 创建布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        # 设置窗口布局
        self.setLayout(hbox)

        # 设置窗口可接受拖拽事件
        self.setAcceptDrops(True)

    def upload_image(self):
        # 打开文件对话框
        file_path, _ = QFileDialog.getOpenFileName(self, '选择图片', '', 'Image files (*.jpg *.png *.jpeg)')
        if file_path:
            # 复制文件并重命名
            current_dir = os.path.dirname(os.path.abspath(__file__))
            new_path = os.path.join(current_dir, '1.png')
            shutil.copy(file_path, new_path)

            # 加载图片
            pixmap = QPixmap(new_path)
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)

            # 关闭窗口
            self.close()

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()  # 接受拖拽事件
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls():
            file_path = e.mimeData().urls()[0].toLocalFile()
            if file_path.endswith('.jpg') or file_path.endswith('.png') or file_path.endswith('.jpeg'):
                # 复制文件并重命名
                current_dir = os.path.dirname(os.path.abspath(__file__))
                new_path = os.path.join(current_dir, '1.png')
                shutil.copy(file_path, new_path)

                # 加载图片
                pixmap = QPixmap(new_path)
                self.label.setPixmap(pixmap)
                self.label.setScaledContents(True)

                # 关闭窗口
                self.close()
        e.accept()  # 接受放置事件

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     uploader = ImageUploader()
#     uploader.show()
#     sys.exit(app.exec_())
