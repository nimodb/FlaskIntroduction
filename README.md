# Flask ToDo App

A simple ToDo application built with Flask and SQLAlchemy.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nimodb/FlaskIntroduction.git

2. Navigate into the project directory:
   ```bash
   cd FlaskIntroduction

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env

4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\env\Scripts\activate
    - On macOS/Linux:
        ```bash
        .\env\Scripts\activate

5. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the Flask application:
   ```bash
   python app.py

2. Open a web browser and go to http://127.0.0.1:5000.

3. Click on "Go to ToDo" to navigate to the ToDo page.

4. Add, update, and delete tasks as needed.

## Project Structure
   ```csharp
    ├── app.py
    ├── requirements.txt
    ├── static
    │   └── css
    │       └── main.css
    ├── templates
    │   ├── base.html
    │   ├── index.html
    │   └── todo.html
    ├── test.db
    └── README.md