from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
import tempfile
import os
import PyPDF2


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        print(request.files)
        if "pdf_file" not in request.files:
            return redirect(url_for("home"))

        pdf_file = request.files["pdf_file"]

        if pdf_file.filename == "":
            return redirect(url_for("home"))

        temp_dir = tempfile.gettempdir()
        temp_file_path = os.path.join(temp_dir, pdf_file.filename)
        print(temp_file_path)
        pdf_file.save(temp_file_path)

        extracted_text = extract_text_from_pdf(temp_file_path)
        print(extracted_text)

        os.remove(temp_file_path)

        generated_audio = gTTS(text=extracted_text, lang="en")
        generated_audio.save(f"static/audio/{pdf_file.filename.split('.')[0]}.mp3")
        return render_template(
            "result.html", filepath=f"{pdf_file.filename.split('.')[0]}.mp3"
        )


if __name__ == "__main__":
    app.run(debug=True)
