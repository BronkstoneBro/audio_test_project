import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QFont
import moviepy.editor as mp
from pathlib import Path


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video to Audio Extractor')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.select_button = QPushButton('Select Video File', self)
        self.select_button.setFont(QFont('Arial', 12))
        self.select_button.setStyleSheet('background-color: #4CAF50; color: white; border: none; padding: 10px;')
        self.select_button.clicked.connect(self.extract_audio)
        layout.addWidget(self.select_button)

        self.result_label = QLabel('No file selected.', self)
        self.result_label.setFont(QFont('Arial', 12))
        self.result_label.setStyleSheet('color: #333;')
        layout.addWidget(self.result_label)

    def extract_audio(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Video File', '', 'Video Files (*.mp4 *.avi *.mov)')
        if file_path:
            video_file = Path(file_path)
            video = mp.VideoFileClip(str(video_file))
            audio = video.audio
            output_path = video_file.with_suffix('.mp3')
            audio.write_audiofile(output_path)
            self.result_label.setText(f"Audio extracted and saved to: {output_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
