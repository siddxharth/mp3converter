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

        # Save files to GridFS
        save_file(file_path, filename)
        save_file(mp3_path, filename.replace('.mp4', '.mp3'))

        user_id = request.form.get('user_id')  # Get user ID from form data
        save_conversion_record(user_id, filename, filename.replace('.mp4', '.mp3'), datetime.utcnow())

        return jsonify({'message': 'File converted successfully', 'mp3_file': mp3_path}), 200

    return jsonify({'error': 'Invalid file type'}), 400

@bp.route('/files/<user_id>', methods=['GET'])
def list_files(user_id):
    # Retrieve all conversion records for the given user_id
    conversions = list(db.conversions.find({'user_id': user_id}, {'_id': 0, 'original_file': 1, 'converted_file': 1, 'conversion_date': 1}))
    return jsonify(conversions), 200

@bp.route('/file/<filename>', methods=['GET'])
def fetch_file(filename):
    file_data = get_file(filename)
    if file_data:
        return send_file(
            io.BytesIO(file_data),
            download_name=filename,  # Use download_name instead of attachment_filename
            as_attachment=True
        )
    return jsonify({'error': 'File not found'}), 404