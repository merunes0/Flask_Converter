#TODO добавить конвертацию .pdf в .word

from flask import Flask, request, render_template
from docx import Document


app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template("converter.html")


@app.route('/uploader', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        f = request.files['file']
        file_content = f.read()

        new_doc = Document()
        new_doc.add_paragraph(
            file_content.decode("utf-8"))

        new_file_path = f.filename.replace(".txt", ".doc")
        new_doc.save(new_file_path)
        return render_template("result.html", original_filename=f.filename, new_filename=new_file_path)
    return 'Файл не выбран'


if __name__ == '__main__':
    app.run(debug=True)
