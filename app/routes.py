from flask import Blueprint, request, jsonify, send_file
from werkzeug.utils import secure_filename
from .conversion import convert_mp4_to_mp3
from .models import save_file, get_file, save_conversion_record, db
import os
from datetime import datetime
import io

bp = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = {'mp4'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join('static/uploads', filename)
        file.save(file_path)

        mp3_path = file_path.replace('.mp4', '.mp3')
        convert_mp4_to_mp3(file_path, mp3_path)

        user_id = request.form.get('user_id')

        original_file_id = save_file(file_path, user_id)
        converted_file_id = save_file(mp3_path, user_id)

        save_conversion_record(user_id, original_file_id, converted_file_id, datetime.utcnow())

        return jsonify({'message': 'File converted successfully', 'mp3_file': mp3_path}), 200

    return jsonify({'error': 'Invalid file type'}), 400

@bp.route('/files/<user_id>', methods=['GET'])
def list_files(user_id):
    conversions = list(db.conversions.find({'user_id': user_id}, {'_id': 0, 'original_file_id': 1, 'converted_file_id': 1, 'conversion_date': 1}))
    return jsonify(conversions), 200

@bp.route('/file/<file_id>', methods=['GET'])
def fetch_file(file_id):
    file_data = get_file(file_id)
    if file_data:
        return send_file(
            io.BytesIO(file_data),
            download_name=f"{file_id}.mp4",
            as_attachment=True
        )
    return jsonify({'error': 'File not found'}), 404
