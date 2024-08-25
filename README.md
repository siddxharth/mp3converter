MP4 to MP3 Converter
# MP4 to MP3 Converter

This application, utilizing Flask for the backend and ReactJS for the frontend, enables users to convert MP4 video files into MP3 audio files. It offers an easy-to-use interface where users can upload their MP4 files and download the resulting MP3 files seamlessly.

## Features
- Easy Conversion: Convert MP4 videos to MP3 audio with a few clicks.
- User-Friendly Interface: Simple and clean UI built with ReactJS.

## Prerequisites
- Python 3.x
- Node.js and npm
- Flask
- ReactJS

## How to Run
### Backend
1. Navigate to the backend directory
    ```sh
    cd /backend
    ```
2. Create a virtual environment
    ```sh
    python3 -m venv .venv
    ```
 4. Activate the virtual environment
    ```sh
    source .venv/bin/activate
    ```
3. Install the required Python packages:
    ```sh
    pip3 install -r requirements.txt
    ```
4. Run the application in development mode
   ```sh
    flask run --debug
    ```

### Frontend
1. Navigate to the frontend directory
   ```sh
    cd frontend/
    ```
2. Install the required npm packages
   ```sh
    npm install
    ```
3. Run the application in development mode
   ```sh
    npm run dev
    ```

## Project Structure
```
mp3converter/
├── backend/
│   ├── app
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── conversion.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── run.py
│   │   └── static/
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.json
├── .gitignore
└── README.md
```

## License
    - This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact
For any questions or suggestions, please contact [Siddharth Khatri](siddxharth@gmail.com).
