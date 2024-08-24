from flask import Flask, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "static/uploads"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route("/upload/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            return "No file found"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('view_media', media=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/view_media/', methods=["GET"])
def view_media():
    if 'media' not in request.args:
        return "No file name provided"
    
    media = request.args['media']
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], media)
    
    # Check if the file exists
    if not os.path.exists(full_filename):
        return "File not found"
    
    # Generate the URL for the media
    media_url = url_for('static', filename=f'uploads/{media}')
    
    # Return the media in an HTML response
    return f'''
        <audio controls>
            <source src="{media_url}" type="audio/mp3">
            Your browser doesn't support the audio element.
        </audio>
    '''

if __name__ == "__main__":
    app.run(debug=True)
