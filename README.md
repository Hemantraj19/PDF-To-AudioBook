# Flask PDF to Speech Converter

This Flask web application allows users to convert text from PDF files into speech. It utilizes the `Flask` framework for web development and `PyPDF2` for extracting text from PDF files. The speech synthesis is handled by the `gTTS` (Google Text-to-Speech) library.

## Features

1. **PDF Upload**: Users can upload PDF files through a web interface.
2. **Text Extraction**: The application extracts text from the uploaded PDF file.
3. **Speech Generation**: The extracted text is converted into speech using the gTTS library.
4. **Audio Output**: Converted speech is saved as an MP3 file.
5. **Web Interface**: Simple web interface for user interaction.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hemantraj19/PDF-To-AudioBook.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-pdf-to-speech
   ```

3. Install dependencies:

   ```bash
   pip install Flask gTTS PyPDF2
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Upload a PDF file using the provided form.
2. Click on the "Convert" button.
3. Wait for the conversion process to complete.
4. Download the generated audio file.

## Dependencies

- **Flask**: A micro web framework for Python.
- **gTTS**: Google Text-to-Speech API wrapper for Python.
- **PyPDF2**: A library capable of splitting, merging, cropping, and transforming PDFs.

## Directory Structure

```
flask-pdf-to-speech/
│
├── static/
│   └── audio/     # Directory to store generated audio files
|   └── css/
|   └── js/
|   └── img/
│
├── templates/
│   ├── index.html       # Homepage HTML template
│   └── result.html      # Result page HTML template
│
├── app.py               # Flask application file
└── README.md            # Project README file
```
