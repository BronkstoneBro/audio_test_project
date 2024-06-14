# Video to Audio Extractor

This project provides a simple GUI application to extract audio from video files using PyQt5 and MoviePy.

## Requirements

- Python 3.x
- PyQt5
- MoviePy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/BronkstoneBro/audio_test_project.git
    cd audio_test_project
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python audio.py
    ```

2. Click on "Select Video File" to choose the video file you want to extract the audio from.

3. The extracted audio will be saved in the same directory as the video file with a `.mp3` extension.

## Dependencies

- PyQt5
- MoviePy
- pathlib

## Troubleshooting

If you encounter issues with Qt platform plugins, ensure you have the necessary dependencies installed:

    ```bash
    sudo apt-get install libxcb-xinerama0
    sudo apt-get install libxkbcommon-x11-0
    sudo apt-get install libxcb-util1 libxcb-image0 libxcb-randr0 libxcb-keysyms1 libxcb-icccm4 libxcb-render-util0 libxcb-xkb1 libxcb-xinerama0 libxcb-xfixes0
    sudo apt-get install libgl1-mesa-glx
    sudo apt-get install libglib2.0-0
    ```

## License

This project is licensed under the MIT License.
