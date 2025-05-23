from flask import Flask, render_template
from datetime import datetime
import locale

app = Flask(__name__)
locale.setlocale(locale.LC_TIME, '')


@app.route('/')
def homepage():
    # ango = "variable no usada para error linter"
    the_time = datetime.now().strftime("%A, %d %b %Y %H:%M")

    # Render HTML with variable
    return render_template("index.html", the_time=the_time, tema="dog",
                           alto="400", ancho="600")


@app.route('/status')
def status():
    return "OK Todo v1"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
