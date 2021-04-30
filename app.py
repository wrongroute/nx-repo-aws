from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(
        status='OK'
    )

@app.route('/hello')
def hello():
    return jsonify(
        status='Hello!'
    )

if __name__ == '__main__':
    app.run()
