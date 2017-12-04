from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/name/<name>')
def hello_world(name):
    return render_template("hello.html", name="raghu")


if __name__ == "__main__":
    app.run(debug=True)
