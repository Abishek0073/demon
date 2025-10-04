# README for Backend Theft Detection Application

## Overview
This backend application is part of the Theft Detection App, which utilizes machine learning to detect theft in real-time using video feeds. It includes functionalities for sending email alerts when theft is detected.

## Files
- `mini_project_4.py`: Contains the main logic for theft detection, including email alert functionality and machine learning model integration.
- `requirements.txt`: Lists the Python dependencies required to run the backend application.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/theft-detection-app.git
   cd theft-detection-app/backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Email Credentials**
   Ensure you have set the environment variables for your email credentials:
   - `SENDER_EMAIL`: Your email address
   - `SENDER_PASSWORD`: Your app-generated password

## Usage
To run the theft detection application, execute the following command:
```bash
python mini_project_4.py
```

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.