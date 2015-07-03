from flask import Flask, send_file, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/table")
def table():
    return render_template('table.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=80)
