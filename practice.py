from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route('/about')
def about():
    return "this is my about page, welcome!"

if __name__ == "__main__":
    app.run(debug=True)