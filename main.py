
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Gemma C++ GitHub Repositories</h1><ul><li><a href='https://github.com/google/gemma.cpp'>gemma.cpp</a></li><li><a href='https://github.com/google/gemma-cpp-examples'>gemma-cpp-examples</a></li></ul>"

@app.route('/api/repos')
def get_repos():
    repos = [
        {
            "name": "gemma.cpp",
            "url": "https://github.com/google/gemma.cpp"
        },
        {
            "name": "gemma-cpp-examples",
            "url": "https://github.com/google/gemma-cpp-examples"
        }
    ]
    return jsonify(repos)

if __name__ == '__main__':
    app.run()
