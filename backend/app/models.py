from pymongo import MongoClient
from gridfs import GridFS
from datetime import datetime
import uuid

client = MongoClient('mongodb://localhost:27017/')
db = client['conversion_db']
fs = GridFS(db)

def generate_unique_id():
    return str(uuid.uuid4())

def save_file(file_path, user_id):
    file_id = generate_unique_id()
    with open(file_path, 'rb') as f:
        fs.put(f, filename=file_id, upload_date=datetime.utcnow(), user_id=user_id)
    return file_id

def get_file(file_id):
    file = fs.find_one({'filename': file_id})
    if file:
        return file.read()

def save_conversion_record(user_id, original_file_id, converted_file_id, conversion_date):
    db.conversions.insert_one({
        'user_id': user_id,
        'original_file_id': original_file_id,
        'converted_file_id': converted_file_id,
        'conversion_date': conversion_date
    })
