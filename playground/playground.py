from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template("index.html")


@app.route('/play/<x>')
def level_2(x):
    return render_template("index2.html", times=int(x))

@app.route('/play/<y>/<color>')
def level_3(y,color):
    return render_template("index3.html", times=int(y), text_color=color)

if __name__ == "__main__":
    app.run(debug=True)
