from flask import Flask
from controllers import summarization_controller

app = Flask(__name__)

app.register_blueprint(summarization_controller, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Python API Project!"

# Add more routes here as needed

if __name__ == '__main__':
    app.run(debug=True)