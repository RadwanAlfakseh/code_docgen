# Python API Project

This project is a simple Python API built using Flask. It serves as a template for creating RESTful APIs with a structured folder layout.

## Project Structure

```
python-api-project
├── src
│   ├── app.py
│   ├── controllers
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── services
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-api-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/app.py
```

The API will be available at `http://localhost:5000`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.