# Theft Detection Application

This project is a theft detection application that utilizes machine learning to identify potential theft incidents in real-time. The application is divided into two main parts: the backend and the frontend.

## Project Structure

```
theft-detection-app
├── backend
│   ├── mini_project_4.py        # Main logic for theft detection
│   ├── requirements.txt          # Python dependencies for backend
│   └── README.md                 # Documentation for backend
├── frontend
│   ├── public
│   │   └── index.html            # Main HTML file for frontend
│   ├── src
│   │   ├── App.js                # Main React component
│   │   ├── index.js              # Entry point for React application
│   │   ├── components
│   │   │   └── TheftDetection.js  # UI for theft detection
│   │   └── styles
│   │       └── App.css           # CSS styles for frontend
├── package.json                  # Configuration for npm
└── README.md                     # Overall project documentation
```

## Backend

The backend is implemented in Python and includes the following:

- **mini_project_4.py**: Contains the main logic for theft detection, including functions for sending email alerts and detecting theft using a machine learning model.
- **requirements.txt**: Lists the Python dependencies required for the backend application, such as pandas, numpy, scikit-learn, and OpenCV.
- **README.md**: Provides documentation for the backend, including setup instructions and usage details.

## Frontend

The frontend is built using React and includes the following:

- **public/index.html**: The main HTML file that serves as the entry point for the web application.
- **src/App.js**: The main React component that sets up the application structure and routing.
- **src/index.js**: The entry point for the React application, rendering the `App` component into the DOM.
- **src/components/TheftDetection.js**: A React component that handles the user interface for theft detection.
- **src/styles/App.css**: Contains the CSS styles for the frontend application.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the backend directory and install the required Python packages:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. Navigate to the frontend directory and install the required npm packages:
   ```
   cd frontend
   npm install
   ```

## Usage

- Start the backend server by running:
  ```
  python mini_project_4.py
  ```

- Start the frontend application by running:
  ```
  npm start
  ```

Visit `http://localhost:3000` in your web browser to access the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.