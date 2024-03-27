from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f'<p>Hello, World!</p><p>Python version: {sys.version_info[0]}.{sys.version_info[1]}</p>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
