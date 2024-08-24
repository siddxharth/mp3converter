from pymongo import MongoClient
from gridfs import GridFS
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['conversion_db']
fs = GridFS(db)

def save_file(file_path, filename):
    with open(file_path, 'rb') as f:
        fs.put(f, filename=filename, upload_date=datetime.utcnow())

def get_file(filename):
    file = fs.find_one({'filename': filename})
    if file:
        return file.read()

def save_conversion_record(user_id, original_file, converted_file, conversion_date):
    db.conversions.insert_one({
        'user_id': user_id,
        'original_file': original_file,
        'converted_file': converted_file,
        'conversion_date': conversion_date
    })
