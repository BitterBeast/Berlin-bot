from flask import Flask
app = Flask(__name__)

@app.route('/')
def lotta_py():
    return 'Muhammad-Inan'


if __name__ == "__main__":
    app.run()
