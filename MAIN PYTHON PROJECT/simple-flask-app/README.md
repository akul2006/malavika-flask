# Simple Flask App

This is a simple web application built using Flask. It serves as a basic template for creating web applications with Python.

## Project Structure

```
simple-flask-app
├── app.py
├── requirements.txt
├── static
│   └── style.css
├── templates
│   └── index.html
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd simple-flask-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command:
```
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

Once the application is running, you can visit the homepage to see the content rendered from the `index.html` template. You can modify the HTML and CSS files to customize the appearance and functionality of the application.

## License

This project is licensed under the MIT License.